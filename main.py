import os
from tkinter import *
from tkinter import ttk
import json, hashlib, hmac, os #used for password hashing

# Maak het venster en zet het Azure light-thema aan.
root = tk.Tk()
root.title("Smart Security System")
root.geometry("640x480")

map_van_app = os.path.dirname(os.path.abspath(__file__))
thema_bestand = os.path.join(map_van_app, "azure.tcl")
root.tk.call("source", thema_bestand)
root.tk.call("set_theme", "light")

correct_user = "midas"
correct_password = "midas735"
systeem_actief = False

# autoconfig:
with open("data.json", "r", encoding="utf-8") as file:
    data = json.load(file)
    user_hash = data["Users"][0]["name"]
    pass_hash = data["Users"][0]["pass"]
    salt = data["Validation"][0]["salt"]

    try:
        salt = bytes.fromhex(salt)
        if len(salt) != 16:
            raise ValueError
    except (ValueError, TypeError):
        foutmelding.config(text="Salt is incorrect, er wordt een nieuwe gegenereerd...")
        salt = os.urandom(16)
        data["Validation"][0]["salt"] = salt.hex()

        with open("data.json", "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

def encrypter(text):
    iterations = 100_000
    password_hash = hashlib.pbkdf2_hmac('sha256', text.encode('utf-8'), salt, iterations)
    return password_hash

def verifier(text, hash):
    text_hash = encrypter(text)
    return hmac.compare_digest(hash, text_hash)


def inloggen():
    input_username = userentry.get()
    input_pass = passentry.get()
    input_username_hash = hashlib.sha256()
    input_username_hash.update(input_username)

    if input_username == correct_user and input_pass == correct_password:
        login_frame.pack_forget()
        dashboard_frame.pack(fill="both", expand=True, padx=25, pady=25)
    else:
        foutmelding.config(text="Gebruikersnaam of wachtwoord is onjuist.")
        passentry.delete(0, tk.END)


def systeem_wijzigen():
    global systeem_actief

    if systeem_actief:
        systeem_actief = False
        activelabel.config(text="Systeem inactief")
        activatebutton.config(text="Activeer systeem")
    else:
        systeem_actief = True
        activelabel.config(text="Systeem actief")
        activatebutton.config(text="Deactiveer systeem")


def open_deur():
    if systeem_actief:
        deurstatus.config(text="Status: open")


def open_achterdeur():
    if systeem_actief:
        achterdeurstatus.config(text="Status: open")


def open_achterraam():
    if systeem_actief:
        achterraamstatus.config(text="Status: open")


# Inlogscherm
login_frame = ttk.Frame(root, padding=25)
login_frame.pack(expand=True)

titel = ttk.Label(login_frame, text="SMART SECURITY", font=("Arial", 23, "bold"))
titel.pack(pady=(0, 20))

username = ttk.Label(login_frame, text="Vul je gebruikersnaam in")
username.pack(anchor="w")
userentry = ttk.Entry(login_frame, width=30)
userentry.pack(pady=(5, 15))

password = ttk.Label(login_frame, text="Vul je wachtwoord in")
password.pack(anchor="w")
passentry = ttk.Entry(login_frame, width=30, show="*")
passentry.pack(pady=(5, 10))

foutmelding = ttk.Label(login_frame, text="")
foutmelding.pack()

loginbutton = ttk.Button(login_frame, text="Log in", command=inloggen, style="Accent.TButton")
loginbutton.pack(fill="x", pady=10)
userentry.focus_set()

# Dashboard: dit frame wordt pas zichtbaar na het inloggen.
dashboard_frame = ttk.Frame(root)

ttk.Label(dashboard_frame, text="Smart Security System", font=("Arial", 20, "bold")).pack(pady=(0, 10))
ttk.Label(dashboard_frame, text="Je bent ingelogd").pack()

activelabel = ttk.Label(dashboard_frame, text="Systeem inactief", font=("Arial", 14))
activelabel.pack(pady=10)
activatebutton = ttk.Button(dashboard_frame, text="Activeer systeem", command=systeem_wijzigen, style="Accent.TButton")
activatebutton.pack(pady=(0, 20))

# Deur
deurframe = ttk.Frame(dashboard_frame)
deurframe.pack(fill="x", pady=5)
ttk.Label(deurframe, text="Deur", width=15).pack(side="left")
deurstatus = ttk.Label(deurframe, text="Status: dicht", width=15)
deurstatus.pack(side="left")
ttk.Button(deurframe, text="Simuleer opening", command=open_deur).pack(side="right")

# Achterdeur
achterdeurframe = ttk.Frame(dashboard_frame)
achterdeurframe.pack(fill="x", pady=5)
ttk.Label(achterdeurframe, text="Achterdeur", width=15).pack(side="left")
achterdeurstatus = ttk.Label(achterdeurframe, text="Status: dicht", width=15)
achterdeurstatus.pack(side="left")
ttk.Button(achterdeurframe, text="Simuleer opening", command=open_achterdeur).pack(side="right")

# Achterraam
achterraamframe = ttk.Frame(dashboard_frame)
achterraamframe.pack(fill="x", pady=5)
ttk.Label(achterraamframe, text="Achterraam", width=15).pack(side="left")
achterraamstatus = ttk.Label(achterraamframe, text="Status: dicht", width=15)
achterraamstatus.pack(side="left")
ttk.Button(achterraamframe, text="Simuleer opening", command=open_achterraam).pack(side="right")

root.mainloop()

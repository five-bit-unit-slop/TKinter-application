
from tkinter import *

root = Tk()

titel = Label(master=root,
text="SMART SECURITY",
font=("Arial", 23, "bold"),
fg="blue",)
titel.pack( padx=25, pady=20)

username = Label(master=root,
text="Vul je gebruikersnaam in",
font=("Arial", 10, ))
username.pack( padx=10, pady=10)

userentry = Entry(master=root)
userentry.pack( padx=10, pady=10)

password = Label(master=root,
text="Vul je wachtwoord in",
font=("Arial", 10, ))
password.pack( padx=10, pady=10)

passentry = Entry(master=root)
passentry.pack( padx=10, pady=10)

correct_user = "midas"
correct_password = "midas735"
def onclick():
    naam = userentry.get()
    wachtwoord = passentry.get()
    if naam == correct_user and wachtwoord == correct_password:
        root.destroy()
        open_dashboard()


button = Button(master=root,
text="Log in",
font=("Arial", 10, ),
command=onclick,)
button.pack( padx=25, pady=20)

def open_dashboard():
    dashboard = Tk()
    dashboard.title("Smart Security System")
    dashboard.geometry("600x400")
    dashboard.configure(bg="#00124f")


    label=Label(master=dashboard,
    text="Smart Security System",
                font=("Arial", 22, "bold"),
                fg="green",
                bg="#00124f")
    label.pack( padx=25, pady=20)

    label = Label(master=dashboard,
                  text="Je bent ingelogd",
                  font=("Arial", 20, ),
                  fg="green",
                  bg="#00124f",)
    label.pack(padx=25, pady=20)

    dashboard.mainloop()



root.mainloop()

# ballz
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

    activelabel = Label(master=dashboard,
                        text="Systeem inactief",
                        font=("Arial", 20,),
                        fg="#FF4848",
                        bg="#084B6D", )
    activelabel.pack(padx=10, pady=10)

    def onclick_deactivate():
        if activelabel.cget("text") == "Systeem inactief":
            activelabel.config(text="Systeem actief",
                           fg="#adc473")
        else:
            activelabel.config(text="Systeem inactief",
                               fg="#FF4848")

        if activatebutton.cget("text")== "Deactiveer systeem":
            activatebutton.config(text="Activeer systeem",
                                  fg="white",
                                  bg="green")
        else:
            activatebutton.config(text="Deactiveer systeem",
                                  fg="white",
                                  bg="red")




    activatebutton = Button(master=dashboard,
                    text="Deactiveer system",
                    fg="white",
                    bg="red",
                    command=onclick_deactivate)
    activatebutton.pack( padx=25, pady=20)

    activatebutton = Button(master=dashboard,
                            text="Activeer system",
                            fg="white",
                            bg="green",
                            font=("Arial", 15,),
                            command=onclick_deactivate)
    activatebutton.pack( padx=25, pady=20)


    def onclick_deursim():
        if activelabel.cget("text") == "Systeem actief":
            if deurstatus.cget("text")== "Status: dicht":
                deurstatus.config(text="Status: open", fg="#FF4848", bg="#02043C")

    def onclick_achterdeursim():
        if activelabel.cget("text") == "Systeem actief":
            if achterdeurstatus.cget("text") == "Status: dicht":
                achterdeurstatus.config(text="Status: open", fg="#FF4848", bg="#02043C")

    def onclick_achterraamsim():
        if activelabel.cget("text") == "Systeem actief":
            if achterraamstatus.cget("text") == "Status: dicht":
                achterraamstatus.config(text="Status: open", fg="#FF4848", bg="#02043C")

    deurframe = Frame(master=dashboard,
                      bg="#02043C")
    deurframe.pack(fill="x", padx=10, pady=10)

    deurlabel = Label(master=deurframe,
                      text="Deur",
                      fg="white",
                      bg="#02043C",
                      font=("Arial", 20,), )
    deurlabel.grid(row=0, column=0, sticky="w")

    deurstatus = Label(master=deurframe,
                       text="Status: dicht",
                       fg="#adc473",
                       bg="#02043C",
                       font=("Arial", 15,))
    deurstatus.grid(padx=140, row=0, column=1)

    deursim = Button(master=deurframe,
                     text="Simuleer opening",
                     font=("Arial", 9),
                     command=onclick_deursim)
    deursim.grid(row=0, column=2, )

    achterdeurframe = Frame(master=dashboard,
                            bg="#02043C")
    achterdeurframe.pack(fill="x", padx=10, pady=10)

    achterdeurlabel = Label(master=achterdeurframe,
                            text="Achterdeur",
                            fg="white",
                            bg="#02043C",
                            font=("Arial", 20,), )
    achterdeurlabel.grid(row=0, column=0, sticky="w")

    achterdeurstatus = Label(master=achterdeurframe,
                             text="Status: dicht",
                             fg="#adc473",
                             bg="#02043C",
                             font=("Arial", 15,))
    achterdeurstatus.grid(padx=67, row=0, column=1)

    achterdeursim = Button(master=achterdeurframe,
                           text="Simuleer opening",
                           font=("Arial", 9),
                           command=onclick_achterdeursim)
    achterdeursim.grid(padx=72, row=0, column=2, )

    achterraamframe = Frame(master=dashboard,
                            bg="#02043C")
    achterraamframe.pack(fill="x", padx=10, pady=10)

    achterraamlabel = Label(master=achterraamframe,
                            text="Achterraam",
                            fg="white",
                            bg="#02043C",
                            font=("Arial", 20,), )
    achterraamlabel.grid(row=0, column=0, sticky="w")

    achterraamstatus = Label(master=achterraamframe,
                             text="Status: dicht",
                             fg="#adc473",
                             bg="#02043C",
                             font=("Arial", 15,))
    achterraamstatus.grid(padx=60, row=0, column=1)

    achterraamsim = Button(master=achterraamframe,
                           text="Simuleer opening",
                           font=("Arial", 9,),
                           command= onclick_achterraamsim)
    achterraamsim.grid(padx=79, row=0, column=2)



    dashboard.mainloop()



root.mainloop()

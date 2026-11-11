
from tkinter import *

root = Tk()

label = Label(master=root,
text="SMART SECURITY",
font=("Arial", 23, "bold"),
fg="blue",)
label.pack( padx=25, pady=20)

label = Label(master=root,
text="Vul je gegevens in",
font=("Arial", 10, ))
label.pack( padx=25, pady=20)

entry = Entry(master=root)
entry.pack( padx=25, pady=20)


button = Button(master=root,
text="Log in",
font=("Arial", 10, ),)
button.pack( padx=25, pady=20)

root.mainloop()

import tkinter as tk
from tkinter import *
import sqlite3
import datetime
import os

connect = sqlite3.connect("contacts.db")
insert = connect.cursor()

def Addcontact():
    newWindow = tk.Toplevel(app)
    newWindow.title("Add User")
    newWindow.geometry("1595x795")
    newWindow.configure(bg="black")


    canvas = Canvas(newWindow, width=500, height=500, bg="black")
    canvas.pack()

    username = Entry (newWindow, width=100) 
    canvas.create_window(200, 50, window=username)
    username.insert(0, 'Enter username')

    phone = Entry (newWindow, width=100) 
    canvas.create_window(200, 100, window=phone)
    phone.insert(0, 'Enter phone number')

    email = Entry (newWindow, width=100) 
    canvas.create_window(200, 150, window=email)
    # email.insert(0, 'Enter email')

    # insert.execute("USE contacts")
    insert.execute(f"INSERT INTO contacts (username, phone, email) VALUES({username}, {phone}, {email})")
    insert.execute("SELECT * FROM contacts")
    result = insert.fetchall()

    for row in result:
        print(row)



app = tk.Tk()
app.title("Contacts")
app.geometry("1595x795")
app.configure(bg="black")

canvas = Canvas(app, width=1540, height=795, bg="black")
canvas.pack()
canvas.create_rectangle(150, 850, 0, 15, fill="grey")

adduser = tk.Button(app, 
              text="Add Contact",
              command=Addcontact)
adduser.pack()
adduser.place(x=5, y=35)


app.mainloop()
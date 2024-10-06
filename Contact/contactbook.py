import sqlite3
from tkinter import *
from tkinter import messagebox
import datetime
import os



connect = sqlite3.connect("contacts.db")
insert = connect.cursor()

# mydb = mysql.connector.connect(
#     user="root",
#     passwd="9570",
#     host="localhost",
#     database ="studentdb",
#     auth_plugin ='mysql_native_password',
#     use_pure = True
#     )

# insert = mydb.cursor()

# insert.execute("USE contacts")


root = Tk()
root.title("Contacts")
root.geometry("1535x795")
root.configure(bg="black")

canvas = Canvas(root, width=1540, height=795, bg="black")
canvas.pack()
canvas.create_rectangle(150, 850, 0, 15, fill="grey")

# messagebox.showinfo("When you click ok a new screen will appear. Fill the form", "Information")

def nextscreen(insert):
    newWindow = Toplevel(root)
  
    newWindow.title("Add user")
  
    newWindow.geometry("1535x795")

    canvas = Canvas(newWindow, width=500, height=500)
    canvas.pack()

    username = Entry (newWindow, width=100) 
    canvas.create_window(200, 50, window=username)
    username.insert(0, 'Enter username')

    phone = Entry (newWindow, width=100) 
    canvas.create_window(200, 100, window=phone)
    phone.insert(0, 'Enter phone number')

    email = Entry (newWindow, width=100) 
    canvas.create_window(200, 150, window=email)
    email.insert(0, 'Enter email')

    username1 = username.get()
    phone1 = phone.get()
    email1 = email.get()

    data = [username1, phone1, email1]

    def completeadduser():
        # add = "INSERT INTO contacts (username, phone, email) VALUES (%s, %s, %s)"
        # val = (username1, phone1, email1)
        insert.execute("INSERT INTO contacts (username phone email) VALUES (%s, %s, %s)", (username.get(), phone.get(), email.get()))
    # username = Entry (newWindow, width=100) 
    # canvas.create_window(200, 50, window=username)
    # username.insert(0, 'Enter username')

    # phone = Entry (newWindow, width=100) 
    # canvas.create_window(200, 100, window=phone)
    # phone.insert(0, 'Enter phone number')

    # email = Entry (newWindow, width=100) 
    # canvas.create_window(200, 150, window=email)
    # email.insert(0, 'Enter email')

    add = Button(newWindow, text="Add User", command=completeadduser())
    add.pack()

    label = Label(newWindow, text="Use someone else's name, phone number and email")
    label.pack()
    
    

adduser = Button(root, text="Add new contact", command=nextscreen(insert))
adduser.place(x=5, y=35)



root.mainloop()
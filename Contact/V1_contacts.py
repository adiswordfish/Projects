from tkinter import *
import sqlite3
import datetime
import os
import tkinter

def nextscreen(insert):
    # window = Tk()
    # window.title("Add User")
    # window.geometry("1535x795")
    # window.configure(bg="black")
    window = tkinter.Toplevel(root)

connect = sqlite3.connect("contacts.db")
insert = connect.cursor()

root = Tk()
root.title("Contacts")
root.geometry("1535x795")
root.configure(bg="black")

canvas = Canvas(root, width=1540, height=795, bg="black")
canvas.pack()
canvas.create_rectangle(150, 850, 0, 15, fill="grey")





adduser = Button(root, text="Add new contact", command=nextscreen(insert))
adduser.place(x=5, y=35)


root.mainloop()
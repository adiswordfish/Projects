from tkinter import *

import mysql.connector
# from test4people import MyPeople
# from test4people import MyPeople
# from test4 import Application

mydb = mysql.connector.connect(
    user="root",
    passwd="9570",
    host="localhost",
    database ="contacter",
    auth_plugin ='mysql_native_password',
    use_pure = True
    )
insert = mydb.cursor()

class Delete(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        print("adding?")
        self.geometry("1000x800")
        self.title("Delete Person")
        self.resizable(False, False)
        self.configure(bg="black")

        

        self.top = Frame(self, height=200, bg="white")
        self.top.pack(fill=X)

        self.bottom = Frame(self, height=1000, bg="#ebb134")
        self.bottom.pack(fill=X)

        # top frame design 
        # self.top_image = PhotoImage(file="14897105341556274008-128.png")
        # self.top_image_label = Label(self.top, image=self.top_image)
        # self.top_image_label.place(x=500, y=69.18)

        self.heading = Label(self.top, text="Delete Contact", font="arial 15 bold", bg="white", fg="#ebb434")
        self.heading.place(x=725, y=69.18)

        self.label_name = Label(self.bottom, text='Name:', font="arial 15 bold", fg="white", bg="#ebb434")
        self.label_name.place(y="50", x="100")

        self.entry_name = Entry(self.bottom, width=30, bd=4)
        self.entry_name.insert(0, "Enter your name")
        self.entry_name.place(y="50", x="400")

        self.label_surname = Label(self.bottom, text='Surname:', font="arial 15 bold", fg="white", bg="#ebb434")
        self.label_surname.place(y="100", x="100")

        self.entry_surname = Entry(self.bottom, width=30, bd=4)
        self.entry_surname.insert(0, "Enter your surname")
        self.entry_surname.place(y="100", x="400")

        note = Label(self.bottom, text="Enter name and surname of the contact you wish to delete", font="arial 15 bold", fg="white", bg="#ebb434")
        note.place(x=100, y=150)



        def delete():
            name = self.entry_name.get()
            surname = self.entry_surname.get()


            print(surname)
            print("calium")

            insert.execute("use contacter")
            insert.execute(f"delete from contactbookusers WHERE person_name =   '"+ name + "' and person_surname = '"+ surname + "'")
            mydb.commit()
 
        button = Button(self.bottom, text="Delete Contact", command=delete)
        button.place(y="400",x="400")
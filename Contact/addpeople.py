from tkinter import *
from tkinter import messagebox
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

class AddPeople(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        print("adding?")
        self.geometry("1000x800")
        self.title("Add New Person")
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

        self.heading = Label(self.top, text="Add Contact", font="arial 15 bold", bg="white", fg="#ebb434")
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

        self.label_email = Label(self.bottom, text='Email:', font="arial 15 bold", fg="white", bg="#ebb434")
        self.label_email.place(y="150", x="100")

        self.entry_email = Entry(self.bottom, width=30, bd=4)
        self.entry_email.insert(0, "Enter your email")
        self.entry_email.place(y="150", x="400")

        self.label_phone_number = Label(self.bottom, text='Phone Number:', font="arial 15 bold", fg="white", bg="#ebb434")
        self.label_phone_number.place(y="200", x="100")

        self.entry_phone_number = Entry(self.bottom, width=30, bd=4)
        self.entry_phone_number.insert(0, "Enter your phone number")
        self.entry_phone_number.place(y="200", x="400")

        self.label_adress = Label(self.bottom, text='Address:', font="arial 15 bold", fg="white", bg="#ebb434")
        self.label_adress.place(y="250", x="100")

        self.entry_adress = Entry(self.bottom, width=30, bd=4)
        self.entry_adress.insert(0, "Enter your Address")
        self.entry_adress.place(y="250", x="400")

        button = Button(self.bottom, text="Add Contact", command=self.add_people)
        button.place(y="400",x="400")


        # self.label_name = Label(self.bottom, text='Email:', font="arial 15 bold", fg="white", bg="#ebb434")
        # self.label_name.place(y="800", x="100")

        # self.entry_name = Entry(self.bottom, width=30, bd=4)
        # self.entry_name.insert(0, "Enter your email")
        # self.entry_name.place(y="800", x="400")

    def add_people(self):
        name = self.entry_name.get()
        surname = self.entry_surname.get()
        email = self.entry_email.get()
        phone = self.entry_phone_number.get()
        address = self.entry_adress.get()

        self.entry_adress.delete(0,"end")
        self.entry_email.delete(0,"end")
        self.entry_name.delete(0,"end")
        self.entry_phone_number.delete(0,"end")
        self.entry_surname.delete(0,"end")

        print(name,surname,email,phone,address)

        # data = name, surname, phone, address, email

        if name != "" and surname!= "" and email!= "" and phone!= "" and address != "":
            try:
                query ="INSERT INTO contactbookusers(person_name, person_Surname, person_phone, person_address, person_email) VALUES (%s, %s, %s, %s, %s)"
                # query = quer.replace("", '')
                insert.execute(query, (name, surname, phone, address, email))
                print(insert)
                print("it working ")
                mydb.commit()
                # people = Application()
                # return people
            except Exception as e:

                # messagebox.showerror("error", str(e))
                print(str(e))
            print("yoyo singer")
        else:
            messagebox.showerror("Error", "fill all the fields")

        

        return name,surname,email,phone,address


        
        

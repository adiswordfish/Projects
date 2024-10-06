from tkinter import *
import datetime
from test4people import MyPeople
from addpeople import AddPeople
from deletepeople import Delete
from aboutus import aboutus
from updatepeople import Update

date = datetime.datetime.now().date()
date = str(date)


class Application(object):
    def __init__(self, master):
        self.master = master

        # frames

        self.top = Frame(master, height=200, bg="white")
        self.top.pack(fill=X)

        self.bottom = Frame(master, height=1000, bg="#34baeb")
        self.bottom.pack(fill=X)

        # top frame design 
        # self.top_image = PhotoImage(file="icons8-add-phone-48.png")
        # self.top_image_label = Label(self.top, image=self.top_image)
        # self.top_image_label.place(x=500, y=69.18)

        self.heading = Label(self.top, text="My Contact Book", font="arial 15 bold", bg="white", fg="#ebb343")
        self.heading.place(x=725, y=69.18)

        self.nowdate = Label(self.top, text="Today's date " + date)
        self.nowdate.place(x=1000, y=69.18)

    

        # add people

        self.adduser = Button(self.bottom, text="   Add Contact   ", font="arial 12 bold", bg="#76aba2", fg="black")
        self.adduser.place(x=613.46, y=45)

        # about us

        self.aboutus = Button(self.bottom, text="   About Us   ", font="arial 12 bold", bg="#76aba2", fg="black")
        self.aboutus.place(x=613.46, y=90)

        def my_people():
            people = MyPeople()
            print("okay")
            return people


        # view people

        self.viewuser = Button(self.bottom, text="   My People   ", font="arial 12 bold", bg="#76aba2", fg="black", command=my_people)
        self.viewuser.place(x=613.46, y=0)

        def update():
            # seleted_item = self.listbox.curselection()
            # print(seleted_item)
            update = Update()
            return update

        def my_people():
            addpeople = AddPeople()
            print("test")
            return addpeople  

        def about():
            abus = aboutus()
            return abus

        def delete():
            deleting = Delete()
            return deleting

        btnadd = Button(self.bottom, text="Add", width=12, font='Sans 12 bold', command=my_people)
        btnadd.grid(row=0, column=2, padx=20, pady=10, sticky=N)

        btnupdate = Button(self.bottom, text="Update", width=12, font='Sans 12 bold', command=update)
        btnupdate.grid(row=0, column=2, padx=20, pady=50, sticky=N)

        btndisplay = Button(self.bottom, text="Display", width=12, font='Sans 12 bold')
        btndisplay.grid(row=0, column=2, padx=20, pady=90, sticky=N)

        btndelete = Button(self.bottom, text="Delete", width=12, font='Sans 12 bold', command=delete)
        btndelete.grid(row=0, column=2, padx=20, pady=130, sticky=N)
    
        btnaboutus = Button(self.bottom, text="About Us", width=12, font="Sans 12 bold", command=about)
        btnaboutus.grid(row=0, column=2, padx=20, pady=170, sticky=N)



root = Tk()
root.title("Contact book")
root.geometry("1000x800")
# root.configure(bg="black")
app = Application(root)































root.mainloop()


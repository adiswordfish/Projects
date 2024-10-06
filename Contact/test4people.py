# from _typeshed import Self
from tkinter import * 
# import font 
import mysql.connector
from addpeople import AddPeople
from aboutus import aboutus
from deletepeople import Delete
from tkinter import ttk
import tkinter as tk

mydb = mysql.connector.connect(
    user="root",
    passwd="9570",
    host="localhost",
    database ="contacter",
    auth_plugin ='mysql_native_password',
    use_pure = True
    )
# insert = mydb.cursor()

class MyPeople(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)

        mydb = mysql.connector.connect(
    user="root",
    passwd="9570",
    host="localhost",
    database ="contacter",
    auth_plugin ='mysql_native_password',
    use_pure = True
    )

        self.geometry("1000x800")
        self.title("Contact book people")
        self.resizable(False, False)
        self.configure(bg="#ebb134")

        self.top = Frame(self, height=200, bg="white")
        self.top.pack(fill=X)

        self.bottom = Frame(self, height=1000, bg="#ebb134")
        self.bottom.pack(fill=X)

        # top frame design 
        # self.top_image = PhotoImage(file="14897105341556274008-128.png")
        # self.top_image_label = Label(self.top, image=self.top_image)
        # self.top_image_label.place(x=500, y=69.18)
        sql_select_Query = "select * from contactbookusers"
        cursor = mydb.cursor()
        person = cursor.execute(sql_select_Query)
        # get all records
        records = cursor.fetchall()
        print("Total number of rows in table: ", cursor.rowcount)

        for row in records:
            a = ["Name = " + str(row[0]), "Surname = " +  str(row[1]),"Phone  = " +  str(row[2]),"Address  = " +  str(row[3]),"Email  = " +  str(row[4])]
            
            a = row[0], row[1], row[2], row[3], row[4]
            print(a)

        


        self.heading = Label(self.top, text="My Contacts", font="arial 15 bold", bg="white", fg="#ebb434")
        self.heading.place(x=725, y=69.18)

        # self.scroll = Scrollbar(self.bottom, orient=VERTICAL)

        # self.listbox = Listbox(self.bottom, width=100, height=100)
        # self.listbox.grid(row=0, column=0, padx=(40,0), pady=(40,0))
        # self.scroll.config(command=self.listbox.yview)
        # self.listbox.config(yscrollcommand=self.scroll.set, justify=CENTER)
        # self.listbox.insert(1, a)
        # self.listbox.pack(padx=10, pady=10, fill="both", expand=True)

        # for i in a:
        #     listbox.insert("", "{}".format(i))
        #     listbox.pack(padx=10, pady=10, fill="both", expand=True)
        # count = 0
        # for i in person:
        #     self.listbox.insert(count, str(i[0]) + " " + str(i[1]) + " " + str(i[2]))

        # try:
        
        # # query = quer.replace("", '')
        
        # for person in peoples:
        #     self.listbox.insert(count, str(person[0]) + " " + person[1] + " " + person[2])
        # print("it working ")
        # mydb.commit()
        # MyPeople()
        # except Exception as e:

                # messagebox.showerror("error", str(e))
            # print(str(e))

        trv = ttk.Treeview(self.bottom)
        trv.pack(side=LEFT, padx=20, pady=20, )

        trv["columns"]=("1", "2", "3", "4", "5")
        trv["show"]="headings"
        trv.column("1", width=150)#, ANCHOR='c')
        trv.column("2", width=150)#, ANCHOR='c')
        trv.column("3", width=150)#, ANCHOR='c')
        trv.column("4", width=150)#, ANCHOR='c')
        trv.column("5", width=150)#, ANCHOR='c')



        mydb = mysql.connector.connect(
            user="root",
            passwd="9570",
            host="localhost",
            database ="contacter",
            auth_plugin ='mysql_native_password',
            use_pure = True
            )
        insert = mydb.cursor()
        query = "SELECT * FROM contactbookusers"
        insert.execute(query)


        for i in insert:
            trv.insert("", 'end', iid=i[0], values=(i[0], i[1], i[2], i[3], i[4]))
            print(i)

        # self.scroll.grid(row=0, column=1, sticky=N+S)



    

        




    
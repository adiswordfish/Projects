
# from tkinter.constants import ANCHOR
import mysql.connector
from tkinter import ttk
import tkinter as tk
from tkinter import *

root = tk.Tk()
root.title("Contact book")
root.geometry("1000x800")
trv = ttk.Treeview(root)
trv.grid(row=1, column=1, padx=20, pady=20)

trv["columns"]=("1", "2", "3", "4", "5")
trv["show"]="headings"
trv.column("1", width=30)#, ANCHOR='c')
trv.column("2", width=80)#, ANCHOR='c')
trv.column("3", width=80)#, ANCHOR='c')
trv.column("4", width=80)#, ANCHOR='c')
trv.column("5", width=80)#, ANCHOR='c')



mydb = mysql.connector.connect(
    user="root",
    passwd="9570",
    host="localhost",
    database ="contacter",
    auth_plugin ='mysql_native_password',
    use_pure = True

    )
entry_name = Entry(root, width=30, bd=4)
# entry_name.insert("Enter your name")
entry_name.place(y="50", x="400")
insert = mydb.cursor()

entry_surname = Entry(root, width=30, bd=4)
# entry_surname.insert(0, "Enter your surname")
entry_surname.place(y="100", x="400")





# for i in insert:
#     trv.insert("", 'end', iid=i[0], values=(i[0], i[1], i[2], i[3], i[4]))
#     print(i)

def update():
            # query = ""
        # insert.execute("use contacter;")

        # insert.execute("update contactbookusers set person_name = 'Shilpa' where person_name = 'Test';")

        # mydb.commit()
        # a='person_name'
    a = entry_surname.get()
    b=entry_name.get()
    insert.execute("use contacter")
    insert.execute(f"delete from contactbookusers WHERE person_name =   '"+ b + "' and person_surname = '"+ a + "'")
    mydb.commit()


button = Button(root, text="Update Contact", command=update)
button.place(y="400",x="400")

root.mainloop()
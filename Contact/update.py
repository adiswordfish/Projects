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

insert.execute("use contacter;")

insert.execute("update contactbookusers set person_name = 'test' where person_name = 'Shilpa';")

mydb.commit()
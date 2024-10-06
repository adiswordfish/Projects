# from tkinter import *
import mysql.connector

mydb = mysql.connector.connect(
    user="root",
    passwd="9570",
    host="localhost",
    database ="contacter",
    auth_plugin ='mysql_native_password',
    use_pure = True
    )
insert = mydb.cursor()




# query = "insert into contactbookusers (person_name, person_surname, person_phone, person_address, person_email) Values ('adi', 'jha', '2342793', 'mumbai', 'blah@gmail.com');"
try:

    insert.execute("SELECT * FROM contactbookusers")
    print(insert)
    mydb.commit()
except mysql.connector.errors.InternalError as mcei:
    print(str(mcei))


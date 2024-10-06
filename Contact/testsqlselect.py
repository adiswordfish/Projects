import mysql.connector

mydb = mysql.connector.connect(
    user="root",
    passwd="9570",
    host="localhost",
    database ="contacter",
    auth_plugin ='mysql_native_password',
    use_pure = True
    )
# query = mydb.cursor()

# x = query.execute("select * from contactbookusers").fetchall()
# print(x)

# sql_select_Query = "select * from contactbookusers"
# cursor = mydb.cursor()
# cursor.execute(sql_select_Query)
# print(cursor)
cur = mydb.cursor()
persons = cur.execute("select * from 'contactbookusers'").fetchall()
print(persons)
# get all records
# records = cursor.fetchall()
# print("Total number of rows in table: ", cursor.rowcount)

# for row in records:
#     print("Name = ", row[0], )
#     print("Surname = ", row[1])
#     print("Phone  = ", row[2])
#     print("Address  = ", row[3])
#     print("Email  = ", row[4], "\n")
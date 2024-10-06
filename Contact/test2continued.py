from tkinter import *

o = Tk()

def event():  #creating button

     cid = t1.get()

     name = t2.get()

     email = t3.get()

     password = t4.get()

     print('your account is created')

     print('Full name is: ',cid,name)

     print('E-mail is: ',email)

     print('Password is: ',password)

b1 = Button(o, text='Sign up',command=event)

b1.pack()
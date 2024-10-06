from tkinter import *

o = Tk()


m1 = Label(text='First Name :')
m1.pack()

t1 = Entry()             # creating 4 entries for input data
t1.pack()
###
m2 = Label(text='Last Name:')
m2.pack()

t2 = Entry()
t2.pack()

m3 = Label(text='E-mail:')
m3.pack()
t3 = Entry()
t3.pack()

m4 = Label(text='Password:')
m4.pack()
t4= Entry()
t4.pack()


##
nex_T = Button(o, "Sign up", command=next)
nex_T.pack()

def next():
    import test2continued




o.mainloop()
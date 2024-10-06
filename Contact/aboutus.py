from tkinter import *

class aboutus(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)

        self.geometry("1595x795")
        self.title("About Us")
        self.resizable(False, False)
        self.top = Frame(self, height=1595, bg="#ffa500")
        self.top.pack(fill=BOTH)
        self.text = Label(self.top, text="Hey this is about us page"'\n this application is made for educational purpose' '\n you can contact us on, ''\n Instagram - Aditya Jha' 'Youtube - Aditya Jha', font="arial 14 bold", bg="#ffa500")

        self.text.place(x=750, y=350)

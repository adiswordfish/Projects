from tkinter import *
import random
import time


def nothing():
    pass

main = Tk()
frame_1 = Frame(main)
frame_1.grid(row=0, column=0)
main_canvas = Canvas(frame_1, width=200, height=200, bg='magenta')

oval = main_canvas.create_oval(20, 20, 40, 40, outline='black', fill='yellow')

main_canvas.pack()
frame_2 = Frame(main)
frame_2.grid(row=0, column=1)

'''
button2 = Button(main_canvas, text="Q", command=nothing, anchor=W)
button2.configure(width=3, activebackground="#33B5E5", relief=FLAT)
button2_window = main_canvas.create_window(10, 10, anchor=NW, window=button2)
button2.pack(side=TOP)
'''

label_f2_1 = Label(frame_2, text="")
label_f2_1.pack()

label_f2_2 = Label(frame_2, text="")
label_f2_2.pack()
x_current, y_current = 30, 30
for loops in range(86400):
    x_new = random.randint(10, 190)
    y_new = random.randint(10, 190)
    main_canvas.move(oval, x_new-x_current, y_new-y_current)
    x_current, y_current = x_new, y_new
    main_canvas.update()
    time.sleep(1)
    now = str(time.ctime())
    label_f2_2.configure(text=now[10:])
    label_f2_1.configure(text=now[0:10])
# print(time.localtime())

main.mainloop()
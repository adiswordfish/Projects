from tkinter import * 
window = Tk()  
window.geometry("1535x795")  
window.title("test")  
window.configure(bg="black")

canvas = Canvas(window, width=1535, height=795, bg="black")
canvas.pack()
canvas.create_rectangle(765, 395, 0, 0, fill="white")

window.mainloop() 
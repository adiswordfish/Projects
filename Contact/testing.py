import tkinter as tk
root = tk.Tk()
root.geometry("400x240")

def clearTextInput():
    textExample.delete("1.0","end")

textExample=tk.Text(root, height=10)
textExample.pack()
btnRead=tk.Button(root, height=1, width=10, text="Clear", 
                    command=clearTextInput)

btnRead.pack()

root.mainloop()
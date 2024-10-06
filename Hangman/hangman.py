import tkinter
from tkinter import *
from string import ascii_lowercase
import random
from functools import partial
import re
from tkinter import messagebox

root = tkinter.Tk()
root.title("Test")
root.geometry("1280x740")

counter = 0
images = [PhotoImage(file="hangman0.png"),PhotoImage(file="hangman1.png"),PhotoImage(file="hangman2.png"),PhotoImage(file="hangman3.png"),PhotoImage(file="hangman4.png"),PhotoImage(file="hangman5.png"),PhotoImage(file="hangman6.png")]
words = [
"abandon",
"black",
"cat",
"dove",
"election",
"down",
"vexing",
"irritating",
"ponder",
"thinking",
"yummy",
"delicious",
"clues",
"doctor",
"zebra",
"company",
"accomplish",
"audio",
"reliable"
]
button_identities = []
rnd=random.choice(words)
word=rnd

#### Display Keyboard
n = 0 
lenword = len(word)


blanks = [] #defining the list for final word
for j in range(lenword):
    blanks.append("_")
seperator = "  "
newblanks = seperator.join(blanks)
lblblanks = Label(text=f"{newblanks}", font=("Arial", 25))
lblblanks.place(x=500+(40*j), y=200)


def destory(): # destroys the screen 
    root.destroy()

def close():
    losemsgbox = messagebox.showerror("Lost",f"you lost the word was {word}. Press ok and start again to play again")
    closebutton = Button(root, text="close", command=destory())

def win():
    MsgBoxwin = tkinter.messagebox.showinfo('Win',f'You won. The word was {word}, hope you enjoyed the game')
    closebutton = Button(root, text="close", command=destory())
    
n_list = {""}

def locate(n):
  n_list.add(f"{n}")
  print(f"{n_list} oyoy")
  # nlisttuple = tuple(n_list)
  seperator4 = "  "
  nlisttuple = seperator4.join(n_list)
  displaynlisttuple = Label(text="Letters pressed: ",  font=("Arial", 25))
  displaynlisttuple.place(x=700, y=400)
  displaynlisttuple = Label(text=f"{nlisttuple}",  font=("Arial", 25))
  displaynlisttuple.place(x=700, y=450)
  global counter
  print(n)
  thereornot = re.findall(n, word)
  print(thereornot)
  if n in thereornot:
    for ai in range(lenword):
        if(word[ai])== n:
            n_list.add(n)
            print(f"{n_list} oyoy")
            print(n, "is found at ",ai+1 )
            del blanks[ai]
            blanks.insert(ai,n)
            seperator2 = "  "
            newblank2 = seperator2.join(blanks)
            lblblanks2 = Label(text=f"{newblank2}", font=("Arial", 25))
            lblblanks2.place(x=500+(40*j), y=200)
            seperator3 = ""
            newblanks3 = seperator3.join(blanks)
            textanswer = f"{newblanks3}"
            print(textanswer)
            if textanswer == word:
                win()
    print(blanks)
    print(counter)
        # n("state") = "disabled"
        # print(blanks)
  # print(n_list)
  else:

    
    imglabela = Label(text="")
    imglabela.config(image=images[counter])
    imglabela.grid(row=0, column=0, columnspan=3, padx=10, pady=40)
    #   n("state") = "disabled"
    counter+=1
    print(counter)
    if counter == 7:
      print("game over")
      close()
      losemsgbox = messagebox.showerror(f"you lost the word was {word}. Press ok and start again to play again")
      closebutton = Button(root, text="close", command=destory())
  print(n_list)
    
  # print(f"you have used {n_list}")

    # n("state") = "disabled"
    
  return counter

for i in ascii_lowercase:

  allatoz = Button(root, text=i, command=partial(locate, i), font= ("Helvetica 18"),width=4).grid(row=1+n//9, column=n%9)
  # my_text = allatoz.cget('text')

  button_identities.append(allatoz)
  n+=1

print(button_identities)

imglbl = Label(root)
imglbl.grid(row=0, column=0, columnspan=3, padx=10, pady=40)

wordlbl = StringVar()
Label(root,textvariable=wordlbl, font=("Consolas 24 bold")).grid(row=0, column=3, columnspan=6, padx=10)

root.mainloop()
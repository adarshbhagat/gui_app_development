from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
x = Tk()

r = "bang"#r will be asigned with int.

def clicked(value):
    mylabel = Label(x,text=value)
    mylabel.pack()

Radiobutton(x,text="option 1",variable=r,command=lambda: clicked("bang")).pack()
Radiobutton(x,text="option 2",variable=r,command=lambda: clicked("bbboooommmm")).pack()

messagebox.showinfo("this is my popup!","welcome")
# this will open a new popup and the title and text is passed in it.
x.mainloop()

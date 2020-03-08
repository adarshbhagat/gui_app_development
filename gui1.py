from tkinter import *

x = Tk()# creates a new window

y = Label(x,text="hello world")#write text in the new window

z=Label(x,text="welcome to tkinter")

y.pack()#It organizes the widgets in blocks before placing in the parent widget

z.pack()

x.mainloop()

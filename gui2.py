from tkinter import *

x = Tk()# creates a new window

y = Label(x,text="hello world")#write text in the new window

z=Label(x,text="welcome to tkinter")

y.grid(row=0,column=0)
#grid method divides screen into grids and place labels according
#to given location. representation of rows and columns are relative

z.grid(row=0,column=1)

x.mainloop()

from tkinter import *

x = Tk()#creates a new window

li=Label(x,text="enter your name")
li.pack()

e = Entry(x,width="50",bg="black",fg="white",borderwidth="3")
#taking input in e
#fg denotes text color
#bg denotes background color
#borderwidth denotes width of input box's border.

#e.insert(0,"enter your name: ")insert the text at 0th index

e.pack()

def ccc():
    l=Label(x,text="i love you "+e.get(),bg="red",fg="white")
    l.pack()

b = Button(x,text="Click here",command=ccc)
#creating button.
#padx represents the no of pixel in x axis and same thing is for pady.
#command = ccc will call the ccc function upon mouse click.

b.pack()

x.mainloop()

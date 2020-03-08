from tkinter import *

x = Tk()#creates a new window

def ccc():
    l=Label(x,text="hello world")
    l.pack()

b = Button(x,text="Click me!",padx=50,pady=50,command=ccc,fg="green",bg="blue")
#creating button.
#padx represents the no of pixel in x axis and same thing is for pady.
#command = ccc will call the ccc function upon mouse click.
#fg is the text color
#bg will denote the background color

b.pack()

x.mainloop()

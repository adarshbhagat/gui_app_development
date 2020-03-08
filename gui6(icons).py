from tkinter import *
from PIL import ImageTk,Image
x = Tk()
x.title('adarsh') #displays this in title bar
#x.iconbitmap("icon.jpg")

button_quit = Button(x,text="exit program",command=x.quit)

#displays this icon in title bar
my_img = ImageTk.PhotoImage(Image.open("try.jpg"))
my_label = Label(image=my_img)
my_label.pack()
button_quit.pack()
x.mainloop()

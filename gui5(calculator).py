from tkinter import *

x = Tk()#creates a new window
x.title("calculator")
#putting text in title bar
f_num=int(0)
math="null"
e = Entry(x,width="40",borderwidth="10")
e.grid(row=0,column=0,columnspan=3, padx=10,pady=10)

def b_click(number):
    current = e.get()
    e.delete(0,END)#deleting existing thing in box
    e.insert(0,str(str(current) + str(number)))
    return
def b_clea(x):
    e.delete(0,END)
    global f_num
    f_num=int(0)
    return

def b_ad(x):
    global math
    math="addition"
    first_number=e.get()
    global f_num
    f_num=f_num+int(first_number)
    e.delete(0,END)
    return

def b_sub(x):
    global math
    math="substraction"
    first_number=e.get()
    global f_num
    f_num=f_num+int(first_number)
    e.delete(0,END)
    return

def b_mul(x):
    global math
    math="multiplication"
    first_number=e.get()
    global f_num
    f_num=f_num+int(first_number)
    e.delete(0,END)
    return

def b_div(x):
    global math
    math="division"
    first_number=e.get()
    global f_num
    f_num=f_num+int(first_number)
    e.delete(0,END)
    return

def b_equal(x):
    global math
    global f_num
    if math == "addition":
        x=f_num+int(e.get())
    if math == "substraction":
        x=f_num-int(e.get())
    if math == "multiplication":
        x=f_num*int(e.get())
    if math == "division":
        x=f_num/int(e.get())
    f_num=int(0)
    e.delete(0,END)
    e.insert(0,str(x))
    math="null"
    return

#creating buttons
b_1 = Button(x,text="1",padx=40,pady=20,command=lambda:b_click(1))#we can't 
b_2 = Button(x,text="2",padx=40,pady=20,command=lambda:b_click(2))#pass arguments
b_3 = Button(x,text="3",padx=40,pady=20,command=lambda:b_click(3))#in buttons
b_4 = Button(x,text="4",padx=40,pady=20,command=lambda:b_click(4))
b_5 = Button(x,text="5",padx=40,pady=20,command=lambda: b_click(5))
b_6 = Button(x,text="6",padx=40,pady=20,command=lambda: b_click(6))
b_7 = Button(x,text="7",padx=40,pady=20,command=lambda: b_click(7))
b_8 = Button(x,text="8",padx=40,pady=20,command=lambda: b_click(8))
b_9 = Button(x,text="9",padx=40,pady=20,command=lambda: b_click(9))
b_0 = Button(x,text="0",padx=40,pady=20,command=lambda: b_click(0))
b_add = Button(x,text="+",padx=39,pady=20,command=lambda: b_ad(0))
b_equals = Button(x,text="=",padx=91,pady=20,command=lambda: b_equal(0))
b_clear = Button(x,text="Clear",padx=79,pady=20,command=lambda: b_clea(0))

b_substract = Button(x,text="-",padx=41,pady=20,command=lambda: b_sub(0))
b_multiply = Button(x,text="*",padx=41,pady=20,command=lambda: b_mul(0))
b_divide = Button(x,text="/",padx=41,pady=20,command=lambda: b_div(0))
#putting buttons on screen

b_1.grid(row=3,column=0)
b_2.grid(row=3,column=1)
b_3.grid(row=3,column=2)

b_4.grid(row=2,column=0)
b_5.grid(row=2,column=1)
b_6.grid(row=2,column=2)

b_7.grid(row=1,column=0)
b_8.grid(row=1,column=1)
b_9.grid(row=1,column=2)

b_0.grid(row=4,column=0)
b_add.grid(row=5,column=0)
b_equals.grid(row=5,column=1,columnspan=2)
b_clear.grid(row=4,column=1,columnspan=2)

b_substract.grid(row=6,column=0)
b_multiply.grid(row=6,column=1)
b_divide.grid(row=6,column=2)

x.mainloop()

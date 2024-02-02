import tkinter
from tkinter import *
root=tkinter.Tk()
a=IntVar()
d=StringVar()
def chkorder():
    s="your order is:"
    if(a.get()==1):
        s+="Tea "
    elif(a.get()==2):
        s+="Coffee "
    elif(a.get()==3):
        s+="Soft Drink "
    d.set(s)
def clr():
    a.set(0)
    d.set("order: ")
c1=Radiobutton(root,text="Tea",value=1,variable=a)
c2=Radiobutton(root,text="Coffee",value=2,variable=a)
c3=Radiobutton(root,text="Soft Drink",value=3,variable=a)
b1=Button(root,text="order",command=chkorder)
b2=Button(root,text="clear",command=clr)
l1=Label(root,text="order",textvariable=d)
c1.grid(row=0,column=0)
c2.grid(row=1,column=0)
c3.grid(row=2,column=0)
b1.grid(row=3,column=0)
b2.grid(row=3,column=1)
l1.grid(row=4,column=0)
root.mainloop()

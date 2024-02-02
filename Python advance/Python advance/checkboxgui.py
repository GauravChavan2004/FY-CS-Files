import tkinter
from tkinter import *
root=tkinter.Tk()
a=IntVar()
b=IntVar()
c=IntVar()
d=StringVar()
def chkorder():
    s="your order is:"
    if(a.get()==1):
        s+="Tea "
    if(b.get()==1):
        s+="Coffee "
    if(c.get()==1):
        s+="Soft Drink "
    d.set(s)
def clr():
    a.set(0)
    b.set(0)
    c.set(0)
    d.set("order ")
c1=Checkbutton(root,text="Tea",onvalue=1,offvalue=0,variable=a)
c2=Checkbutton(root,text="Coffee",onvalue=1,offvalue=0,variable=b)
c3=Checkbutton(root,text="Soft Drink",onvalue=1,offvalue=0,variable=c)
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

import tkinter
from tkinter import*
root= tkinter.Tk()
a=StringVar()
b=StringVar()
c=StringVar()
def chklog():
    x=a.get()
    y=b.get()
    if(x=="admin" and y=="admin"):
        c.set(" login.successful!!!")
    else:
        c.set("login.incorrect")
def clrlog():
    a.set(" ")
    b.set(" ")
    c.set("Result:")
l1=Label(root,text="enter username")
l2=Label(root,text="enter password")
l3=Label(root,text="Result", textvariable=c)
t1=Entry(root,textvariable=a)
t2=Entry(root,show="#",textvariable=b)
b1=Button(root,text="login",command=chklog)
b2=Button(root,text="cancel", command=clrlog)
l1.pack()
t1.pack()
l2.pack()
t2.pack()
b1.pack()
b2.pack()
l3.pack()
root=mainloop()


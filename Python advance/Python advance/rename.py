import os
f=open("abc.txt","r")
f1=open("D:/xyz/abc.txt","w")
x=f.read()
f1.write(x)
f1.close()
f.close()
os.rename("abc.txt","x.txt")

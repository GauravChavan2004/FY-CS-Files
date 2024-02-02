f=open("abc.txt","r")
x=f.readlines()
i=1
for b in x:
    print("\n",i,")",b)
    i+=1
f.close()

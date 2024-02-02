def yrange (n):
    i=0
    while(i<n):
        yield i
        i+=1
y=yrange(5)
print(y.__next__())
print(y.__next__())
print(y.__next__())
print(y.__next__())

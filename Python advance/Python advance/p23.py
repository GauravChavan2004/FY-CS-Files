def yrange(n):
    i=0
    while (i<n):
        yield i
        i+=1
y=yrange(5)
print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))

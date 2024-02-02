x=[10,20,30,40]
y=iter(x)
print(next(y))
print(next(y))
print(next(y))
print(y.__next__())
print(y.__next__())
print(y.__next__())

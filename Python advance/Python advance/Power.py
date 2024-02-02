class PowerTwo:
    def __init__(self,max=0):
        self.n=0
        self.max=max
    def __iter__(self):
        return self
    def __next__(self):
        if(self.n <= self.max):
            result=2** self.n
            self.n+=1
            return result
        else:
            raise StopIteration
ans=PowerTwo(5)
print (next(ans))
print (next(ans))           
print (next(ans)) 
print (next(ans))
print (next(ans))       


        

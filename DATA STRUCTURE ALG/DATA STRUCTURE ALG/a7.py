def split(arr):
    return(arr[:len(arr)//2],arr[len(arr)//2:])
def merge(left,right):
    leftIndex=0
    righrindex=0
result=[]
while leftIndex<len(left)and rightIndex<len(right):
    if left[leftIndex]<=right[rightIndex]:
        result.append(left[leftIndex])
        leftIndex+=1
    else:
        result.append(right[rightIndex])
        rightIndex+=1
    if leftIndex<len(left):
        result.extend(left[leftIndex:])
        

def bubble_sort(array):
    n = len(array)

    for i in range(n):
        
        already_sorted = True

        
        for j in range(n - i - 1):
            if array[j]>array[j + 1]:
                
                array[j],array[j + 1] =array[j + 1],array[j]
                already_sorted = False
        if already_sorted:
            break
    return array
array = [64, 34, 25, 12, 22, 11, 90]
 
bubble_sort(array)
 
print("Sorted array is:")
for i in range(len(array)):
    print("% d" % array[i], end=" ")

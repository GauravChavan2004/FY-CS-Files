def insertion_sort(array):
    for i in range(1, len(array)):
        key_item = array[i]

        j = i - 1
        while j >= 0 and array[j] > key_item:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key_item

    return array
array = [200,30,50,6,90,34,23]
 
insertion_sort(array)
 
print("Sorted array is:")
for i in range(len(array)):
    print("% d" % array[i], end=" ")

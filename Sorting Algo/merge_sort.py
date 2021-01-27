def mergeSort(array):

    #split to small parts
    if len(array)<=1: return array

    mid = len(array)//2
    left = array[:mid]
    right = array[mid:]

    left = mergeSort(left)
    right = mergeSort(right)

    #sort 
    block = []
    l = r = 0
    while l<len(left) and r<len(right):
        if left[l]<right[r]:
            block.append(left[l])
            l+=1
        else:
            block.append(right[r])
            r+=1
    
    #append the remaining values
    if l < len(left):
        block+=left[l:]
    elif r < len(right):
        block+=right[r:]
    
    return block


print(mergeSort([8, 5, 2, 9, 5, 6, 3]))

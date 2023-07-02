def mergesort(array: list):
    pivot = array[-1] # use last element as pivot
    for i, num in enumerate(array):
        if num > pivot:
            pointer = i
        else: # if smaller element than pivot found, smaller element swapped withlarger element
            array[i] = array[pointer]
            array[i-1] = num
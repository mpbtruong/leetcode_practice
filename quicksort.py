# def quickSort(arrayay: list, start: int, end: int):
#     if start < end:
#         pivotIndex = splitList(arrayay, start, end)
#         quickSort(arrayay, start, pivotIndex-1)
#         quickSort(arrayay, pivotIndex+1, end)

# def splitList(arrayay: list, start: int, end: int):

def quickSort(array):
    # Quicksort when the starting pivot is the first element of the array
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
        less = [x for x in array[1:] if x <= pivot]
        greater = [x for x in array[1:] if x > pivot]
        return quickSort(less) + [pivot] + quickSort(greater)

if __name__ == "__main__":
    my_list = [4, 2, 8, 1, 5, 3, 7, 6]
    sorted_list = quickSort(my_list)
    print(sorted_list)
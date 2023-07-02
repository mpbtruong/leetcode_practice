def bubblesort(array: list):
    history = {}
    # starting with first element (i=0) in array,
    # iterate over every single element in the list to compare with element to its right,
    # -1 because don't compare starting element with itself.
    for i in range(len(array)-1):
        # -i because in every iteration of bubblesort, the largest value in the list of elements to sort is brought to
        # the right, so don't need to check the righthand side of the list
        for j in range(len(array)-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j] 
        history[str(i)] = array[:j+1].copy()

if __name__ == "__main__":
    my_list = [2, 1, 3, 1, 1]
    bubblesort(my_list)
    assert my_list == [1, 1, 1, 2, 3]

    my_list = [4, 2, 8, 1, 5, 3, 7, 6]
    bubblesort(my_list)
    assert my_list == [1, 2, 3, 4, 5, 6, 7, 8]

    my_list = [2, 8, 5, 3, 9, 4 ,1]
    bubblesort(my_list)
    assert my_list == [1, 2, 3, 4, 5, 8, 9]

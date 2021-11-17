"""Written by Jakob Adamsson"""
def insertionsort(unsorted_array):
    '''
    Args:
        unsorted_array list: unosrted unsorted_array
    Returns:
        list: sorted unsorted_array
    '''
    for i in range(1, len(unsorted_array)):
        #get element a[i] starting at index 1
        key = unsorted_array[i]
        #grab previous element idx
        idx = i - 1
        while idx > -1 and unsorted_array[idx] > key:
            unsorted_array[idx+1] = unsorted_array[idx]
            idx -= 1
        #assign the replaced lower element with the value of key
        unsorted_array[idx+1] = key
    return unsorted_array
      
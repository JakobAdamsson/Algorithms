"""Written by Jakob Adamsson"""
def quicksort(array):
    """Args: array (list): An array containing ints
Returns: list: A sorted array, acsending order"""
    lengt = len(array)
    #basecase, if array is trivial lenght, return
    if lengt <= 1:
        return array
    pivot_element = array.pop()
    small_arr = []
    large_arr = []
    #loops through array and soring values by large and small
    for element in array:
        #if lower, put in small list
        if element < pivot_element:
            small_arr.append(element)
        #put it in large list
        else:
            large_arr.append(element)
    #preform quicksort on the small array, pivot_element and large arrag untill basecase
    return quicksort(small_arr) + [pivot_element] + quicksort(large_arr)

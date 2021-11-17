"""Heapsort algoritm written by Jakob Adamsson"""
def swap(any_arr, idx1, idx2):
    """Swaps two elements with each other, constant time compexity"""
    any_arr[idx1], any_arr[idx2] = any_arr[idx2], any_arr[idx1]
    return any_arr

def left(i):
    """Calculates index of left child idx"""
    return 2*i+1

def right(i):
    """Calculates index of right child idx"""
    return 2*i+2

def max_heap(unsorted_arr, idx_i, arr_size):
    """---O(n) time complexity, making the array max heap"""
    #find left and right child
    left_child = left(idx_i)
    right_child = right(idx_i)
    #get max value idx
    max_idx = idx_i
    #comparing
    if left_child < arr_size and unsorted_arr[idx_i] <unsorted_arr[left_child]:
        max_idx = left_child
    if right_child < arr_size and unsorted_arr[max_idx] < unsorted_arr[right_child]:
        max_idx = right_child
    #if max_idx has change, that is, its not i
    if max_idx != idx_i:
        swap(unsorted_arr, max_idx, idx_i)
        max_heap(unsorted_arr, max_idx, arr_size)

def heapsort(unsorted_arr):
    """O(nlogn) time complexity, Sorting the max heap"""
    #get len of arr
    lenght = len(unsorted_arr)
    #make it max heap
    for i in range(lenght//2, -1, -1):
        max_heap(unsorted_arr, i, lenght)
    #sorting the max heap
    for i in range(len(unsorted_arr)-1, 0, -1):
        swap(unsorted_arr, 0, i)
        lenght -= 1
        max_heap(unsorted_arr, 0, lenght)
    return unsorted_arr

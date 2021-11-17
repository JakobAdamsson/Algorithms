import time
import random
from heapsort import heapsort
from insertionsort import insertionsort
from quicksort import quicksort

def create_lst(lenght):
    return [random.randint(1, 10000) for nbr in range(1, lenght)]

#put algoritms in dict for easy use in for loop later
algoritms = {'heapsort': heapsort, 'insertionsort': insertionsort, 'quicksort': quicksort}

#get time for algoritm with 1000 elements
print('Started sorting process of 50000 elements')
for name, algoritm in algoritms.items():
    lst_50000 = create_lst(50000)
    start = time.time()
    algoritm(lst_50000) 
    end = time.time()
    print(f'{name} sorterade listan på {end-start} sekunder')
    lst_50000 = []
    time.sleep(2)
print('Sorting of 50000 elements ended \n')

#get time for algoritm with 10000 elements
print('Started sorting process of 100000 elements ')
for name, algoritm in algoritms.items():
    lst_100000 = create_lst(100000)
    start = time.time()
    algoritm(lst_100000)
    end = time.time()
    print(f'{name} sorterade listan på {end-start} sekunder')
    lst_100000 = []
    time.sleep(2)
print('Sorting of 100000 elements ended')
print('All done!')
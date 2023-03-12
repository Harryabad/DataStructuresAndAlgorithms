# Big O Notation
# O(log n)

import sys
from load import load_numbers

numbers = load_numbers(sys.argv[1])

def quicksort(values):
    # if list size is zero or one, it is already sorted
    if len(values) <= 1:
        return values
    # divide and conquer 
    less_than_pivot = []
    greater_than_pivot = []
    pivot = values[0]
    for value in values[1:]:
        if value <= pivot:
            less_than_pivot.append(value)
        else:
            greater_than_pivot.append(value)
    print("%15s %1s %-15s" % (less_than_pivot, pivot, greater_than_pivot))
    return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)

print(numbers)  
sorted_numbers = quicksort(numbers)
print(sorted_numbers)

# [3, 6, 0, 9, 3, 5, 7, 4]
#          [0, 3] 3 [6, 9, 5, 7, 4]
#              [] 0 [3]
#          [5, 4] 6 [9, 7]
#             [4] 5 []
#             [7] 9 []
# [0, 3, 3, 4, 5, 6, 7, 9]

import sys
from load import load_numbers

numbers = load_numbers(sys.argv[1])

def selection_sort(values):
    sorted_list = []
    print("%-25s %-25s" % (values, sorted_list))
    for i in range(0, len(values)):
        index_to_move = index_of_min(values)
        sorted_list.append(values.pop(index_to_move))
        print("%-25s %-25s" % (values, sorted_list))
    return sorted_list

def index_of_min(values):
    min_index = 0

    for i in range(1, len(values)):
        if values[i] < values[min_index]:
             min_index = i
    return min_index

print(selection_sort(numbers))

# [3, 6, 0, 9, 3, 5, 7, 4]  []
# [3, 6, 9, 3, 5, 7, 4]     [0]
# [6, 9, 3, 5, 7, 4]        [0, 3]
# [6, 9, 5, 7, 4]           [0, 3, 3]
# [6, 9, 5, 7]              [0, 3, 3, 4]
# [6, 9, 7]                 [0, 3, 3, 4, 5]
# [9, 7]                    [0, 3, 3, 4, 5, 6]
# [9]                       [0, 3, 3, 4, 5, 6, 7]
# []                        [0, 3, 3, 4, 5, 6, 7, 9]
# [0, 3, 3, 4, 5, 6, 7, 9]
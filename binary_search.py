# Binary Search only works on sorted values
# Big O Notation
# O(log n)

def binary_search(list, target):
    first = 0
    last = len(list)-1

    while first <= last:
        midpoint = (first + last)//2

        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1

    return None

def verify(index):
    if index is not None:
        print("Target found at index:", index)
    else:
        print("Target not found in list")


numbers = [x for x in range(1,11)]

result = binary_search(numbers, 12)
verify(result)

result = binary_search(numbers, 6)
verify(result)

# Target not found in list
# Target found at index: 5
import random

def merge_sort(list):
    """
    Sorts a list in ascending order
    Returns a new sorted list
    
    Divide: Find the midpoint of list and divide into sublist
    Conquer: Recursively sort the sublists created in previous step
    Combine: Merge the sorted sublisted created in previous step
    Takes overall O(kn log n) time   takes n form merge * k log n from split
    """

    if len(list) <= 1:
        return list
    
    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)

def split(list):
    """
    Divide the unsorted list at midpoint into sublist
    Returns two sublists - left and right
    Takes overall O(k log n) time
    k slice for each split
    """
    mid = len(list)//2
    left = list[:mid]
    right = list[mid:]

    return left, right

def merge(left, right):
    """
    Merges two lists - Arrays, sorting them in the process
    Returns a new merged list
    runs in overall O(n) time
    """

    l = []
    i = 0
    j = 0

    while i < len(left) and j < len(right): # if left list is shorter will terminate too early and return false
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1


    # right list shorter than the left
    while i < len(left):
        l.append(left[i])
        i += 1

     # left list shorter than the right
    while j < len(right):
        l.append(right[j])
        j += 1
    
    return l



def verify_sorted(list):
    n = len(list)
    
    if n == 0 or n == 1:
        return True
    
    return list[0] < list[1] and verify_sorted(list[1:])



numbers = random.sample(range(1,101), 9)
print(numbers, verify_sorted(numbers))
l = merge_sort(numbers)
print(l, verify_sorted(l))

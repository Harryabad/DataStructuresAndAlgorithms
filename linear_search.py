def linear_search(list, target):
    """
    Returns index position of target if found, else none
    """
    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return None

def verify(index):
    if index is not None:
        print("Target found at index:", index)
    else:
        print("Target not found in list")

numbers = [x for x in range(1,11)]

result = linear_search(numbers, 12)
verify(result)

result = linear_search(numbers, 6)
verify(result)
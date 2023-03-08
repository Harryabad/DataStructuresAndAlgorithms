def sum(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

def recursive_sum(numbers):
    
    if not numbers:
        # if list is empty
        return 0
    print("calling sum(%s)" % numbers[1:])
    remaining_sum = recursive_sum(numbers[1:])
    print("call to sum(%s) returning %d + %d" % (numbers, numbers[0], remaining_sum))
    
    return numbers[0] + remaining_sum


numbers = [0, 1, 2, 3, 4]

print(recursive_sum(numbers))

# calling sum([1, 2, 3, 4])
# calling sum([2, 3, 4])
# calling sum([3, 4])
# calling sum([4])
# calling sum([])
# call to sum([4]) returning 4 + 0
# call to sum([3, 4]) returning 3 + 4
# call to sum([2, 3, 4]) returning 2 + 7
# call to sum([1, 2, 3, 4]) returning 1 + 9
# call to sum([0, 1, 2, 3, 4]) returning 0 + 10
# 10
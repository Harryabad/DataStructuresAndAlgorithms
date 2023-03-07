""" Bogo_sort is deliberately bad
    1. Randomise list
    2. is it sorted?
    3. if not GOTO 1
"""

import random
import sys
from load import load_numbers

numbers = load_numbers(sys.argv[1])
#numbers = load_numbers("numbers/5.txt")
#numbers = load_numbers("numbers/8.txt")

def is_sorted(values):
    # if the list is sorted every value that comes next will be greater than the current value
    for index in range(len(values) - 1):
        if values[index] > values[index + 1]:
            return False
    return True

def bogo_sort(values):
    attempts = 0
    while not is_sorted(values):
        print(attempts)
        random.shuffle(values)
        attempts += 1
    return values


print(bogo_sort(numbers))

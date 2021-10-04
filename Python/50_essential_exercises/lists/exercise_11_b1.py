# Given a sequence of positive and negative numbers, sort them by absolute
# value.

import random

numbers = [random.randrange(-100, 100) for i in range(10)]

def absolute_sort(seq):
    return sorted([abs(i) for i in seq])


print(numbers)
print(absolute_sort(numbers))

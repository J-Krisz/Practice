# Given a list of lists, with each list containing zero or more numbers, sort
# by the sum of each inner lists numbers.

import random

lol = [[random.randint(0, 25) for i in range(9)]for j in range(9)]

def sum_of_inner_lists(list_of_lists):
    return sorted(list_of_lists, key=sum)



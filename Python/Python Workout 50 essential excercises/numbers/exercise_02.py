####################
# Summing numbers  #
####################

# Re-implement the built in sum() function so that it takes a variable amount of
# arguments instead of one sequence, like so my_sum(1, 2, 3) instead of
# my_sum([1, 2, 3]) 

def my_sum(*args):

    output = 0

    for num in args:
        output += num

    return output

print(my_sum(1, 2, 3))

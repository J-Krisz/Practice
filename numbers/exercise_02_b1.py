####################
# Summing numbers  #
####################

# The built in version of sum() takes an optional argument, which is used as the
# starting point of the summing. So sum([1, 2, 3], 4) returns 10. Re-implement
# the my_sum() function such that it works in this way. If second argument is
# not provided it should default to 0

# ** Note that while you can wwrite a function that defines a parameter afte
# *args, I'd suggesdt avoiding it and just taking two arguments --a list  and an
# optional starting point.

def my_sum(numbers, start=0):

    output = 0

    for num in numbers:
        output += num

    return start + output

to_sum = [i for i in range(6)]

print(my_sum(to_sum, 10))

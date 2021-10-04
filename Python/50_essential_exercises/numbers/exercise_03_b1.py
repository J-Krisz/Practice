##############
# Run timing #
##############

# Write a function that takes a float and two integers (before and after). The
# fuction should return a float consisting of before digits before the decimal
# point and after digits after. Thus, if we call the function with 1234.5678, 2
# and 3, the return value shuld be 34.567

def two_sides_of_the_dot(number, before, after):

    # first we cast the number to str()
    string = str(number)
    # than we index the floating point
    point_index = string.find(".")

    return string[point_index - before:point_index + after + 1]


print(two_sides_of_the_dot(1234.5678, 2, 3))

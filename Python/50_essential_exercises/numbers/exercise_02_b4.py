###################
# Summing numbers #
###################

# Write a function tha takes a list of Python objects. Sum the objects that
# either are integers or can be turned into integers, ignoring others.

def is_int(elem):

    try:
        int(elem)
    except ValueError:
        print(f"{elem} can not be type casted to int")

def sum_obj(objects):

    output = [elem for elem in objects if is_int(elem)]
    return sum(output)


print(sum_obj())

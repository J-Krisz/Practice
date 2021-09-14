####################
# Lists and Tuples #
####################


# Write a function, firstlast(), that takes sequence (string, list or tuple)
# and returns the first and last elements of that sequence, in a two-element
# sequence of hte same type. So firstlast('abc') will return the string as,
# while firstlast([1, 2, 3, 4]) will return the list [1, 4].


def firstlast(element):
    return element[:1] + element[-1:]

print(firstlast("asd"))
print(firstlast([1, 2, 3, 4]))

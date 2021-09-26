# Re-define the mysum() function from chapter one. Such that it can take any
# number of arguments. The arguments must all be of the same type and know how
# to respond to the + operator. (Thus, the function should work with any
# numbers, strings, lists and tuplse but not with sets and dicts).
# The result should be a new, longer sequence of the type provide by the
# parameters. Thus, the result of mysum('abc', 'def') will be the string
# 'abcdef', and the result of mysume([1,2,3], [4,5,6]) will be the six-element
# list [1,2,3,4,5,6]. Of  course, it should alse still return the integer 6 if
# we invoke mysum(1,2,3).


def mysum(*args):

    if not args:
        return args
    res = args[0]
    for i in args[1:]:
        res += i
    return res

print(mysum('abc', 'def'))
print(mysum([1,2,3], [4,5,6]))
print(mysum(1,2,3))

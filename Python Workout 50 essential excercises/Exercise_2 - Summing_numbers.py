def my_sum(*arg, start=0):
    """The function accepts any number of arguments (integers only) and returns their sum

     :param arg: integers or iterable prefixed with *
     :param start: start of summation, if not specified default is 0
     :returns sum of arguments
    """

    output = 0

    for i in arg:
        start += i
    output = start
    return output


def arm(*arg):
    """
    This function calculates the arithmetic median of the arguments passed
    :param arg:
    :return: arithmetic median
    """

    temp = 0

    for i in arg:
        temp += i
    return temp / len(arg)


def string_info(strngs):
    """
    Checks the length of strings in the list and returns a tuple of integers with the len() of longest and
    shortest words and the avg. len() of words

    :param strngs: a [] of str()
    :return: tuple of int()
    """

    output = tuple()
    word_len = {}

    # TODO: algo to find longest/shortest word
    avglen = sum([len(word) for word in strngs]) / len(strngs)

    pass


def sum_objects(obj_list):
    """


    :param obj_list: list of Python objects
    :return: int() and obj that can be turned to int()
    """

    pass
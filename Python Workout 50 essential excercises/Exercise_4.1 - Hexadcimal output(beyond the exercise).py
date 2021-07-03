def hex_output():

    """
    function return dec value of hex num using ord() and char() built in
    functuions

    :return: dec value in int()
    """

    decnum = 0
    hexnum = input("Enter your hex number: ")

    for pwr, digit in enumerate(hexnum[::-1]):
        # TODO use ord() and chr() to identify characters and ignore the ones
        # not legal for the number base


hex_output()

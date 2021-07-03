def hex_output():

    """
    Function to return decimal value of a hex number
    
    :return: deciaml value of argument
    """

    decnum = 0 
    hexnum = input("Choose a hex num: ")
    
    for pwr, digit in enumerate(hexnum[::-1]):
       decnum += int(digit, 16) * (16 ** pwr)

    return(decnum)


print(hex_output())

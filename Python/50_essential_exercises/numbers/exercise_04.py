######################
# Hexadecimal output #
######################

# You need to write a function hex_output() that takes a hex number and returns
# the decimal equivalent. Thats it, if the user enters 50, you'll assume that
# its a hex number (equal to 0x50) and will pritn the value 80 to the screen.
# And no, you should not convert the value at once using the int() function,
# although it's permissable using int() one digit at the time.

def from_hex_to_dec():

    num = input("Enter value you'd like to convert : ")

    for index, digit in enumerate(num[::-1]):
       dec  = int(digit, 16) * (16 ** index)

    return dec


print(from_hex_to_dec())

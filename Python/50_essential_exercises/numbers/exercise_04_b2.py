######################
# Hexadecimal output #
######################

# Write a program that asks the user for their name and then produces a "name
# triangle": the first letter o their name, then the first two letters, then
# the first three, and so forth, until the entire name is written on the final
# line.

def triangle():

    name = input("Enter your name :")

    for i in range(len(name)):
        print(name[:i+1])

triangle()

##############
# Run timing #
##############

# Explore the Decimal class, which has an alternative floating-point
# representation that's as accurate as any decimal number can be.
# Write a function that takes two strigs from the user, turns them into decimal
# instances, and then prints the floating point sum of the user's two inputs. In
# other words, make it possible for the user to enter 0.1 and 0.2, and for us to
# get 0.3 back.

import decimal 

def sum_decimals(a, b):

    num1 = decimal.Decimal(a)
    num2 = decimal.Decimal(b)

    return float(num1 + num2)

print(sum_decimals(0.2, 0.3))

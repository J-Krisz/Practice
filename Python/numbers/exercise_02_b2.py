###################
# Summing numbers #
###################

# Write a function that takes a list of numbers. It should return the average
# of those numbers.

def average(numbers):

    output = 0

    for n in numbers:
        output += n

    return output / len(numbers)


nums = [i for i in range(15)]

print(average(nums))

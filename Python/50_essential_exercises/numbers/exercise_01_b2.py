########################
# Number guessing game #
# Beyond the exercise  #
########################

# Not only shoul rou chose a random number, but you should also choose a random
# number base, from 2 to 16, inwhich the user should submit their input. If
# their inputs "10" as their guess, you'll need to interpret it in the correct
# number base; "10" might mean 10(decimal), or 2(binary) or 16(hexadecimal).

import random

def guessing_game():

    secret_number = random.randint(1, 30)
    base = random.choice([2, 8, 10, 16])

    number_of_attempts = 5

    while number_of_attempts <= 5:

        user_guess = int(input("I'm thinking of a number, can you guess it?: "),
                        base)

        if user_guess == secret_number:
            print(f"Yes! I was thinknig of {user_guess}")
            break

        if user_guess < secret_number:
            print(f"I'm afraid {user_guess} is too low, try higher")
        else:
            print(f"I'm afraid {user_guess} is too high, try lower")

        number_of_attempts += 1

    else:
        print("Unfortunately you are out of attempts, try again next time")
        break

guessing_game()

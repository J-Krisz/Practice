########################
# Number guessing game #
########################

# write a function guessing_game() that takes no arguments
# when run function chooses random int() between 0 and 30
# than ask the user to guess the number that has been chosen
# each time a guess has been made the program should indicate one of the
# following

    # too high
    # too low
    # just right

# if the user guesses correctly, the program exits. Otherwise, the user is asked
# to try again.
# The program only exits if the user guesses correctly.


import random 

def guessing_game():
    
    secret_number = random.randint(1, 30)

    while True:
        user_guess = int(input("Guess the number I'm thinking of : "))

        if user_guess == secret_number:
            print(f"Right!! I was thinking of {secret_number}")
            break

        if user_guess > secret_number:
            print("Too high, try lower")
        else:
            print("Too low, try higher")


guessing_game()

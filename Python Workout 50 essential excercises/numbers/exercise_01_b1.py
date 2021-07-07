########################
# Number guessing game #
# Beyond the exercise  #
########################

# Modify the previous program, such that it gives the user only three chances to
# guess the correct number. If they try three times without success, the program
# tells them that they didn't guess in time and than exits.

import random 

def guessing_game():
    
    secret_number = random.randint(1, 30)
    number_of_attempts = 0 

    while number_of_attempts < 3:

        number_of_attempts += 1
        user_guess = int(input("Guess the number I'm thinking of : "))
        
        if user_guess == secret_number:
            print(f"Right!! I was thinking of {secret_number}")
            break

        if user_guess > secret_number:
            print("Too high, try lower")
        else:
            print("Too low, try higher")
    else:
        print("Sorry, no more guesses for you")


guessing_game()

import sys
import random

def guessing_game(num):
    secret_number = random.randint(1, num)
    user_guess = 0
    attempts = 1

    while user_guess != secret_number:

        user_guess = input(f"I though of a number between 1 and {num}(inclusive). Can you guess it? : ")
        try:
            user_guess = int(user_guess)
        except ValueError:
            print(f"{user_guess} is not a number.")
            sys.exit()

        if user_guess == secret_number:
            print(f"Well done!! I was thinking of #{secret_number}. And it took you only {attempts} attempts.")
        elif user_guess > secret_number:
            print("That's too high, guess again")
        elif user_guess < secret_number:
            print("That's too low, guess again")

        attempts += 1

        if attempts == 3:
            print("You tried 3 times already, soz. Try again another time. Bye!")
            sys.exit()


guessing_game(10)
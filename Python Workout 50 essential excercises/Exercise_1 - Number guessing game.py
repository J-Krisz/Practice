import sys
import random

# TODO: choose not just a number but random number base as well(binary, octa;, decimal, hexadecimal)
# TODO: in which the user should submit their input

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

        if 1 <= user_guess <= num:
            if user_guess == secret_number:
                print(f"Well done!! I was thinking of #{secret_number}. And it took you only {attempts} attempts.")
            elif user_guess > secret_number:
                print("That's too high, guess again")
            elif user_guess < secret_number:
                print("That's too low, guess again")
        else:
            print(f" {user_guess}Is not within range")

        attempts += 1

        if attempts > 3:
            print(f"You tried {attempts} times already, soz. Try again another time. Bye!")
            sys.exit()
try:
    guessing_game(10)
except KeyboardInterrupt:
    print("Thanks, bye")

# TODO: Try the same thing but have the program choose a random word  from the dictionary and than ask the user to
# TODO: to guess the word. Try and limit the len() of the word to 3-5 letters.
# TODO: insted of instructing the user to guess higher or lower number have them choose an earlier  or later word from the dictionary
import random

def guessing_game(number):
    secret_number = random.randint(1, number)
    user_guess = 0
    attempts = 0

    while user_guess != secret_number:

        user_guess = int(input(f"I though of a number between 1 and {number}(inclusive). Can you guess it? : "))

        if user_guess == secret_number:
            print(f"Well done!! I was thinking of #{secret_number}")
        elif user_guess > secret_number:
            print("That's too high, guess again")
        elif user_guess < secret_number:
            print("That's too low, guess again")

        attempts += 1

        if attempts == 3:
            print("You tried 3 times already, soz. Try again another time. Bye!")


guessing_game(10)
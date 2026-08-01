print("Welcome to the Number Guessing Game!")
import random

number = random.randint(1, 100)
guess = None
attempts = 0

while guess != number:
    guess = int(input("Guess a number between 1 and 100: "))
    attempts += 1

    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print(f"Congratulations! You guessed the number in {attempts} attempts.")



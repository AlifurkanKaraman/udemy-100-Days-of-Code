#Number Guessing Game Objectives:

from art import logo
from replit import clear
import random

EASY_LEVEL_MODE = 10
HARD_LEVEL_MODE = 5

def attempts(game_mode):
    if game_mode == "hard":
        return HARD_LEVEL_MODE
    elif game_mode == "easy":
        return EASY_LEVEL_MODE

def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    mode = input("Choose a difficulty. Type 'easy' or 'hard': ")
    user_attempts = attempts(mode)
    answer = random.randint(1, 100)

    while user_attempts != 0:
        print(f"You have {user_attempts} attempts remaining to guess the number.")
        guess_number = int(input("Make a guess: "))

        if guess_number == answer:
            print(f"You got it! The answer was {guess_number}.")
            break
        elif guess_number > answer:
            print("Too high.")
            print("Guess again")
            user_attempts -= 1
        else:
            print("Too low.")
            print("Guess again")
            user_attempts -= 1

        if user_attempts == 0:
            print("You've run out of guesses, you lose.")
    
while input("Do you want to play? 'y' for yes or 'n' for no: ") == 'y':
    clear()
    game()





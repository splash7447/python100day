# Number Guessing Game Objectives:

# Include an ASCII art logo.
from random import randint
from art import logo

# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def check_answer(guess, answer, turns):
    # Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it!The answer was {answer}.")


def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    # Allow the player to submit a guess for a number between 1 and 100.
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    # If they got the answer correct, show the actual answer to the player.
    print(f"Pssst, the correct answer is {answer}")

    turns = set_difficulty()
    guess = 0
    while guess != answer:
        # Track the number of turns remaining.
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        # If they run out of turns, provide feedback to the player.
        if turns == 0:
            print("You're run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")

game()






#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random

logo = """
  ________                              ___________.__              _______               ___.                 
 /  _____/ __ __   ____   ______ ______ \__    ___/|  |__   ____    \      \  __ __  _____\_ |__   ___________ 
/   \  ___|  |  \_/ __ \ /  ___//  ___/   |    |   |  |  \_/ __ \   /   |   \|  |  \/     \| __ \_/ __ \_  __ \
\    \_\  \  |  /\  ___/ \___ \ \___ \    |    |   |   Y  \  ___/  /    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/
 \______  /____/  \___  >____  >____  >   |____|   |___|  /\___  > \____|__  /____/|__|_|  /___  /\___  >__|   
        \/            \/     \/     \/                  \/     \/          \/            \/    \/     \/      
"""

print(logo)

EASY_MODE = 10
HARD_MODE = 5
game_life = 0

def check_answer(guess, answer):
  if guess > answer:
    global game_life
    print("Too high")
    game_life -= 1
  elif guess < answer:
    print("Too low")
    game_life -= 1
  else:
    print("Congration, You got the answer.")

def set_diffculty():
  game_level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if game_level == "easy":
    global game_life
    game_life = EASY_MODE
  else:
    game_life = HARD_MODE

def game():
  print("Welcome to the Nubmer Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  answer = random.choice(range(1, 101))
  set_diffculty()
  guess = 0
  while guess != answer and game_life != 0:
    print(f"You have {game_life} attempts remaining to guess the number.")
    guess = int(input("Please submit a guess for a number between 1 and 100: "))
    check_answer(guess, answer)
  else:
    print("You're run out of guesses, you lose.")

game()
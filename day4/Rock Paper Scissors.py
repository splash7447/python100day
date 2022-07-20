import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
game_images = [rock, paper, scissors]


user_chose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if user_chose >= 3 or user_chose < 0:
    print("You typed an invalid number, you lose!")
else:
    print(game_images[user_chose])
    compute_chose = random.randint(0, 2)
    print("Computer chose:")
    print(game_images[compute_chose])
    if compute_chose == 0 and user_chose == 2:
        print("You lose")
    elif compute_chose == 2 and user_chose == 0:
        print("You win!")
    elif compute_chose > user_chose:
        print("You lose")
    elif user_chose > compute_chose:
        print("You win!")
    elif compute_chose == user_chose:
        print("It's a draw")
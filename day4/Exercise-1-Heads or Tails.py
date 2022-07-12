#Write your code below this line 👇
#Hint: Remember to import the random module first. 🎲

import random

head_or_tails = random.randint(0, 1)

if head_or_tails == 1:
  print("Heads")
elif head_or_tails == 0:
  print("Tails")
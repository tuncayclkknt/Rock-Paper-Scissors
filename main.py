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

import random

user_choice = int(input("What do you choose? Type 0 for Rock, type 1 for Paper, type 2 for Scrissors: "))


if user_choice >= 3 or user_choice < 0: 
  print("You typed an invalid number, you lose!")
elif user_choice < 3 or user_choice >= 0:
  game_images = [rock, scissors, paper]

  print(game_images[user_choice])
    
  print("Computer chose:")

  secimler = random.randint(0, 2)
  
  print(game_images[secimler])
  
  
  if user_choice == 0 and secimler == 0:
    print("Draw.")
  elif user_choice == 0 and secimler == 1:
    print("You win.")
  elif user_choice == 0 and secimler == 2:
    print("You lose.")
  
  if user_choice == 1 and secimler == 0:
    print("You lose.")
  elif user_choice == 1 and secimler == 1:
    print("Draw.")
  elif user_choice == 1 and secimler == 2:
    print("You win.")
  
  if user_choice == 2 and secimler == 0:
    print("You win.")
  elif user_choice == 2 and secimler == 1:
    print("You lose.")
  elif user_choice == 2 and secimler == 2:
    print("Draw.") 


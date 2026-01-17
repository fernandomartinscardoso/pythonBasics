# 100 Days of Python
# Day 4 - Randomization and Python Lists
# Project of the day: Rock, Paper, Scissors Game

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

print("Let's play Rock, Paper, Scissors!")

choices = [rock, paper, scissors]
computer_choice = random.randint(0, 2)
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if computer_choice == player_choice:
    print(choices[player_choice])
    print("Computer chose:\n"+choices[computer_choice])
    print("It's a draw!")
elif computer_choice == 0:
    if player_choice == 1:
        print(choices[player_choice])
        print("Computer chose:\n" + choices[computer_choice])
        print("You win!")
    else:
        print(choices[player_choice])
        print("Computer chose:\n" + choices[computer_choice])
        print("You lose!")
elif computer_choice == 1:
    if player_choice == 0:
        print(choices[player_choice])
        print("Computer chose:\n" + choices[computer_choice])
        print("You lose!")
    else:
        print(choices[player_choice])
        print("Computer chose:\n" + choices[computer_choice])
        print("You win!")
else:
    if player_choice == 0:
        print(choices[player_choice])
        print("Computer chose:\n" + choices[computer_choice])
        print("You win!")
    else:
        print(choices[player_choice])
        print("Computer chose:\n" + choices[computer_choice])
        print("You lose!")

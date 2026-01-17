# 100 Days of Python
# Day 14 - Reviewing Functions and Algorithms in Python
# Project of the day: Higher or Lower Game

import random
import higher_or_lower_art as art
import game_data

# Defining profiles A and B:
profileA = random.choice(game_data.data)
profileB = random.choice(game_data.data)
while profileB == profileA:
    profileB = random.choice(game_data.data)

# Setting initial conditions
print(art.logo)
game_over = False
score = 0
player_choice = ""
while not game_over:
    print(f"Compare A: {profileA['name']}, {profileA['description']}, from {profileA['country']}\n"
          f"{art.vs}\n"
          f"Against B: {profileB['name']}, {profileB['description']}, from {profileB['country']}")
    player_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    if player_choice == "a" and profileA['follower_count'] > profileB['follower_count']:
        profileA = profileB
        while profileB == profileA:
            profileB = random.choice(game_data.data)
        score += 1
        print("\n"*20)
        print(art.logo)
        print(f"You're right! Current score: {score}")
    elif player_choice == "b" and profileA['follower_count'] > profileB['follower_count']:
        print("\n"*20)
        print(art.logo)
        print(f"Sorry, that's wrong. Final score: {score}")
        game_over = True
    elif player_choice == "b" and profileA['follower_count'] < profileB['follower_count']:
        profileA = profileB
        while profileB == profileA:
            profileB = random.choice(game_data.data)
        score += 1
        print("\n"*20)
        print(art.logo)
        print(f"You're right! Current score: {score}")
    elif player_choice == "a" and profileA['follower_count'] < profileB['follower_count']:
        print("\n"*20)
        print(art.logo)
        print(f"Sorry, that's wrong. Final score: {score}")
        game_over = True
    else:
        print("\n"*20)
        print(art.logo)
        print("Invalid option! Goodbye!")
        break

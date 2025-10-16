# 100 Days of Python
# Day 11 - Review of concepts and project
# Project of the day: The Blackjack Capstone
# Demo version: https://appbrewery.github.io/python-day11-demo/
# Emojis by: https://www.flaticon.com/authors/freepik and https://emojipedia.org/

import blackjack_art
import random
import math

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def current_score(cards):
    total_cards = math.fsum(cards)
    return total_cards

game_is_not_over = True

while game_is_not_over:
    play_game_choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if play_game_choice == 'n':
        print("OK! See you next time!")
        game_is_not_over = False
    elif play_game_choice == 'y':
        print(blackjack_art.logo)
        player_cards = []
        computer_cards = []

        for i in range(2):
            player_cards.append(random.choice(cards))
            if i == 1:
                computer_cards.append(random.choice(cards))

        computer_score = current_score(computer_cards)
        player_score = current_score(player_cards)
        while player_score <= 21:
            print(f"Your cards: {player_cards}, current score: {player_score}")
            print(f"Computer's first card: {computer_cards}")
            another_card_choice = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if another_card_choice == 'y':
                player_cards = player_cards.append(random.choice(cards))
                player_score = math.fsum(player_cards)
            else:
                break

    else:
        print("Option not valid! Goodbye!")
        break

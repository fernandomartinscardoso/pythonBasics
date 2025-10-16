# 100 Days of Python
# Day 11 - Review of concepts and project
# Project of the day: The Blackjack Capstone
# Demo version: https://appbrewery.github.io/python-day11-demo/
# Emojis by: https://www.flaticon.com/authors/freepik and https://emojipedia.org/

import blackjack_art
import random
import math

print(blackjack_art.logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

game_is_not_over = True

selected_cards = []
for i in range(2):
    selected_cards.append(random.choice(cards))

print(math.fsum(selected_cards))

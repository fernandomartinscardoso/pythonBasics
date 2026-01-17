# 100 Days of Python
# Day 3 - Control Flow and Logical Operators
# Project of the day: Treasure Island Game

print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

first_step = input("You find yourself at the island shore. There are two paths to follow. Which one do you take?\n"
                   "Type left or right\n")
if first_step == 'left':
    second_step = input("After a long walk, you noticed the island is crossed by the sea\n"
                        "You have the option to wait until the tide goes out or to swim to the other side\n"
                        "Type wait or swim\n")
    if second_step == 'wait':
        third_step = input("On the other side of the island, you see three doors:\n"
                           "One Blue, One Red, and One Yellow. Which one do you choose?\n"
                           "Type blue, red, or yellow\n")
        if third_step == 'yellow':
            print("Congratulations! You found the treasure and won the game!")
        elif third_step == 'blue':
            print("You were eaten by beasts. Game over!")
        elif third_step == 'red':
            print("You were burned by fire. Game over!")
        else:
            print("You chose poorly. Game over!")
    else:
        print("You were eaten by a trout.\nGame over!")
else:
    print("You fell into a hole.\nGame over!")

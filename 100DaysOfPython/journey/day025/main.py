# 100 Days of Python
# Day 25 - Introduction to Pandas
# First Project of the day: Counting Squirrels by Colors in Central Park

import pandas

# Read the squirrel data from the CSV file and convert the "Primary Fur Color" column to a list
squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
squirrel_color_list = squirrel_data["Primary Fur Color"].to_list()

# Initialize counters for each fur color
gray = 0
cinnamon = 0
black = 0
for color in squirrel_color_list:
    if color == "Black":
        black += 1
    elif color == "Gray":
        gray += 1
    elif color == "Cinnamon":
        cinnamon += 1

# Create a dictionary to hold the fur color counts
squirrel_color_dict = {
    "Fur Color": ["Black", "Cinnamon", "Gray"],
    "Count": [black, cinnamon, gray]
}

# Convert the dictionary to a DataFrame and save it as a new CSV file
data = pandas.DataFrame(squirrel_color_dict)
data.to_csv("squirrel_count.csv")

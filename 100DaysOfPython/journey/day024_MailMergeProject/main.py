# 100 Days of Python
# Day 24 - Files, directories and paths
# Second Project of the day: Mail Merge Project

#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./Input/Names/invited_names.txt") as file:  # ./Input/Names/invited_names.txt
    names_ = file.readlines()
    names = []
    for i in names_:
        x = i.strip("\n")
        names.append(x)

with open("./Input/Letters/starting_letter.txt") as letter:
    sample_letter = letter.read()
    for name in names:
        personal_letter = sample_letter.replace("[name]", name, 1)
        f = open(f"./Output/ReadyToSend/letter_for_{name}.docx", "w")
        f.write(personal_letter)
        f.close()
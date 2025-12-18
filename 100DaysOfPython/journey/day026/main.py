# 100 Days of Python
# Day 26 - List and Dictionary Comprehensions
# Project of the day: The NATO Phonetic Alphabet

import pandas

# Creating the phonetic alphabet dictionary using letter as keys and code as values.
data = pandas.read_csv("nato_phonetic_alphabet.csv")
data_letter = data.letter.to_list()
data_code = data.code.to_list()
phonetic_alpha_dict = {data_letter[i]: data_code[i] for i in range(len(data_letter))}

# Printing the phonetic code words from a word that the user inputs.
user_word = input("Enter the word: ").upper()
phonetic_list = [phonetic_alpha_dict[letter_key] for letter_key in user_word]
print(phonetic_list)

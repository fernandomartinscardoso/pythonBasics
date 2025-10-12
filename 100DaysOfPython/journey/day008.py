# 100 Days of Python
# Day 8 - Functions with Inputs 
# Project of the day: The Caesar Cipher

import caesar_art
print(caesar_art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    coding = True
    while coding:
        if encode_or_decode == "decode":
            shift_amount *= -1
        for letter in original_text:
            if letter not in alphabet:
                output_text += letter
            else:
                shifted_position = alphabet.index(letter) + shift_amount
                shifted_position %= len(alphabet)
                output_text += alphabet[shifted_position]
        print(f"Here is the {encode_or_decode}d result: {output_text}")
        loop = input("Would like to continue coding texts? Type y or n\n").lower()
        if loop == "n":
            print("Goodbye!")
            coding = False
        elif loop == "y":
            encode_or_decode = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
            original_text = input("Type your message:\n").lower()
            shift_amount = int(input("Type the shift number:\n"))
            output_text = ""
        else:
            print("Invalid option.")

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
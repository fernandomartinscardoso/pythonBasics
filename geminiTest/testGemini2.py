import tkinter as tk
import random
from playsound import playsound

def generate_random_number():
    random_number = random.randint(0, 1000)
    label.config(text=f"Random Number: {random_number}")
    playsound("meow.wav")  # Replace with the path to your chime sound file

# Create the main window
window = tk.Tk()
window.title("Random Number Generator")

# Create a label to display the random number
label = tk.Label(window, text="Random Number:")
label.pack()

# Create a button to generate the random number
button = tk.Button(window, text="Generate Random Number", command=generate_random_number)
button.pack()

# Start the event loop
window.mainloop()
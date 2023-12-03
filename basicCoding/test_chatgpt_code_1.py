import tkinter as tk
import random

# Define the function to generate and display the random number
def generate_random_number():
    # Generate a random number between 1 and 100
    random_number = random.randint(1, 100)
    # Display the random number in the display widget
    display.config(text=f"Random number: {random_number}")

# Create the main window
root = tk.Tk()
root.title("Random Number Generator")

# Create the button widget
button = tk.Button(root, text="Generate Random Number", command=generate_random_number)
button.pack(padx=20, pady=10)

# Create the display widget
display = tk.Label(root, text="Press the button to generate a random number")
display.pack(padx=20, pady=10)

# Start the main event loop
root.mainloop()

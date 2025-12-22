# 100 Days of Python
# Day 27 - GUI with Tkinter and Function Arguments 
# Project of the day: Mile to Kilometers Converter Project

from tkinter import *

# Function to convert miles to km
def calculate():
    miles = float(miles_entry.get())
    km = miles*1.60934
    result_label.config(text=f"{km:.1f}")

# Windows config
window = Tk()
window.title("Mile to km Converter")
window.minsize(width=350, height=180)
window.config(padx=50, pady=50)

# Labels
miles_label = Label(text="Miles", font=("Arial", 12, "bold"))
miles_label.grid(column=2, row=0)

equal_label = Label(text="is equal to", font=("Arial", 12, "bold"))
equal_label.grid(column=0, row=1)

km_label = Label(text="km", font=("Arial", 12, "bold"))
km_label.grid(column=2, row=1)

result_label = Label(text="0", font=("Arial", 12, "bold"))
result_label.grid(column=1, row=1)

# Button
calculate_button = Button(text="Calculate", command=calculate)
calculate_button.grid(column=1, row=2)

# Entry
miles_entry = Entry(width=6)
miles_entry.grid(column=1, row=0)

window.mainloop()

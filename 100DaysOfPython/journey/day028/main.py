# 100 Days of Python
# Day 28 - GUI with Tkinter and Dynamic Typing
# Project of the day: Pomodoro Timer

from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
MIN_SEC = 60
reps = 0
tick_text = ""
timer = None

# ------------------------------ TIMER RESET --------------------------------- # 
def reset():
    global reps, tick_text
    window.after_cancel(timer)
    timer_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    reps = 0
    tick_text = ""
    tick_label.config(text=tick_text)

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start():
    global reps
    reps += 1

    work_sec = WORK_MIN * MIN_SEC
    short_break_sec = SHORT_BREAK_MIN * MIN_SEC
    long_break_sec = LONG_BREAK_MIN * MIN_SEC

    if reps % 2 == 1:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)
    elif reps % 2 == 0 and reps < 8:
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=PINK)
    else:
        count_down(long_break_sec)
        timer_label.config(text="Break", fg=RED)
        reps = 0

# -------------------------- COUNTDOWN MECHANISM ----------------------------- # 
def count_down(count):
    global tick_text
    count_min = count // MIN_SEC
    count_sec = count % MIN_SEC
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start()
        if reps % 2 == 0:
            tick_text += "✅"
        else:
            tick_text = tick_text
        tick_label.config(text = tick_text)

# ------------------------------- UI SETUP ----------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=80, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

# Labels
timer_label = Label(text="Timer", font=(FONT_NAME, 40, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

tick_label = Label(text="", fg=GREEN, font=(FONT_NAME, 30, "bold"), bg=YELLOW)
tick_label.grid(column=1, row=3)

# Buttons
start_button = Button(text="Start", command=start)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset)
reset_button.grid(column=2, row=2)

window.mainloop()

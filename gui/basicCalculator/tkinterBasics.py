from tkinter import *

# Window configuration
window = Tk()
window.geometry("350x500")
window.title("Calculator")
window.configure(bg="#499e3e")  # Choosing color of background. Tip: use color picker on Google
window.iconbitmap("calculator_icon.ico") # Changes the icon of the app, but the icon has to be in the same folder of the app

# Creating buttons and entries
buttont = Button(window,width=5,height=5,text="0000",relief="ridge",bg="#69cc5c",font=("new times roman",12))
buttont.pack() # pady=20 increases distance between button and next element; fill=X or Y makes the button with axis width
# # Instead of using pack function, which centralizes the button, it can be used the function place:
# buttont.place(x=175,y=250)

equation = StringVar()
entry0 = Entry(window,textvariable=equation,justify="right")
entry0.pack()

# To use grid, first you need to create a frame
button_frame = Frame(window)
button_frame.pack()

button0 = Button(button_frame,text="0",relief="ridge")
button1 = Button(button_frame,text="1",relief="ridge")
button2 = Button(button_frame,text="2",relief="ridge")
button3 = Button(button_frame,text="3",relief="ridge")
button4 = Button(button_frame,text="4",relief="ridge")
button5 = Button(button_frame,text="5",relief="ridge")
button6 = Button(button_frame,text="6",relief="ridge")
button7 = Button(button_frame,text="7",relief="ridge")
button8 = Button(button_frame,text="8",relief="ridge")
button9 = Button(button_frame,text="9",relief="ridge")

button0.grid(row=0,column=0,columnspan=3,sticky="nsew")
button1.grid(row=1,column=0)
button2.grid(row=1,column=1)
button3.grid(row=1,column=2)
button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)
button7.grid(row=3,column=0)
button8.grid(row=3,column=1)
button9.grid(row=3,column=2)


window.mainloop()

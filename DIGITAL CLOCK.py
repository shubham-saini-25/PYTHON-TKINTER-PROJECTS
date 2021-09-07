# Digital Clock using Python

from tkinter import *
import time

root = Tk()
root.title("Digital Clock")
root.geometry("500x125")
root.resizable(0, 0)

def digital_clock():
    current_time = time.strftime("%I:%M:%S %p")
    
    label.config(text = current_time )
    
    label.after(100, digital_clock)


label = Label(root, font = ("Arial 60 bold"), bg = "black", fg = "green2", bd = 20)
label.pack()

digital_clock()
root.mainloop()

# Follow :- @python_with_shubham
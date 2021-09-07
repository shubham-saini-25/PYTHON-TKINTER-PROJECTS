# Random Password Generator

from tkinter import *
import random

root = Tk()
root.title("Random Password Generator")
root.geometry("700x400+200+30")
root.config(bg = "powderblue")

Label(root, text = "Password Generator", font = ("None 45 bold underline"), bg = "powderblue", fg = "darkblue").place(x = 60, y = 10)

Label(root, text = "Enter the Password Length: ", font = ("None 30 bold"), bg = "powderblue").place(x = 50, y = 100)

pass_length = IntVar()
pass_length.set("")
Entry(root, textvariable = pass_length, font = ("None 30 bold"), bg = "lightgreen", width = 3).place(x = 590, y = 100)

def pswrd():
    pass1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    pass2 = "abcdefghijklmnopqrstuvwxyz"
    pass3 = "!@#$%^&*()?><|?/"
    pass4 = "1234567890"
    Total_pass = pass1 + pass2 + pass3 + pass4
    password = ""
    for i in range(pass_length.get()):
        password = password + random.choice(Total_pass)
    show_password.set(password)
    
def clear():
    pass_length.set("")
    show_password.set("")
    
Button(root, text = "Password", command = pswrd, font = ("None 25 bold"),
        bg = "lime", activebackground = "lime", bd = 5).place(x = 140, y = 290)

Button(root, text = "Clear All", command = clear, font = ("None 25 bold"),
        bg = "coral", activebackground = "coral", bd = 5).place(x = 400, y = 290)

show_password = StringVar()
Entry(root, textvariable = show_password, font = ("None 30 bold"), bg = "lightgreen", width = 25).place(x = 80, y = 200) 

root.mainloop()
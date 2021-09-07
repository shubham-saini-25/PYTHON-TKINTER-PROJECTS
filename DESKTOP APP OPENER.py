# Gui Desktop App Opener using Python

from tkinter import *
import subprocess

root = Tk()
root.title("Desktop App Opener")
root.geometry("330x170")

def openApp():
    app = App_Name.get()
    subprocess.call(f"C:/Windows/System32/{app}.exe")
 
App_Name = StringVar()
Entry(root, textvariable = App_Name, font = ("Consolas 20 bold"), bd = 5).place(x = 10, y = 5)

Button(root, text = "Open App", font = ("Consolas 20 bold"), bd = 5, command = openApp).place(x = 80, y = 70)

root.mainloop()
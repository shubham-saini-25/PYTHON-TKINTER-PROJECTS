# GUI TEMPERATURE CHECKER

from tkinter import *
import requests
from bs4 import BeautifulSoup

root = Tk()
root.geometry("870x400+100+50")
root.title("City Temperature Checker")
root.config(bg = "lightgreen")

# Function Define for Calculating the Temperature
def temp():
    
    search = City.get()
    
    url = f"https://www.google.com/search?&q=weather+in+{search}"
    
    r = requests.get(url)
    
    s = BeautifulSoup(r.text, "html.parser")
    
    weather = s.find("div", class_="BNeawe").text
    
    Temp.set(weather)

# Create a Function to Clear All Entry
def clear():
    City.set("")
    Temp.set("0°C")
        
# Display a Label
Label(root, text = "Weather Temperature Checker ", font = ("None 35 bold underline"), bg = "lightgreen").place(x = 120, y = 5)

# Display a Label and create a Entry
Label(root, text = "Enter a City Name:", font = ("None 30 bold"), bg = "lightgreen", fg = "green").place(x = 70, y = 100)
City = StringVar()   
Entry(root, textvariable = City, font = ("None 25 bold"), width = 15, bg = "khaki1").place(x = 470, y = 105)

# Display a Label and create a Entry to Display Temperature
Label(root, text = "Current Temperature in your City is:", font = ("None 30 bold"), bg = "lightgreen", fg = "blue4").place(x = 30, y = 180)
Temp = StringVar()
Temp.set("0°C")
Entry(root, textvariable = Temp, font = ("None 25 bold"), width = 5, bg = "khaki1").place(x = 730, y = 185)

# Create a Buttton
Button(root, text = "Check Temperature", command = temp, font = ("None 25 bold"), bg = "yellow", activebackground = "green1").place(x = 150, y = 280)

Button(root, text = "Clear", command = clear, font = ("None 25 bold"), bg = "coral", activebackground = "coral3").place(x = 580, y = 280)

root.mainloop()
# GUI AGE CALCULATOR USING PYTHON

from tkinter import *
from datetime import datetime

root = Tk()
root.geometry("780x550+50+50")
root.title("Age Calculator")
root.config(bg="khaki")

# Define for Calculating the Age
def cal():
    date = datetime.now()
    current_year = int(date.year)
    current_month = int(date.month)
    current_day = int(date.day)

    age_year = int(current_year - birth_year.get())
    
    age_month = int(current_month - birth_month.get())
    
    if age_month < 0:
        age_year = age_year - 1
        age_month = 12 - (birth_month.get() - current_month)
        
    age_day = int(current_day - birth_day.get())
    
    if age_day < 0:
        age_month = age_month - 1
        age_day = 31 - (birth_day.get() - current_day)
    
    Age.set(f"{str(age_year)} Years, {str(age_month)} Months, {str(age_day)} Days")

# Display a Label
Label(root, text = "AGE CALCULATOR", font = ("None 35 bold underline"), bg = "khaki").place(x = 150, y = 5)

# Display a Label and create a Entry for Birth Year
Label(root, text = "Enter Your Birth Year:", font = ("None 30 bold"), bg = "khaki", fg = "maroon3").place(x = 70, y = 100)
birth_year = IntVar()
birth_year.set("")
Entry(root, textvariable = birth_year, font = ("None 25 bold"), width = 7, bg = "skyblue").place(x = 510, y = 105)

# Display a Label and create a Entry for Birth Month
Label(root, text = "Enter Your Birth Month:", font = ("None 30 bold"), bg = "khaki", fg = "maroon3").place(x = 40, y = 180)
birth_month = IntVar()
birth_month.set("")
Entry(root, textvariable = birth_month, font = ("None 25 bold"), width = 7, bg = "skyblue").place(x = 510, y = 185)

# Display a Label and create a Entry for Birth Day
Label(root, text = "Enter Your Birth Day:", font = ("None 30 bold"), bg = "khaki", fg = "maroon3").place(x = 80, y = 260)
birth_day = IntVar()
birth_day.set("")
Entry(root, textvariable = birth_day, font = ("None 25 bold"), width = 7, bg = "skyblue").place(x = 510, y = 265)

# Display a Label and create a Entry to Calculate Age
Label(root, text = "Your Age is:", font = ("None 30 bold"), bg = "khaki", fg = "slateblue4").place(x = 30, y = 350)
Age = StringVar()
Age.set("")
Entry(root, textvariable = Age, font = ("None 25 bold"), width = 27, bg = "skyblue").place(x = 280, y = 355)

# Create a Buttton
Button(root, text = "Calculate Age", command = cal, font = ("None 25 bold"), bg = "yellow").place(x = 260, y = 440)

root.mainloop()
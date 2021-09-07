# GUI CALENDAR USING PYTHON TKINTER

from tkinter import *
from tkcalendar import Calendar

root = Tk()
# Download icons in '.ico' format from https://iconarchive.com/"
root.title("GUI CALENDAR")
root.geometry("600x400+300+30")
root.config(bg = "olivedrab2")

def valid(char):
   if char.isdigit():
      return True
   else:
      return False

def btn():
   root1 = Tk()
   root1.title("GUI CALENDAR")
   root1.geometry("980x660+200+10")
   root1.config(bg = "darkblue")
    
   dd = int(day.get())
   mm = int(month.get())
   yy = int(year.get())
    
   Calendar(root1, font = ("None 40 bold"), year = yy, month = mm, day = dd, background = "cadetblue2", foreground = "midnightblue",
            headersbackground = "lightpink", normalbackground = "khaki", normalforeground = "red2").place(x = 32, y = 10)
    
   Label(root1, text = "↑\nWeeks", font = ("None 25 bold"), bg = "darkblue", fg = "cadetblue2").place(x = 15, y = 572)
    
   Button(root1, text = "Close Calendar", font = ("none 25 bold"), command = exit ,bg = "coral1", fg = "black", 
            activebackground = "coral2", bd = 5).place(x = 330, y = 580)


Label(root, text = "GUI CALENDAR", font = ("Times New Roman", 50, "bold", "underline"), bg = "olivedrab2", fg = "black").place(x = 40)

Label(root, text = "Enter Date:", font = ("None 25 bold"), bg = "olivedrab2", fg = "black").place(x = 90, y = 100)

Label(root, text = "Enter Month:", font = ("None 25 bold"), bg = "olivedrab2", fg = "black").place(x = 90, y = 160)

Label(root, text = "Enter Year:", font = ("None 25 bold"), bg = "olivedrab2", fg = "black").place(x = 90, y = 220)

reg = (root.register(valid), '%P')

day = Entry(root, font = ("None 25 bold"), validate = "key", validatecommand = reg, bg = "olivedrab3", width = "10")
day.place(x = 320, y = 100)

month = Entry(root, font = ("None 25 bold"), validate = "key", validatecommand = reg, bg = "olivedrab3", width = "10")
month.place(x = 320, y = 160)

year = Entry(root, font = ("None 25 bold"), validate = "key", validatecommand = reg, bg = "olivedrab3", width = "10")
year.place(x = 320, y = 220)

Button(root, text = "Show Calendar", font = ("none 25 bold"), command = btn ,bg = "springgreen2", 
       fg = "black",activebackground = "springgreen3", bd = 5).place(x = 175, y = 300)

root.mainloop()

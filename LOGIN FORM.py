# Student Login Form using Python GUI

from tkinter import *
from tkinter import ttk
from tkinter import messagebox as msg

root = Tk()
root.title("STUDENT LOGIN FORM")
root.iconbitmap("D:/PYTHON MODULES/TKINTER/TKINTER PROJECTS/ICONs/Student.ico")
root.option_add("*TCombobox*Listbox*font","None 18 bold")
root.geometry("200x150+100+100")

def valid(char):
    if char.isdigit():
        return True
    elif char is str:
        return True
    else:
        return False
    
def submit():
    msg.showinfo("Congratulation", "Login Successfully!")
    
def reset():
    name.set("")
    date.set("1")
    month.set("January")
    year.set("2021")
    boy.set(b.deselect())
    girl.set(g.deselect())
    course.set("Select Course")
    branch.set("Select Branch")
    phone.set("")
    email.set("")
    password.set("")
    
def select(event):
    if course.get() == "B.Tech.":
        branch.config(value = Btech)
        branch.set("Select Branch")
    elif course.get() == "B.Sc.":
        branch.config(value = Bsc)
        branch.set("Select Branch")
    elif course.get() == "B.Com.":
        branch.config(value = Bcom)
        branch.set("Select Branch")
    elif course.get() == "B.A.":
        branch.config(value = Ba)
        branch.set("Select Branch")
    elif course.get() == "M.Tech.":
        branch.config(value = Mtech)
        branch.set("Select Branch")
    elif course.get() == "M.Sc.":
        branch.config(value = Msc)
        branch.set("Select Branch")
    elif course.get() == "M.Com.":
        branch.config(value = Mcom)
        branch.set("Select Branch")
    elif course.get() == "M.A.":
        branch.config(value = Ma)
        branch.set("Select Branch")

PanedWindow(root, width = 620, height = 600, bg = "tan2", relief = GROOVE, bd = 10).place(x = 400, y = 30)

# Labels
Label(root, text = "STUDENT LOGIN FORM", font = ("None 32 bold underline"), bg = "tan2").place(x = 470, y = 50)
Label(root, text = "Name:",     font = ("lucida 25 bold"), bg = "tan2").place(x = 430, y = 130)
Label(root, text = "DOB:",      font = ("lucida 25 bold"), bg = "tan2").place(x = 430, y = 180)
Label(root, text = "Course:",   font = ("lucida 25 bold"), bg = "tan2").place(x = 430, y = 230)
Label(root, text = "Branch:",   font = ("lucida 25 bold"), bg = "tan2").place(x = 430, y = 280)
Label(root, text = "Gender:",   font = ("lucida 25 bold"), bg = "tan2").place(x = 430, y = 330)
Label(root, text = "Phone:",    font = ("lucida 25 bold"), bg = "tan2").place(x = 430, y = 380)
Label(root, text = "Email:",    font = ("lucida 25 bold"), bg = "tan2").place(x = 430, y = 430)
Label(root, text = "Password:", font = ("lucida 25 bold"), bg = "tan2").place(x = 430, y = 480)

# Entry
name = StringVar()
Entry(root, textvariable = name, font = ("lucida 22 bold"), bd = 2).place(x = 620, y = 135, width = 360)

DD = [i for i in range(1,32)]
date = StringVar() 
date.set("1")
show = OptionMenu(root, date , *DD) 
show.config(font = ("lucida 22 bold"))
root.nametowidget(show.menuname).config(font = ("None 18 bold"), bg = "lightgray")
show.place(x = 620, y = 185, width = 65, height = 40)

MM = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
month = StringVar() 
month.set("January")
show = OptionMenu(root, month, *MM) 
show.config(font = ("lucida 22 bold"))
root.nametowidget(show.menuname).config(font = ("None 18 bold"), bg = "lightgray")
show.place(x = 690, y = 185, width = 185, height = 40)

YY = [i for i in range(1991, 2022)]
year = StringVar() 
year.set("2021")
show = OptionMenu(root, year , *YY) 
show.config(font = ("lucida 22 bold"))
root.nametowidget(show.menuname).config(font = ("None 18 bold"), bg = "lightgray")
show.place(x = 880, y = 185, width = 100, height = 40)

std = ["B.Tech.", "B.Sc.", "B.Com.", "B.A.", "M.Tech.", "M.Sc.", "M.Com.", "M.A."]
course = ttk.Combobox(root, value = std, font = ("lucida 22 bold"), state = "readonly")
course.set("Select Course")
course.place(x = 620, y = 235, width = 250, height = 40)
course.bind("<<ComboboxSelected>>", select)

Btech = Mtech = ["Computer Science", "Information Technology", "Electronic & Communications", "Biotechnology","Electrical", "Mechanical"]
Bsc = Msc = ["Computer Science", "Mathematics", "Biology", "Statics"]
Bcom = Mcom = ["Accounts & Finance", "Banking & Insurance", "Marketing", "Economics"]
Ba = Ma = ["Political Science", "English", "History", "Psychology", "Philosophy", "Economics", "Sociology", "Geography"]

branch = ttk.Combobox(root, value = [" "], font = ("lucida 22 bold"), state = "readonly")
branch.set("Select Branch")
branch.place(x = 620, y = 285, width = 300)

boy = IntVar()
b = Checkbutton(root, text = "Male", var = boy, font = ("lucida 22 bold"), bg = "tan2", activebackground = "tan2" )
b.place(x = 650, y = 335)

girl = IntVar()
g = Checkbutton(root, text = "Female", var = girl, font = ("lucida 22 bold"), bg = "tan2", activebackground = "tan2")
g.place(x = 800, y = 335)

code = IntVar()
Entry(root, text = code, font = ("lucida 22 bold"), state = "readonly", bd = 2).place(x = 620, y = 385, width = 55)
code.set("+91")

phone = StringVar()
reg = root.register(valid)
Entry(root, textvariable = phone, validate = "key", validatecommand = (reg, '%S'),
      font = ("lucida 22 bold"), bd = 2).place(x = 680, y = 385, width = 300)

email = StringVar()
Entry(root, textvariable = email, font = ("lucida 22 bold"), bd = 2).place(x = 620, y = 435, width = 360)

password = StringVar()
Entry(root, textvariable = password, font = ("lucida 22 bold"), bd = 2, show = "*").place(x = 620, y = 485, width = 360)

# Button
Button(root, text = "Reset", font = ("lucida 22 bold"), command = reset, bg = "yellow3",
       activebackground = "darksalmon", bd =5).place(x = 470, y = 545)

Button(root, text = "Cancel", font = ("lucida 22 bold"), command = quit, bg = "indianred1",
       activebackground = "darksalmon", bd = 5).place(x = 640, y = 545)

Button(root, text = "Submit", font = ("lucida 22 bold"), command = submit, bg = "lawngreen",
       activebackground = "chartreuse3", bd = 5).place(x = 820, y = 545)

root.mainloop()
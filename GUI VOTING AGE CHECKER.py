# Candidate Age Checker for Voting
# Follow @python_with_shubham 

from tkinter import *
from tkinter import messagebox as msg

root = Tk()
root.geometry("620x380+380+150")
root.title("Voting Age Checker")
root.config(bg="yellow")

# create a function for checking Candidate Age
def check():
    name = Name.get()
    age = Age.get()
    if age > 18:
        msg.showinfo("valid for Voting", f"{name}, You can Cast the Vote because your Age({age}) is above 18.")
    elif age < 18:
        msg.showwarning("Not valid for Voting", f"{name}, You can not Cast the Vote because your Age{age} is below 18.")

Label(root, text="Candidate Age Checker for Voting", font=("None 25 bold underline"), bg="yellow").place(x=50, y=20)

# Label for Name
Label(root, text="Enter Name:", font=("None 20 bold"), bg="yellow").place(x=70, y=100)

# Entry for Name
Name = StringVar()
Entry(root, textvariable=Name, font=("None 20 bold"), bg="lightpink").place(x=250, y=100)

# Label for Age
Label(root, text="Enter Age:", font=("None 20 bold"), bg="yellow").place(x=80, y=180)

# Entry for Age
Age = IntVar()
Age.set("")
Entry(root, textvariable=Age, font=("None 20 bold"), bg="lightpink").place(x=250, y=180)

Button(root, text="Check", command=check, font=("None 20 bold"), bd=4, bg="springgreen3").place(x=270, y=260)

root.mainloop()

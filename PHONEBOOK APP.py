# phonebook App using Python

from tkinter import *
from tkinter import messagebox

root = Tk()
root.iconbitmap("D:/PYTHON MODULES/TKINTER/TKINTER PROJECTS/ICONs/Phonebook.ico")
root.geometry("1350x680+10+10")
root.title("Phonebook App")
root.config(bg = "lightblue")

# Create a function to Add the Contact
def add_contact():
    
    # Check Name and Phone Entry Should Not be Empty otherwise it Shows an Error Message
    if f_name.get() != "" and l_name.get() != "" and phone.get() != "":
        
        # Insert the Item into the Listbox
        List.insert(1, f" {f_name.get()} {l_name.get()}  -  {phone.get()}")
        
        # It Clear the EntryBox of First Name, Last Name and Phone Number after Adding Contact
        f_name.set("")
        l_name.set("")
        phone.set("")
        
    else: 
        # It Shows the Error Message
        messagebox.showerror("Contacts", "Please Complete Your Details.") 

# Create a function to Delete the Contact
def del_task():
    for i in List.curselection():
        List.delete(i)

# Create a Label
Label(root, text = "PHONEBOOK APP", font = ("None 40 bold underline"), bg = "lightblue").place(x = 320, y = 0)

# Create a Frame
Frame(root, width = 600, height = 550, bg = "lightpink", bd = 8, relief = GROOVE).place(x = 100, y = 100)

# Create a Label and Entry for First Name
Label(root, text = "First Name :", font = ("None 25 bold"), bg = "lightpink").place(x = 150, y = 130)
f_name = StringVar()
Entry(root, textvariable = f_name, font = ("None 25 bold"), bg = "burlywood1", bd = 3, width = 17).place(x = 360, y = 130)

# Create a Label and Entry for Last Name
Label(root, text = "Last Name :", font = ("None 25 bold"), bg = "lightpink").place(x = 150, y = 200)
l_name = StringVar() 
Entry(root, textvariable = l_name, font = ("None 25 bold"), bg = "burlywood1", bd = 3, width = 17).place(x = 360, y = 200)

# Create a Label and Entry for Phone Number
Label(root, text = "Phone No. :", font = ("None 25 bold"), bg = "lightpink").place(x = 150, y = 270)
phone = StringVar()
Entry(root, textvariable = phone, font = ("None 25 bold"), bg = "burlywood1", bd = 3, width = 17).place(x = 360, y = 270)

# Create a Button for Add Contact
Button(root, text = " Add Contact  ", command = add_contact, font = ("None 20 bold"), bg = "lime", activebackground = "green3", bd = 5).place(x = 170, y = 380)

# Create a Button for Delete Contact
Button(root, text = "Delete Contact", command = del_task, font = ("None 20 bold"), bg = "orangered", activebackground = "brown1", bd = 5).place(x = 420, y = 380)

# Create a Button for Exit from the App
Button(root, text = "Exit", command = quit, font = ("None 20 bold"), bg = "darkgoldenrod1", activebackground = "goldenrod2", bd = 5, width = 12).place(x = 290, y = 500)

# Create a Listbox and Add Contact Name Label and Phone No Label on the Top of Listbox
Label(root, text = "Contact Name", font = ("None 25 bold underline"), bg = "lightblue").place(x = 780, y = 90)
Label(root, text = "Phone No", font = ("None 25 bold underline"), bg = "lightblue").place(x = 1055, y = 90)
List = Listbox(root, font = ("None 25 bold"), bg = "khaki1", bd = 5, relief = GROOVE, selectmode = SINGLE)
List.place(x = 750, y = 150, width = 550, height = 500)

# Create a Scrollbar
scrollbar = Scrollbar(root)
scrollbar.place(x = 1276, y = 154, height = 490, width = 25)

# Join the Scrollbar to the Listbox
List.config(yscrollcommand = scrollbar.set)
scrollbar.config(command = List.yview)

# close the root Window
root.mainloop()
from tkinter import *
from tkinter import messagebox as msg
    
root = Tk()
# Download icons in '.ico' format from "https://iconarchive.com/"
root.iconbitmap("D:/PYTHON MODULES/TKINTER/TKINTER PROJECTS/ICONs/To-Do List.ico")
root.geometry('460x500+450+80')
root.title("TO-DO LIST APP")
root.config(bg='#437481')
root.resizable(0, 0)

def add_task():
    add = my_task.get()
    if add != "":
        lbox.insert(END, add)
        my_task.set("")
        msg.showinfo("Saved", "Your Task Added Successfully.")
    else:
        msg.showwarning("Warning", "Please Enter a Task.")

def del_one():
    for i in lbox.curselection():
        lbox.delete(i)
        msg.showinfo("Deleted", "Your Selected Task Delete Successfully.")

def del_all():
    lbox.delete(0, END)
    msg.showinfo("Deleted", "Your All Task Delete Successfully.")

frame = Frame(root)
frame.place(x = 65, y = 20)

lbox = Listbox(frame, width=27, height=8, font=("Times 18 bold"), bg = "khaki", selectbackground='#a6a436', relief=GROOVE)
lbox.pack(side=LEFT, fill=BOTH)
                
sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)
lbox.config(yscrollcommand=sb.set)
sb.config(command=lbox.yview)

Label(root, text="Enter Task:", font=("None 17 bold"), bg='#437481').place(x = 5, y = 282)

my_task = StringVar()
Entry(root, textvariable=my_task, font=("None 20 bold")).place(x = 140, y = 280)

Button(root, text='Add Task', font=('Times 18 bold'), bg='#c5f776', command=add_task).place(x = 90, y = 350)

Button(root, text='Delete Task', font=('Times 18 bold'), bg='#ff8b61', command=del_one).place(x = 235, y = 350)

Button(root, text='Delete All', font=('Times 18 bold'), bg='#a84587', command=del_all).place(x = 87, y = 430)

Button(root, text='Exit', font=('Times 18 bold'), bg='#848732', command=exit).place(x = 270, y = 430)

root.mainloop()
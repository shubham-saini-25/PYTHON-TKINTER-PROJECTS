# GUI Calculator using Python Programming Language

from tkinter import *

root = Tk()
root.iconbitmap("D:/PYTHON MODULES/TKINTER/TKINTER PROJECTS/ICONs/Calculator.ico")
root.title("PYTHON GUI CALCULATOR")
root.geometry("340x378")

F = Frame(root, bg = "navy", bd = 10, width = 350, height = 400)
F.pack()

def press(text):
    num = txt.get()
    if num == "Error":
        txt.set("Error")
    else:
        txt.set(num + text)
        
def reset():
    txt.set("")
    
def cancel():
    txt.set(txt.get()[:-1])

def cal():
    try:
        txt.set(eval(txt.get()))
    except:
        txt.set("Error")
        
txt = StringVar()
Entry(F, textvariable = txt, font = ("None 20 bold"), state = "readonly", borderwidth = 2).grid(columnspan = 5,pady = 10, ipadx = 3,ipady = 8)

Button(F, text = "C",  command = reset, font = ("None 20 bold"), width = 4, bg ="yellow", activebackground = "lightblue").grid(row = 1, column = 0)
Button(F, text = "(", command = lambda:press("("), font = ("None 20 bold"), width = 4, bg ="yellow", activebackground = "lightblue").grid(row = 1, column = 1)
Button(F, text = ")", command = lambda:press(")"), font = ("None 20 bold"), width = 4, bg ="yellow", activebackground = "lightblue").grid(row = 1, column = 2)
Button(F, text = "CE", command = cancel, font = ("None 20 bold"), width = 4, bg ="yellow", activebackground = "lightblue").grid(row = 1, column = 3)

Button(F, text = "7", command = lambda:press("7"), font = ("None 20 bold"), width = 4, bg ="yellow", activebackground = "lightblue").grid(row = 2, column = 0)
Button(F, text = "8", command = lambda:press("8"), font = ("None 20 bold"), width = 4, bg ="yellow", activebackground = "lightblue").grid(row = 2, column = 1)
Button(F, text = "9", command = lambda:press("9"), font = ("None 20 bold"), width = 4, bg ="yellow", activebackground = "lightblue").grid(row = 2, column = 2)
Button(F, text = "/", command = lambda:press("/"), font = ("None 20 bold"), width = 4, bg ="yellow", activebackground = "steelblue1").grid(row = 2, column = 3)

Button(F, text = "4", command = lambda:press("4"), font = ("None 20 bold"), width = 4, bg ="yellow", activebackground = "lightblue").grid(row = 3, column = 0)
Button(F, text = "5", command = lambda:press("5"), font = ("None 20 bold"), width = 4, bg ="yellow", activebackground = "lightblue").grid(row = 3, column = 1)
Button(F, text = "6", command = lambda:press("6"), font = ("None 20 bold"), width = 4, bg ="yellow", activebackground = "lightblue").grid(row = 3, column = 2)
Button(F, text = "x", command = lambda:press("*"), font = ("None 20 bold"), width = 4, bg ="yellow", activebackground = "steelblue1").grid(row = 3, column = 3)

Button(F, text = "1", command = lambda:press("1"), font = ("None 20 bold"), width = 4, bg ="yellow", activebackground = "lightblue").grid(row = 4, column = 0)
Button(F, text = "2", command = lambda:press("2"), font = ("None 20 bold"), width = 4, bg ="yellow", activebackground = "lightblue").grid(row = 4, column = 1)
Button(F, text = "3", command = lambda:press("3"), font = ("None 20 bold"), width = 4, bg ="yellow", activebackground = "lightblue").grid(row = 4, column = 2)
Button(F, text = "-", command = lambda:press("-"), font = ("None 20 bold"), width = 4, bg ="yellow", activebackground = "steelblue1").grid(row = 4, column = 3)

Button(F, text = ".", command = lambda:press("."), font = ("None 20 bold"), width = 4, bg ="yellow", activebackground = "lightblue").grid(row = 5, column = 0)
Button(F, text = "0", command = lambda:press("0"), font = ("None 20 bold"), width = 4, bg ="yellow", activebackground = "lightblue").grid(row = 5, column = 1)
Button(F, text = "=", command = cal, font = ("None 20 bold"), width = 4, bg ="yellow", activebackground = "salmon2").grid(row = 5, column = 2)
Button(F, text = "+", command = lambda:press("+"), font = ("None 20 bold"), width = 4, bg ="yellow", activebackground = "steelblue1").grid(row = 5, column = 3)

# Label(root, text = "CALCULATOR", font = ("None 30 bold")).pack()

root.mainloop()
# GUI Scientific Calculator using Python Programming Language

from tkinter import *
from math import *

root = Tk()
# Download icons in '.ico' format from https://iconarchive.com/"
root.iconbitmap("D:/PYTHON MODULES/TKINTER/TKINTER PROJECTS/ICONs/Calculator.ico")
root.title("PYTHON GUI SCIENTIFIC CALCULATOR")
root.geometry("600x625+50+40")
root.resizable(0,0)

F = Frame(root, bg="darkslateblue", bd=10, width=350, height=500)
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
Entry(F, textvariable=txt, font=("None 30 bold"), bg="yellow", bd=5).grid(columnspan=15, pady=10, ipadx=58, ipady=12)


B11 = Button(F, text="sin", command=lambda:press("sin"), font=("None 25 bold"), bd=4, width=5, bg="springgreen1", activebackground="steelblue1")
B11.grid(row=1, column=0)
B12 = Button(F, text="cos", command=lambda:press("cos"), font=("None 25 bold"), bd=4, width=5, bg="springgreen1", activebackground="steelblue1")
B12.grid(row=1, column=1)
B13 = Button(F, text="tan", command=lambda:press("tan"), font=("None 25 bold"), bd=4, width=5, bg="springgreen1", activebackground="steelblue1")
B13.grid(row=1, column=2)
B14 = Button(F, text="log", command=lambda:press("log"), font=("None 25 bold"), bd=4, width=5, bg="springgreen1", activebackground="steelblue1")
B14.grid(row=1, column=3)
B15 = Button(F, text="Clear", command=reset, font=("None 25 bold"), bd=4, width=5, bg="tomato", activebackground="red")
B15.grid(row=1, column=4)


B21 = Button(F, text="pow", command=lambda:press("**"), font=("None 25 bold"), bd=4, width=5, bg="springgreen1", activebackground="steelblue1")
B21.grid(row=2, column=0)
B22 = Button(F, text="sqrt", command=lambda:press("sqrt"), font=("None 25 bold"), bd=4, width=5, bg="springgreen1", activebackground="steelblue1")
B22.grid(row=2, column=1)
B23 = Button(F, text="exp", command=lambda:press("exp"), font=("None 25 bold"), bd=4, width=5, bg="springgreen1", activebackground="steelblue1")
B23.grid(row=2, column=2)
B24 = Button(F, text="log10", command=lambda:press("log10"), font=("None 25 bold"), bd=4, width=5, bg="springgreen1", activebackground="steelblue1")
B24.grid(row=2, column=3)
B25 = Button(F, text="Del", command=cancel, font=("None 25 bold"), bd=4, width=5, bg="orange", activebackground="goldenrod1")
B25.grid(row=2, column=4)


B31 = Button(F, text="sinh", command=lambda:press("sinh"), font=("None 25 bold"), bd=4, width=5, bg="springgreen1", activebackground="steelblue1")
B31.grid(row=3, column=0)
B32 = Button(F, text="cosh", command=lambda:press("cosh"), font=("None 25 bold"), bd=4, width=5, bg="springgreen1", activebackground="steelblue1")
B32.grid(row=3, column=1)
B33 = Button(F, text="tanh", command=lambda:press("tanh"), font=("None 25 bold"), bd=4, width=5, bg="springgreen1", activebackground="steelblue1")
B33.grid(row=3, column=2)
B34 = Button(F, text="Deg", command=lambda:press("degrees"), font=("None 25 bold"), bd=4, width=5, bg="springgreen1", activebackground="steelblue1")
B34.grid(row=3, column=3)
B35 = Button(F, text="Rad", command=lambda:press("radians"), font=("None 25 bold"), bd=4, width=5, bg="springgreen1", activebackground="steelblue1")
B35.grid(row=3, column=4)


B41 = Button(F, text="7", command=lambda:press("7"), font=("None 25 bold"), bd=4, width=5, bg="springgreen3", activebackground="deepskyblue2")
B41.grid(row=4, column=0)
B42 = Button(F, text="8", command=lambda:press("8"), font=("None 25 bold"), bd=4, width=5, bg="springgreen3", activebackground="deepskyblue2")
B42.grid(row=4, column=1)
B43 = Button(F, text="9", command=lambda:press("9"), font=("None 25 bold"), bd=4, width=5, bg="springgreen3", activebackground="deepskyblue2")
B43.grid(row=4, column=2)
B44 = Button(F, text="x", command=lambda:press("*"), font=("None 25 bold"), bd=4, width=5, bg="springgreen", activebackground="steelblue2")
B44.grid(row=4, column=3)
B45 = Button(F, text="/", command=lambda:press("/"), font=("None 25 bold"), bd=4, width=5, bg="springgreen", activebackground="steelblue2")
B45.grid(row=4, column=4)


B51 = Button(F, text="4", command=lambda:press("4"), font=("None 25 bold"), bd=4, width=5, bg="springgreen3", activebackground="deepskyblue2")
B51.grid(row=5, column=0)
B52 = Button(F, text="5", command=lambda:press("5"), font=("None 25 bold"), bd=4, width=5, bg="springgreen3", activebackground="deepskyblue2")
B52.grid(row=5, column=1)
B53 = Button(F, text="6", command=lambda:press("6"), font=("None 25 bold"), bd=4, width=5, bg="springgreen3", activebackground="deepskyblue2")
B53.grid(row=5, column=2)
B54 = Button(F, text="+", command=lambda:press("+"), font=("None 25 bold"), bd=4, width=5, bg="springgreen", activebackground="steelblue2")
B54.grid(row=5, column=3)
B55 = Button(F, text="-", command=lambda:press("-"), font=("None 25 bold"), bd=4, width=5, bg="springgreen", activebackground="steelblue2")
B55.grid(row=5, column=4)


B61 = Button(F, text="1", command=lambda:press("1"), font=("None 25 bold"), bd=4, width=5, bg="springgreen3", activebackground="deepskyblue2")
B61.grid(row=6, column=0)
B62 = Button(F, text="2", command=lambda:press("2"), font=("None 25 bold"), bd=4, width=5, bg="springgreen3", activebackground="deepskyblue2")
B62.grid(row=6, column=1)
B63 = Button(F, text="3", command=lambda:press("3"), font=("None 25 bold"), bd=4, width=5, bg="springgreen3", activebackground="deepskyblue2")
B63.grid(row=6, column=2)
B64 = Button(F, text="(", command=lambda:press("("), font=("None 25 bold"), bd=4, width=5, bg="springgreen", activebackground="steelblue1")
B64.grid(row=6, column=3)
B65 = Button(F, text=")", command=lambda:press(")"), font=("None 25 bold"), bd=4, width=5, bg="springgreen", activebackground="steelblue1")
B65.grid(row=6, column=4)


B71 = Button(F, text="π", command=lambda:press("pi"), font=("None 25 bold"), bd=4, width=5, bg="springgreen1", activebackground="steelblue1")
B71.grid(row=7, column=0)
B72 = Button(F, text="0", command=lambda:press("0"), font=("None 25 bold"), bd=4, width=5, bg="springgreen3", activebackground="deepskyblue2")
B72.grid(row=7, column=1)
B73 = Button(F, text=".", command=lambda:press("."), font=("None 25 bold"), bd=4, width=5, bg="springgreen1", activebackground="steelblue1")
B73.grid(row=7, column=2)
B74 = Button(F, text="e", command=lambda:press("e"), font=("None 25 bold"), bd=4, width=5, bg="springgreen1", activebackground="steelblue1")
B74.grid(row=7, column=3)
B75 = Button(F, text="=", command=cal, font=("None 25 bold"), bd=4, width=5, bg="lime", activebackground="cyan")
B75.grid(row=7, column=4)

root.mainloop()

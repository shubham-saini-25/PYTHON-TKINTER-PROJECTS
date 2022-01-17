# Virtual Keyboard using Python Tkinter GUI
# This Virtual Keyboard is Made by:- @python_with_shubham

# importing the required Modules
from tkinter import *
import pyautogui

# Create a Tkinter window and set its Title, icon, Geometry
root = Tk()
root.title("VIRTUAL KEYBOARD")
# Download icons in '.ico' format from https://iconarchive.com/"
root.iconbitmap("D:/PYTHON MODULES/TKINTER/TKINTER PROJECTS/ICONs/Keyboard.ico")
root.geometry("1350x670+0+0")
root.config(bg="khaki")

# Create a Label and Text Editor
Label(root, text="Text Editor", font=("Arial 20 bold underline"), bg = "khaki").place(x = 370, y = 0)
input_text = Text(root, font=("Arial 13 bold"), bg = "pink", bd = 4, relief=SOLID)
input_text.place(x=100, y=40, width=700, height=220)
sb1 = Scrollbar(root)
sb1.place(x=800, y=40, height=220)
input_text.config(yscrollcommand=sb1.set)
sb1.config(command=input_text.yview)
input_text.focus_set()

# Create a Label and a Listbox
Label(root, text="Keys Pressed by System Keyboard", font=("Arial 18 bold underline"), bg = "khaki").place(x = 910, y = 0)
pressed_keys = Listbox(root, font=("Arial 13 bold"), bg = "orange", bd = 4, relief=SOLID, activestyle="none", selectbackground='orangered')
pressed_keys.place(x=910, y=40, width=400, height=220)
sb2 = Scrollbar(pressed_keys)
sb2.pack(side=RIGHT, fill=BOTH)
pressed_keys.config(yscrollcommand=sb2.set)
sb2.config(command=pressed_keys.yview)

# Create 2 variable and assign value as False
shift_btn_pressed = False
caps = False

# Create a Informaion Label
Label(root, text="Press Esc for Exit.\t\tPress Delete for Clear All Text.", font=("Arial 16 bold"), bg = "khaki").place(x = 400, y = 635)

# Create a Function for Entering Text from Virtual Keyboard
def press(text):
    input_text.insert(END, text)

# Create a Function for Detect pressed keys from System Keyboard
def system_keyboard_keys(e):
    key = e.keysym
    pressed_keys.insert(0, f"Key Pressed by System Keyboard : {key}")
    if key == "Escape":
        root.destroy()
    elif key == "Delete":
        delete()

# Create a Function for CapsLock Button Working in Virtual Keyboard
def capslock():
    global caps
    caps = not caps
    if(caps):
        caps_btn.config(bg="blue")
        B14.config(text="Q", command=lambda:press("Q")) , B15.config(text="W", command=lambda:press("W"))
        B16.config(text="E", command=lambda:press("E")) , B17.config(text="R", command=lambda:press("R"))
        B18.config(text="T", command=lambda:press("T")) , B19.config(text="Y", command=lambda:press("Y"))
        B20.config(text="U", command=lambda:press("U")) , B21.config(text="I", command=lambda:press("I"))
        B22.config(text="O", command=lambda:press("O")) , B23.config(text="P", command=lambda:press("P"))
        B27.config(text="A", command=lambda:press("A")) , B28.config(text="S", command=lambda:press("S"))
        B29.config(text="D", command=lambda:press("D")) , B30.config(text="F", command=lambda:press("F"))
        B31.config(text="G", command=lambda:press("G")) , B32.config(text="H", command=lambda:press("H"))
        B33.config(text="J", command=lambda:press("J")) , B34.config(text="K", command=lambda:press("K"))
        B35.config(text="L", command=lambda:press("L")) , B38.config(text="Z", command=lambda:press("Z"))
        B39.config(text="X", command=lambda:press("X")) , B40.config(text="C", command=lambda:press("C"))
        B41.config(text="V", command=lambda:press("V")) , B42.config(text="B", command=lambda:press("B"))
        B43.config(text="N", command=lambda:press("N")) , B44.config(text="M", command=lambda:press("M"))
    else:
        caps_btn.config(bg="royalblue1")
        B14.config(text="q", command=lambda:press("q")) , B15.config(text="w", command=lambda:press("w"))
        B16.config(text="e", command=lambda:press("e")) , B17.config(text="r", command=lambda:press("r"))
        B18.config(text="t", command=lambda:press("t")) , B19.config(text="y", command=lambda:press("y"))
        B20.config(text="u", command=lambda:press("u")) , B21.config(text="i", command=lambda:press("i"))
        B22.config(text="o", command=lambda:press("o")) , B23.config(text="p", command=lambda:press("p"))
        B27.config(text="a", command=lambda:press("a")) , B28.config(text="s", command=lambda:press("s"))
        B29.config(text="d", command=lambda:press("d")) , B30.config(text="f", command=lambda:press("f"))
        B31.config(text="g", command=lambda:press("g")) , B32.config(text="h", command=lambda:press("h"))
        B33.config(text="j", command=lambda:press("j")) , B34.config(text="k", command=lambda:press("k"))
        B35.config(text="l", command=lambda:press("l")) , B38.config(text="z", command=lambda:press("z"))
        B39.config(text="x", command=lambda:press("x")) , B40.config(text="c", command=lambda:press("c"))
        B41.config(text="v", command=lambda:press("v")) , B42.config(text="b", command=lambda:press("b"))
        B43.config(text="n", command=lambda:press("n")) , B44.config(text="m", command=lambda:press("m"))
    
# Create a Function for Shift Button Working in Virtual Keyboard
def shift():
    global shift_btn_pressed
    shift_btn_pressed = not shift_btn_pressed
    if(shift_btn_pressed):
        left_shift_btn.config(bg="royalblue4")
        right_shift_btn.config(bg="royalblue4")
        B1.config(text="~", command=lambda:press("~")) , B2.config(text="!", command=lambda:press("!"))
        B3.config(text="@", command=lambda:press("@")) , B4.config(text="#", command=lambda:press("#"))
        B5.config(text="$", command=lambda:press("$")) , B6.config(text="%", command=lambda:press("%"))
        B7.config(text="^", command=lambda:press("^")) , B8.config(text="&", command=lambda:press("&"))
        B9.config(text="*", command=lambda:press("*")) , B10.config(text="(", command=lambda:press("("))
        B11.config(text=")", command=lambda:press(")")) , B12.config(text="_", command=lambda:press("_"))
        B13.config(text="+", command=lambda:press("+")) , B14.config(text="Q", command=lambda:press("Q"))
        B15.config(text="W", command=lambda:press("W")) , B16.config(text="E", command=lambda:press("E"))
        B17.config(text="R", command=lambda:press("R")) , B18.config(text="T", command=lambda:press("T"))
        B19.config(text="Y", command=lambda:press("Y")) , B20.config(text="U", command=lambda:press("U"))
        B21.config(text="I", command=lambda:press("I")) , B22.config(text="O", command=lambda:press("O"))
        B23.config(text="P", command=lambda:press("P")) , B24.config(text="{", command=lambda:press("{"))
        B25.config(text="}", command=lambda:press("}")) , B26.config(text="|", command=lambda:press("|"))
        B27.config(text="A", command=lambda:press("A")) , B28.config(text="S", command=lambda:press("S"))
        B29.config(text="D", command=lambda:press("D")) , B30.config(text="F", command=lambda:press("F"))
        B31.config(text="G", command=lambda:press("G")) , B32.config(text="H", command=lambda:press("H"))
        B33.config(text="J", command=lambda:press("J")) , B34.config(text="K", command=lambda:press("K"))
        B35.config(text="L", command=lambda:press("L")) , B36.config(text=":", command=lambda:press(":"))
        B37.config(text="”", command=lambda:press("”")) , B38.config(text="Z", command=lambda:press("Z"))
        B39.config(text="X", command=lambda:press("X")) , B40.config(text="C", command=lambda:press("C"))
        B41.config(text="V", command=lambda:press("V")) , B42.config(text="B", command=lambda:press("B"))
        B43.config(text="N", command=lambda:press("N")) , B44.config(text="M", command=lambda:press("M"))
        B45.config(text="<", command=lambda:press("<")) , B46.config(text=">", command=lambda:press(">"))
        B47.config(text="?", command=lambda:press("?"))
    else:
        left_shift_btn.config(bg="royalblue1")
        right_shift_btn.config(bg="royalblue1")
        B1.config(text="`", command=lambda:press("`")) , B2.config(text="1", command=lambda:press("1"))
        B3.config(text="2", command=lambda:press("2")) , B4.config(text="3", command=lambda:press("3"))
        B5.config(text="4", command=lambda:press("4")) , B6.config(text="5", command=lambda:press("5"))
        B7.config(text="6", command=lambda:press("6")) , B8.config(text="7", command=lambda:press("7"))
        B9.config(text="8", command=lambda:press("8")) , B10.config(text="9", command=lambda:press("9"))
        B11.config(text="0", command=lambda:press("0")) , B12.config(text="-", command=lambda:press("-"))
        B13.config(text="=", command=lambda:press("=")) , B14.config(text="q", command=lambda:press("q"))
        B15.config(text="w", command=lambda:press("w")) , B16.config(text="e", command=lambda:press("e"))
        B17.config(text="r", command=lambda:press("r")) , B18.config(text="t", command=lambda:press("t"))
        B19.config(text="y", command=lambda:press("y")) , B20.config(text="u", command=lambda:press("u"))
        B21.config(text="i", command=lambda:press("i")) , B22.config(text="o", command=lambda:press("o"))
        B23.config(text="p", command=lambda:press("p")) , B24.config(text="[", command=lambda:press("["))
        B25.config(text="]", command=lambda:press("]")) , B26.config(text="\\", command=lambda:press("\\"))
        B27.config(text="a", command=lambda:press("a")) , B28.config(text="s", command=lambda:press("s"))
        B29.config(text="d", command=lambda:press("d")) , B30.config(text="f", command=lambda:press("f"))
        B31.config(text="g", command=lambda:press("g")) , B32.config(text="h", command=lambda:press("h"))
        B33.config(text="j", command=lambda:press("j")) , B34.config(text="k", command=lambda:press("k"))
        B35.config(text="l", command=lambda:press("l")) , B36.config(text=";", command=lambda:press("l"))
        B37.config(text="'", command=lambda:press("l")) , B38.config(text="z", command=lambda:press("z"))
        B39.config(text="x", command=lambda:press("x")) , B40.config(text="c", command=lambda:press("c"))
        B41.config(text="v", command=lambda:press("v")) , B42.config(text="b", command=lambda:press("b"))
        B43.config(text="n", command=lambda:press("n")) , B44.config(text="m", command=lambda:press("m"))
        B45.config(text=",", command=lambda:press(",")) , B46.config(text=".", command=lambda:press("."))
        B47.config(text="/", command=lambda:press("/"))

# Create a Function for Escape Button Working in Virtual Keyboard
def esc():
    root.destroy()

# Create a Function for Delete Button Working in Virtual Keyboard
def delete():
    input_text.delete(1.0, END)
    pressed_keys.delete(0, END)

# Create a Function for Backspace Button Working in Virtual Keyboard
def backspace():
    input_text.delete("end-2c")

# Create some Frames for our Virtual Keyboard keys
frame=Frame(root, bg="royalblue1", bd=3, relief=SOLID)
frame.place(x=22, y=280)

f1=Frame(frame, bg="royalblue1", bd=2)
f1.grid(row=0, column=0)

f2=Frame(frame, bg="royalblue1", bd=2)
f2.grid(row=1, column=0)

f3=Frame(frame, bg="royalblue1", bd=2)
f3.grid(row=2, column=0)

f4=Frame(frame, bg="royalblue1", bd=2)
f4.grid(row=3, column=0)

f5=Frame(frame, bg="royalblue1", bd=2)
f5.grid(row=4, column=0)

f6=Frame(frame, bg="royalblue1", bd=2)
f6.grid(row=5, column=0)

# Display window 10 image on Window Button
photo=PhotoImage(file=r"D:\PYTHON MODULES\TKINTER\TKINTER PROJECTS\ICONs\Window 10 icon.png")
photoimage=photo.subsample(2, 3)

# Create a Function for Displaying all the Vitual Keyboard Buttons
def keyboard_buttons():
    global left_shift_btn,right_shift_btn,caps_btn,B1,B2,B3,B4,B5,B6,B7,B8,B9,B10,B11,B12,B13,B14,B15,B16,B17,B18,B19,B20,B21,B22,B23,B24,B25,B26,B27,B28,B29,B30,B31,B32,B33,B34,B35,B36,B37,B38,B39,B40,B41,B42,B43,B44,B45,B46,B47
    Button(f1, text="Esc", font=("Arial 13 bold"), command=lambda:esc(), bg="royalblue1", activebackground="royalblue3", width=6, height=1, bd=4).grid(row=0, column=0)
    Button(f1, text="F1", font=("Arial 13 bold"), bg="royalblue1", activebackground="royalblue3", width=6, height=1, bd=4).grid(row=0, column=1)
    Button(f1, text="F2", font=("Arial 13 bold"), bg="royalblue1", activebackground="royalblue3", width=6, height=1, bd=4).grid(row=0, column=2)
    Button(f1, text="F3", font=("Arial 13 bold"), bg="royalblue1", activebackground="royalblue3", width=6, height=1, bd=4).grid(row=0, column=3)
    Button(f1, text="F4", font=("Arial 13 bold"), bg="royalblue1", activebackground="royalblue3", width=6, height=1, bd=4).grid(row=0, column=4)
    Button(f1, text="F5", font=("Arial 13 bold"), bg="royalblue1", activebackground="royalblue3", width=6, height=1, bd=4).grid(row=0, column=5)
    Button(f1, text="F6", font=("Arial 13 bold"), bg="royalblue1", activebackground="royalblue3", width=6, height=1, bd=4).grid(row=0, column=6)
    Button(f1, text="F7", font=("Arial 13 bold"), bg="royalblue1", activebackground="royalblue3", width=6, height=1, bd=4).grid(row=0, column=7)
    Button(f1, text="F8", font=("Arial 13 bold"), bg="royalblue1", activebackground="royalblue3", width=6, height=1, bd=4).grid(row=0, column=8)
    Button(f1, text="F9", font=("Arial 13 bold"), bg="royalblue1", activebackground="royalblue3", width=6, height=1, bd=4).grid(row=0, column=9)
    Button(f1, text="F10", font=("Arial 13 bold"), bg="royalblue1", activebackground="royalblue3", width=6, height=1, bd=4).grid(row=0, column=10)
    Button(f1, text="F11", font=("Arial 13 bold"), bg="royalblue1", activebackground="royalblue3", width=6, height=1, bd=4).grid(row=0, column=11)
    Button(f1, text="F12", font=("Arial 13 bold"), bg="royalblue1", activebackground="royalblue3", width=6, height=1, bd=4).grid(row=0, column=12)
    Button(f1, text="Home", font=("Arial 13 bold"), bg="royalblue1", activebackground="royalblue3", width=7, height=1, bd=4).grid(row=0, column=13)
    Button(f1, text="End", font=("Arial 13 bold"), bg="royalblue1", activebackground="royalblue3", width=7, height=1, bd=4).grid(row=0, column=14)
    Button(f1, text="Insert", font=("Arial 13 bold"), bg="royalblue1", activebackground="royalblue3", width=7, height=1, bd=4).grid(row=0, column=15)
    Button(f1, text="Delete", font=("Arial 13 bold"), command=lambda:delete(), bg="royalblue1", activebackground="royalblue3", width=7, height=1, bd=4).grid(row=0, column=16)
    Button(f2, text="Backspace", font=("Arial 13 bold"), command=lambda:backspace(), bg="royalblue1", activebackground="royalblue3", width=9, height=2, bd=4).grid(row=0, column=13)
    Button(f3, text="Tab", font=("Arial 13 bold"), command=lambda:press("     "), bg="royalblue1", activebackground="royalblue3", width=7, height=2, bd=4).grid(row=0, column=0)
    Button(f4, text="Enter", font=("Arial 13 bold"), command=lambda:press("\n") , bg="royalblue1", activebackground="royalblue3", width=12, height=2, bd=4).grid(row=0, column=12)
    Button(f5, text="↑", font=("Calibri 12 bold"), command=lambda:press("↑"), bg="royalblue1", activebackground="royalblue3", width=8, height=2, bd=4).grid(row=0, column=11)

    caps_btn = Button(f4, text="Caps Lock", font=("Arial 13 bold"), command=lambda:capslock(), bg="royalblue1", activebackground="royalblue3", width=11, height=2, bd=4)
    caps_btn.grid(row=0, column=0)

    left_shift_btn = Button(f5, text="Shift", font=("Arial 13 bold"), command=lambda:shift(), bg="royalblue1", activebackground="royalblue3", width=12, height=2, bd=4)
    left_shift_btn.grid(row=0, column=0)  

    right_shift_btn = Button(f5, text="Shift", font=("Arial 13 bold"), command=lambda:shift(), bg="royalblue1", activebackground="royalblue3", width=16, height=2, bd=4)
    right_shift_btn.grid(row=0, column=12)
    
    Button(f6, text="Ctrl", font=("Arial 13 bold"), bg="royalblue1", activebackground="royalblue3", width=10, height=2, bd=4).grid(row=0, column=0)
    Button(f6, text="Fn", font=("Arial 13 bold"), command=lambda:press(""), bg="royalblue1", activebackground="royalblue3", width=8, height=2, bd=4).grid(row=0, column=1)
    Button(f6, image=photoimage, bg="royalblue1", command=lambda:pyautogui.hotkey('win'), activebackground="royalblue3", width=70, height=46, bd=4).grid(row=0, column=2)
    Button(f6, text="Alt", font=("Arial 13 bold"), bg="royalblue1", activebackground="royalblue3", width=10, height=2, bd=4).grid(row=0, column=3)
    Button(f6, text="", font=("Arial 13 bold"), command=lambda:press(" "), bg="royalblue1", activebackground="royalblue3", width=44, height=2, bd=4).grid(row=0, column=4)
    Button(f6, text="Alt", font=("Arial 13 bold"), bg="royalblue1", activebackground="royalblue3", width=10, height=2, bd=4).grid(row=0, column=5)
    Button(f6, text="←", font=("Calibri 12 bold"), command=lambda:press("←"), bg="royalblue1", activebackground="royalblue3", width=8, height=2, bd=4).grid(row=0, column=6)
    Button(f6, text="↓", font=("Calibri 12 bold"), command=lambda:press("↓"), bg="royalblue1", activebackground="royalblue3", width=8, height=2, bd=4).grid(row=0, column=7)
    Button(f6, text="→", font=("Calibri 12 bold"), command=lambda:press("→"), bg="royalblue1", activebackground="royalblue3", width=8, height=2, bd=4).grid(row=0, column=8)
    Button(f6, text="Ctrl", font=("Arial 13 bold"), bg="royalblue1", activebackground="royalblue3", width=8, height=2, bd=4).grid(row=0, column=9)

    B1=Button(f2, text="`", font=("Arial 13 bold"), command=lambda:press("`"), bg="royalblue1", activebackground="royalblue3", width=5, height=2, bd=4)
    B1.grid(row=0, column=0)
    B2=Button(f2, text="1", font=("Arial 13 bold"), command=lambda:press("1"), bg="royalblue1", activebackground="royalblue3", width=8, height=2, bd=4)
    B2.grid(row=0, column=1)
    B3=Button(f2, text="2", font=("Arial 13 bold"), command=lambda:press("2"), bg="royalblue1", activebackground="royalblue3", width=8, height=2, bd=4)
    B3.grid(row=0, column=2)
    B4=Button(f2, text="3", font=("Arial 13 bold"), command=lambda:press("3"), bg="royalblue1", activebackground="royalblue3", width=8,height=2, bd=4)
    B4.grid(row=0, column=3)
    B5=Button(f2, text="4", font=("Arial 13 bold"), command=lambda:press("4"), bg="royalblue1", activebackground="royalblue3", width=8, height=2, bd=4)
    B5.grid(row=0, column=4)
    B6=Button(f2, text="5", font=("Arial 13 bold"), command=lambda:press("5"), bg="royalblue1", activebackground="royalblue3", width=8, height=2, bd=4)
    B6.grid(row=0, column=5)
    B7=Button(f2, text="6", font=("Arial 13 bold"), command=lambda:press("6"), bg="royalblue1", activebackground="royalblue3", width=8, height=2, bd=4)
    B7.grid(row=0, column=6)
    B8=Button(f2, text="7", font=("Arial 13 bold"), command=lambda:press("7"), bg="royalblue1", activebackground="royalblue3", width=8, height=2, bd=4)
    B8.grid(row=0, column=7)
    B9=Button(f2, text="8", font=("Arial 13 bold"), command=lambda:press("8"), bg="royalblue1", activebackground="royalblue3", width=8, height=2, bd=4)
    B9.grid(row=0, column=8)
    B10=Button(f2, text="9", font=("Arial 13 bold"), command=lambda:press("9"), bg="royalblue1", activebackground="royalblue3", width=8, height=2, bd=4)
    B10.grid(row=0, column=9)
    B11=Button(f2, text="0", font=("Arial 13 bold"), command=lambda:press("0"), bg="royalblue1", activebackground="royalblue3", width=8, height=2, bd=4)
    B11.grid(row=0, column=10)
    B12=Button(f2, text="-", font=("Arial 13 bold"), command=lambda:press("-"), bg="royalblue1", activebackground="royalblue3", width=8, height=2, bd=4)
    B12.grid(row=0, column=11)
    B13=Button(f2, text="=", font=("Arial 13 bold"), command=lambda:press("="), bg="royalblue1", activebackground="royalblue3", width=8, height=2, bd=4)
    B13.grid(row=0, column=12)
    B14=Button(f3, text="q", font=("Arial 13 bold"), command=lambda:press("q"), bg="royalblue1", activebackground="royalblue3", width=8, height=2, bd=4)
    B14.grid(row=0, column=1)
    B15=Button(f3, text="w", font=("Arial 13 bold"), command=lambda:press("w"), bg="royalblue1", activebackground="royalblue3", width=8, height=2, bd=4)
    B15.grid(row=0, column=2)
    B16=Button(f3, text="e", font=("Arial 13 bold"), command=lambda:press("e"), bg="royalblue1", activebackground="royalblue3", width=8, height=2, bd=4)
    B16.grid(row=0, column=3)
    B17=Button(f3, text="r", font=("Arial 13 bold"), command=lambda:press("r"),bg="royalblue1", activebackground="royalblue3", width=8, height=2, bd=4)
    B17.grid(row=0, column=4)
    B18=Button(f3, text="t", font=("Arial 13 bold"), command=lambda:press("t"), bg="royalblue1", activebackground="royalblue3", width=8, height=2, bd=4)
    B18.grid(row=0, column=5)
    B19=Button(f3, text="y", font=("Arial 13 bold"), command=lambda:press("y"), bg="royalblue1", activebackground="royalblue3", width=8, height=2, bd=4)
    B19.grid(row=0, column=6)
    B20=Button(f3, text="u", font=("Arial 13 bold"), command=lambda:press("u"), bg="royalblue1", activebackground="royalblue3", width=8, height=2, bd=4)
    B20.grid(row=0, column=7)
    B21=Button(f3, text="i", font=("Arial 13 bold"), command=lambda:press("i"), bg="royalblue1", activebackground="royalblue3", width=8, height=2, bd=4)
    B21.grid(row=0, column=8)
    B22=Button(f3, text="o", font=("Arial 13 bold"), command=lambda:press("o"), bg="royalblue1", activebackground="royalblue3", width=8, height=2, bd=4)
    B22.grid(row=0, column=9)
    B23=Button(f3, text="p", font=("Arial 13 bold"), command=lambda:press("p"), bg="royalblue1", activebackground="royalblue3", width=8, height=2, bd=4)
    B23.grid(row=0, column=10)
    B24=Button(f3, text="[", font=("Arial 13 bold"), command=lambda:press("["), bg="royalblue1", activebackground="royalblue3", width=8, height=2, bd=4)
    B24.grid(row=0, column=11)
    B25=Button(f3, text="]", font=("Arial 13 bold"), command=lambda:press("]"), bg="royalblue1", activebackground="royalblue3", width=8, height=2, bd=4)
    B25.grid(row=0, column=12)
    B26=Button(f3, text="\ ", font=("Arial 13 bold"), command=lambda:press("\ "), bg="royalblue1", activebackground="royalblue3", width=7, height=2, bd=4)
    B26.grid(row=0, column=13)
    B27=Button(f4, text="a", font=("Arial 13 bold"), command=lambda:press("a"), bg="royalblue1", activebackground="royalblue3", width=8, height=2, bd=4)
    B27.grid(row=0, column=1)
    B28=Button(f4, text="s", font=("Arial 13 bold"), command=lambda:press("s"), bg="royalblue1", activebackground="royalblue3", width=8, height=2, bd=4)
    B28.grid(row=0, column=2)
    B29=Button(f4, text="d", font=("Arial 13 bold"), command=lambda:press("d"), bg="royalblue1", activebackground="royalblue3", width=8, height=2, bd=4)
    B29.grid(row=0, column=3)
    B30=Button(f4, text="f", font=("Arial 13 bold"), command=lambda:press("f"), bg="royalblue1", activebackground="royalblue3", width=8, height=2, bd=4)
    B30.grid(row=0, column=4)
    B31=Button(f4, text="g", font=("Arial 13 bold"), command=lambda:press("g"), bg="royalblue1", activebackground="royalblue3", width=8, height=2, bd=4)
    B31.grid(row=0, column=5)
    B32=Button(f4, text="h", font=("Arial 13 bold"), command=lambda:press("h"), bg="royalblue1", activebackground="royalblue3", width=8, height=2, bd=4)
    B32.grid(row=0, column=6)
    B33=Button(f4, text="j", font=("Arial 13 bold"), command=lambda:press("j"), bg="royalblue1", activebackground="royalblue3", width=8, height=2, bd=4)
    B33.grid(row=0, column=7)
    B34=Button(f4, text="k", font=("Arial 13 bold"), command=lambda:press("k"), bg="royalblue1", activebackground="royalblue3", width=8, height=2, bd=4)
    B34.grid(row=0, column=8)
    B35=Button(f4, text="l", font=("Arial 13 bold"), command=lambda:press("l"), bg="royalblue1", activebackground="royalblue3", width=8, height=2, bd=4)
    B35.grid(row=0, column=9)
    B36=Button(f4, text=";", font=("Arial 13 bold"), command=lambda:press(";"), bg="royalblue1", activebackground="royalblue3", width=8, height=2, bd=4)
    B36.grid(row=0, column=10)
    B37=Button(f4, text="'", font=("Arial 13 bold"), command=lambda:press("'"), bg="royalblue1", activebackground="royalblue3", width=8, height=2, bd=4)
    B37.grid(row=0, column=11)
    B38=Button(f5, text="z", font=("Arial 13 bold"), command=lambda:press("z"), bg="royalblue1", activebackground="royalblue3", width=8, height=2, bd=4)
    B38.grid(row=0, column=1)
    B39=Button(f5, text="x", font=("Arial 13 bold"), command=lambda:press("x"), bg="royalblue1", activebackground="royalblue3", width=8, height=2, bd=4)
    B39.grid(row=0, column=2)
    B40=Button(f5, text="c", font=("Arial 13 bold"), command=lambda:press("c"), bg="royalblue1", activebackground="royalblue3", width=8, height=2, bd=4)
    B40.grid(row=0, column=3)
    B41=Button(f5, text="v", font=("Arial 13 bold"), command=lambda:press("v"), bg="royalblue1", activebackground="royalblue3", width=8, height=2, bd=4)
    B41.grid(row=0, column=4)
    B42=Button(f5, text="b", font=("Arial 13 bold"), command=lambda:press("b"), bg="royalblue1", activebackground="royalblue3", width=8, height=2, bd=4)
    B42.grid(row=0, column=5)
    B43=Button(f5, text="n", font=("Arial 13 bold"), command=lambda:press("n"), bg="royalblue1", activebackground="royalblue3", width=8, height=2, bd=4)
    B43.grid(row=0, column=6)
    B44=Button(f5, text="m", font=("Arial 13 bold"), command=lambda:press("m"), bg="royalblue1", activebackground="royalblue3", width=8, height=2, bd=4)
    B44.grid(row=0, column=7)
    B45=Button(f5, text=",", font=("Arial 13 bold"), command=lambda:press(","), bg="royalblue1", activebackground="royalblue3", width=7, height=2, bd=4)
    B45.grid(row=0, column=8)
    B46=Button(f5, text=".", font=("Arial 13 bold"), command=lambda:press("."), bg="royalblue1", activebackground="royalblue3", width=7, height=2, bd=4)
    B46.grid(row=0, column=9)
    B47=Button(f5, text="/", font=("Arial 13 bold"), command=lambda:press("/"), bg="royalblue1", activebackground="royalblue3", width=7, height=2, bd=4)
    B47.grid(row=0, column=10)

keyboard_buttons()  # Call this Functin for display Virtual Keyboard

# Binding some events with Keys
root.bind("<Key>", lambda text:press(text))
root.bind("<Key>", lambda e:system_keyboard_keys(e))

root.mainloop()

##############################################################################################################################################
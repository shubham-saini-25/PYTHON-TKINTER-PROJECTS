# TIC-TAC-TOE GAME USING PYTHON

from tkinter import *
from tkinter import messagebox as msg

root = Tk()
root.title("TIC-TAC-TOE GAME")
root.config(bg = "steelblue3")
root.geometry("500x520+420+60")

count = 0
board=[['','','',], ['','','',], ['','','',]]

# Create a function to enter 'X' & 'O' while pressing buttton and for checking Winner
def show(btn, row, col):
    global count
    if btn["text"] == "":
        if count % 2 == 0:
            btn["text"] = "X"
            board[row][col] = "X"
            Label(root, text = "Player(2) = 'O'", font = ("None 25 bold"), bg = "yellow").place(x = 135, y = 16) 
        else:
            btn["text"] = "O"
            board[row][col] = "O"
            Label(root, text = "Player(1) = 'X'", font = ("None 25 bold"), bg = "yellow").place(x = 135, y = 16) 
        count = count + 1 
        if count >= 5:
            winner()
    else:
        msg.showerror("Error", "This box already has a value!") 

# function to close the game window
def close():
    root.destroy()
            
# Create a function to check winning conditions
def winner():
    if (board[0][0] == board[0][1] == board[0][2] == "X") or (board[1][0] == board[1][1] == board[1][2] == "X") or\
        (board[2][0] == board[2][1] == board[2][2] == "X") or (board[0][0] == board[1][0] == board[2][0] == "X") or\
        (board[0][1] == board[1][1] == board[2][1] == "X") or (board[0][2] == board[1][2] == board[2][2] == "X") or\
        (board[0][0] == board[1][1] == board[2][2] == "X") or (board[0][2] == board[1][1] == board[2][0] == "X"):
            msg.showinfo("Winner", "Player(1) = 'X' won the Game.")
            close()
    
    elif (board[0][0] == board[0][1] == board[0][2] == "O") or (board[1][0] == board[1][1] == board[1][2] == "O") or\
        (board[2][0] == board[2][1] == board[2][2] == "O") or (board[0][0] == board[1][0] == board[2][0] == "O") or\
        (board[0][1] == board[1][1] == board[2][1] == "O") or (board[0][2] == board[1][2] == board[2][2] == "O") or\
        (board[0][0] == board[1][1] == board[2][2] == "O") or (board[0][2] == board[1][1] == board[2][0] == "O"):
            msg.showinfo("Winner", "Player(2) = 'O' won the Game.")
            close()
            
    elif count == 9:
        msg.showinfo("Draw", "It's a Tie, Play Again!!!")
        close()

# create a Label
Label(root, text = "Player(1) = 'X'", font = ("None 25 bold"), bg = "yellow").place(x = 135, y = 16)            

# Create the button from btn1 to btn9                                                                  
btn1 = Button(root, text = "", command  = lambda:show(btn1, 0, 0), font = ("None 110 bold"), bg = "skyblue", activebackground = "bisque", relief = GROOVE, bd = 8)
btn1.place(x = 40, y = 71, width = 140, height = 140)

btn2 = Button(root, text = "", command  = lambda:show(btn2, 0, 1), font = ("None 110 bold"), bg = "skyblue", activebackground = "bisque", relief = GROOVE, bd = 8)
btn2.place(x = 180, y = 71, width = 140, height = 140)

btn3 = Button(root, text = "", command  = lambda:show(btn3, 0, 2), font = ("None 110 bold"), bg = "skyblue", activebackground = "bisque", relief = GROOVE, bd = 8)
btn3.place(x = 320, y = 71, width = 140, height = 140)

btn4 = Button(root, text = "", command  = lambda:show(btn4, 1, 0), font = ("None 110 bold"), bg = "skyblue", activebackground = "bisque", relief = GROOVE, bd = 8)
btn4.place(x = 40, y = 210, width = 140, height = 140)

btn5 = Button(root, text = "", command  = lambda:show(btn5, 1, 1), font = ("None 110 bold"), bg = "skyblue", activebackground = "bisque", relief = GROOVE, bd = 8)
btn5.place(x = 180, y = 210, width = 140, height = 140)

btn6 = Button(root, text = "", command  = lambda:show(btn6, 1, 2), font = ("None 110 bold"), bg = "skyblue", activebackground = "bisque", relief = GROOVE, bd = 8)
btn6.place(x = 320, y = 210, width = 140, height = 140)

btn7 = Button(root, text = "", command  = lambda:show(btn7, 2, 0), font = ("None 110 bold"), bg = "skyblue", activebackground = "bisque", relief = GROOVE, bd = 8)
btn7.place(x = 40, y = 350, width = 140, height = 140)

btn8 = Button(root, text = "", command  = lambda:show(btn8, 2, 1), font = ("None 110 bold"), bg = "skyblue", activebackground = "bisque", relief = GROOVE, bd = 8)
btn8.place(x = 180, y = 350, width = 140, height = 140)

btn9 = Button(root, text = "", command  = lambda:show(btn9, 2, 2), font = ("None 110 bold"), bg = "skyblue", activebackground = "bisque", relief = GROOVE, bd = 8)
btn9.place(x = 320, y = 350, width = 140, height = 140)

root.mainloop()

# Follow on Instagram:- @python_with_shubham
# Rock Paper Scissor Game

from tkinter import *
from tkinter import messagebox as msg
from PIL import Image, ImageTk
import random

root = Tk()
root.geometry("800x520+282+70")
root.title("ROCK PAPER SCISSOR GAME")
root.config(bg="light blue")

# Provide full path of Images
rock_img = "D:/PYTHON MODULES/TKINTER/TKINTER PROJECTS/ROCK-PAPER-SCISSOR/rock.png"
paper_img = "D:/PYTHON MODULES/TKINTER/TKINTER PROJECTS/ROCK-PAPER-SCISSOR/paper.png"
scissor_img = "D:/PYTHON MODULES/TKINTER/TKINTER PROJECTS/ROCK-PAPER-SCISSOR/scissor.png"

images = [rock_img, paper_img, scissor_img]

main_img = Image.open("D:/PYTHON MODULES/TKINTER/TKINTER PROJECTS/ROCK-PAPER-SCISSOR/rps.png")
main_img = main_img.resize((200, 70))
main_img = ImageTk.PhotoImage(main_img)
lbl = Label(image=main_img)
lbl.image = main_img
lbl.place(x = 298, y = 100)

def play():
    global player, lbl1
    player = random.choice(images)
    img1 = Image.open(player)
    img1 = img1.resize((235, 235))
    img1 = ImageTk.PhotoImage(img1)
    lbl1 = Label(image=img1)
    lbl1.image = img1
    lbl1.place(x = 55, y = 205) 

def comp():
    global computer, lbl2
    computer = random.choice(images)
    img2 = Image.open(computer)
    img2 = img2.resize((235, 235))
    img2 = ImageTk.PhotoImage(img2)
    lbl2 = Label(image=img2)
    lbl2.image = img2
    lbl2.place(x = 505, y = 205)


def conditions():
    if player == rock_img and computer == scissor_img:
        Label(root, text="Rock\t\t\tScissor", font=("None 25 bold"), bg = "lightblue", 
                                fg = "darkblue", width=35).place(x = 70, y = 450)
        msg.showinfo("Winner", "Player won the Game.")

    elif player == rock_img and computer == paper_img:
        Label(root, text="Rock\t\t\tPaper", font=("None 25 bold"), bg = "lightblue", 
                                fg = "darkblue", width=35).place(x = 50, y = 450)
        msg.showinfo("Winner", "Computer won the Game.")

    elif player == paper_img and computer == rock_img:
        Label(root, text="Paper\t\t\t    Rock", font=("None 25 bold"), bg = "lightblue", 
                                fg = "darkblue", width=35).place(x = 45, y = 450)
        msg.showinfo("Winner", "Player won the Game.")

    elif player == paper_img and computer == scissor_img:
        Label(root, text="Paper\t\t\t   Scissor", font=("None 25 bold"), bg = "lightblue", 
                                fg = "darkblue", width=35).place(x = 50, y = 450)
        msg.showinfo("Winner", "Computer won the Game.")

    elif player == scissor_img and computer == paper_img:
        Label(root, text="Scissor\t\t\t      Paper", font=("None 25 bold"), bg = "lightblue", 
                                fg = "darkblue", width=35).place(x = 40, y = 450)
        msg.showinfo("Winner", "Player won the Game.")

    elif player == scissor_img and computer == rock_img:
        Label(root, text="Scissor\t\t\t   Rock", font=("None 25 bold"), bg = "lightblue", 
                                fg = "darkblue", width=35).place(x = 40, y = 450)
        msg.showinfo("Winner", "Computer won the Game.")

    else:
        if player == rock_img and computer == rock_img:
            Label(root, text="Rock\t\t\t   Rock", font=("None 25 bold"), bg = "lightblue", 
                                fg = "darkblue", width=35).place(x = 60, y = 450)
            msg.showinfo("Draw", "It's a Draw, Play again!!!")
    
        elif player == paper_img and computer == paper_img:
            Label(root, text="Paper\t\t\t   Paper", font=("None 25 bold"), bg = "lightblue", 
                                fg = "darkblue", width=35).place(x = 60, y = 450)
            msg.showinfo("Draw", "It's a Draw, Play again!!!")

        elif player == scissor_img and computer == scissor_img:
            Label(root, text="Scissor\t\t\t   Scissor", font=("None 25 bold"), bg = "lightblue", 
                                fg = "darkblue", width=35).place(x = 50, y = 450)
            msg.showinfo("Draw", "It's a Draw, Play again!!!")


def reset():
    Frame(root, width=250, height=250, bg = "plum3", relief=RIDGE, bd = 5).place(x = 50, y = 200)
    Frame(root, width=250, height=250, bg = "plum3", relief=RIDGE, bd = 5).place(x = 500, y = 200)
    Label(root, width=200, font=("None 25 bold"), bg = "lightblue").place(x = 100, y = 450)
    lbl1.destroy()
    lbl2.destroy()
    
    
Label(root, text="ROCK PAPER SCISSOR GAME", font=("None 35 bold"), relief=SUNKEN, bg = "orange").place(x = 60, y = 20)

Label(root, text="Player", font=("None 25 bold"), bd = 5, bg="light blue").place(x = 120, y = 150)

Frame(root, width=250, height=250, bg = "plum3", relief=RIDGE, bd = 5).place(x = 50, y = 200)

Label(root, text="Computer", font=("None 25 bold"), bd = 5, bg="light blue").place(x = 550, y = 150)

Frame(root, width=250, height=250, bg = "plum3", relief=RIDGE, bd = 5).place(x = 500, y = 200)

Button(root, text="Play", font=("None 20 bold"), bg = "gold", relief=RAISED, bd = 5, 
                            activebackground="yellow", command=lambda:[play(), comp(), conditions()]).place(x = 360, y = 250)

Button(root, text="Reset", font=("None 20 bold"), bg = "tan1", relief=RAISED, bd = 5, 
                            activebackground="tan1", command=reset).place(x = 350, y = 350)

root.mainloop()

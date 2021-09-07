
from tkinter import *
from instabot import Bot

root = Tk()
root.geometry("800x400")

def upload_post():
    Insta_bot = Bot()
    
    Insta_bot.login(username = "shubham_saini_15", password = "@")
    
    Insta_bot.upload_photo("D:/WEB DEVELOPEMENT/HTML PROGRAM/micky.png", caption ="This Post is Uploaded using Python InstaBot.")
    
Label(root, text = "Enter Your Username:", font = ("None 20 bold")).place(x = 10, y = 50)
user = StringVar()
Entry(root, textvariable = user, font = ("None 20 bold"), bg = "orange", bd = 4).place(x = 350, y = 50)

Label(root, text = "Enter Your Password:", font = ("None 20 bold"), ).place(x = 10, y = 150)
pswrd = StringVar()
Entry(root, textvariable = pswrd, font = ("None 20 bold"), bg = "orange", bd = 4).place(x = 350, y = 150)

Button(root, text = "Upload", command = upload_post, font = ("None 20 bold"), bd = 7).place(x = 250, y = 300)

root.mainloop()
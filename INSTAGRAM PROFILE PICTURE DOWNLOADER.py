# Instagram Profile Picture Downloader

from tkinter import *
import instaloader

root = Tk()
root.title("INSTAGRAM PROFILE PIC DOWNLOADER")
root.geometry("700x250")
root.config(bg = "pink")

def download_Insta_profile_Pic():
    download = instaloader.Instaloader()
    user_name = user.get()
    download.download_profile(user_name, profile_pic_only = True)

Label(root, text = "Instagram Profile Pic Downloader", font = ("None 30 bold underline"),
      bg = "pink", fg= "darkblue").place(x = 35, y = 5)

Label(root, text = "Enter the Username: ", font = ("None 20 bold"), bg = "pink").place(x = 35, y = 100)

user = StringVar()
Entry(root, textvariable = user, font = ("None 20 bold"), bg = "khaki", bd = 4, width = 23).place(x = 325, y = 100)

Button(root, text = "Download Profile Picture", command = download_Insta_profile_Pic, font = ("None 20 bold"),
       bg = "cyan", activebackground = "cyan3", bd = 5).place(x = 170, y = 170)

root.mainloop()
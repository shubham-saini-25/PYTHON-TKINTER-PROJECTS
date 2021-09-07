# Required Module:- pip install webbrowser

from tkinter import *
import webbrowser

root = Tk()
# get icons from here -- iconarchive.com
root.iconbitmap("D:/PYTHON MODULES/TKINTER/TKINTER PROJECTS/ICONs/Chrome.ico")
root.geometry("900x500+100+50")
root.title("Web Browser")
root.config(bg = "skyblue")

def search():
    search = Data.get() 
    url = f"https://www.google.com/search?&q={search}"
    webbrowser.open(url)
    Data.set("")

def google():
    webbrowser.open("www.google.com")
    
def youtube():
    webbrowser.open("www.youtube.com")
    
def facebook():
    webbrowser.open("www.facebook.com")
    
def instagram():
    webbrowser.open("www.instagram.com")

Label(root, text = "Web Browser", font = ("None 45 bold underline"), bg = "lightblue").place(x = 270, y = 15)

Data = StringVar()
Entry(root, textvariable = Data, font = ("None 25 bold"), width = 25, bg = "khaki1").place(x = 150, y = 150, height = 50)

Button(root, text = "Search", command = search, font = ("None 20 bold"), bg = "darkolivegreen3", activebackground = "green3", bd = 4).place(x = 650, y = 145)

Button(root, text = "Google", command = google, font = ("None 25 bold"), bg = "orange", activebackground = "orangered").place(x = 180, y = 250)

Button(root, text = "Youtube", command = youtube, font = ("None 25 bold"), bg = "firebrick1", activebackground = "firebrick3").place(x = 420, y = 250)

Button(root, text = "Facebook", command = facebook, font = ("None 25 bold"), bg = "royalblue", activebackground = "dodgerblue").place(x = 160, y = 350)

Button(root, text = "Instagram", command = instagram, font = ("None 25 bold"), bg = "deeppink", activebackground = "hotpink").place(x = 405, y = 350)

root.mainloop()
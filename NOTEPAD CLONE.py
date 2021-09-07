# Notepad Clone using Python Tkinter

from tkinter import *

root = Tk()
root.title("Untitled - Notepad")
root.geometry("400x300")
root.config(bg = "white")

Text(root, height = 600, width = 1350, font = ("Consolas 16")).pack()

menubar = Menu(root)

File = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = "File", menu = File)
File.add_command(label = "New                  Ctrl+N", command = None)
File.add_command(label = "Open...             Ctrl+O", command = None)
File.add_command(label = "Save                  Ctrl+S", command = None)
File.add_command(label = "Save As...", command = None)
File.add_separator()
File.add_command(label = "Page Setup...", command = None)
File.add_command(label = "Print...               Ctrl+P", command = None)
File.add_separator()
File.add_command(label = "Exit", command = exit)

Edit = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = "Edit", menu = Edit)
Edit.add_command(label = "Undo                                  Ctrl+Z", command = None)
Edit.add_separator()
Edit.add_command(label = "Cut                                     Ctrl+X", command = None)
Edit.add_command(label = "Copy                                  Ctrl+C", command = None)
Edit.add_command(label = "Paste                                  Ctrl+V", command = None)
Edit.add_command(label = "Delete                                    Del", command = None)
Edit.add_separator()
Edit.add_command(label = "Search with Bing...           Ctrl+E", command = None)
Edit.add_command(label = "Find...                                 Ctrl+F", command = None)
Edit.add_command(label = "Find Next                                  F3", command = None)
Edit.add_command(label = "Replace...                           Ctrl+H", command = None)
Edit.add_command(label = "Go To...                              Ctrl+G", command = None)
Edit.add_separator()
Edit.add_command(label = "Select All                            Ctrl+A", command = None)
Edit.add_command(label = "Time/Date                                F5", command = None)
 
Format = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = "Format", menu = Format)
Format.add_command(label = "Word Wrap", command = None)
Format.add_command(label = "Font...", command = None)

View = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = "View", menu = View)
View.add_command(label = "Zoom", command = None)
View.add_command(label = "Status Bar", command = None)

Help = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = "Help", menu = Help)
Help.add_command(label = "View Help", command = None)
Help.add_separator()
Help.add_command(label = "About Notepad", command = None)

root.config(menu=menubar)
root.mainloop()
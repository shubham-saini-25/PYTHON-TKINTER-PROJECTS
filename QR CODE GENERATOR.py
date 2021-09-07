from tkinter import *
import qrcode

root = Tk()
root.title("QR Code Generator")
root.geometry("550x300")
root.config(bg = "khaki1")

def qr():
    
    img = qrcode.make(QR.get())
    
    img.save('D:/PYTHON MODULES/TKINTER/TKINTER PROJECTS/QR_Code1.png')

Label(root, text = "QR Code Generator", font = ("None 30 bold underline"), bg = "khaki1").place(x = 100, y = 10)

Label(root, text = "Enter Data:", font = ("None 20 bold"), bg = "khaki1").place(x = 10, y = 100)

QR = StringVar()
Entry(root, textvariable = QR, font = ("None 22 bold"), bg = "yellow2", bd = 8, relief = GROOVE).place(x = 180, y = 90)

Button(root, text = "Get QR CODE", command = qr, font = ("None 20 bold"), bg = "orange", bd = 5).place(x = 170, y = 180)

root.mainloop()
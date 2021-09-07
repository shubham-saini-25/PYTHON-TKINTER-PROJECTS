# ALARM CLOCK USING PYTHON

from tkinter import *
from datetime import datetime
import time
import winsound

root = Tk()
root.geometry("670x280+380+150")
root.title("Alarm Clock using Python")
root.config(bg = "gray")
root.resizable(0, 0)

def alarm():
    while True:
        time.sleep(1)
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")

        my_alarm = f"{Hour.get()}:{Min.get()}:{Sec.get()}"

        H, M, S = now.hour, now.minute, now.second
        print(H,":",M,":",S)

        if current_time == my_alarm:
            print("Hello Buddy")
            winsound.Beep(2500, 1000)
            root.destroy()

Label(root, text = "GUI ALARM CLOCK", font = ("None 35 bold underline"), bg = "gray").place(x = 130, y = 20)

Label(root, text = "Enter Time(24-Hour Format):", font = ("None 20 bold"), bg = "gray").place(x = 20, y = 120)

Hour = IntVar()
Hour.set("")
Entry(root, textvariable = Hour, font = ("None 20 bold"), bg = "lightpink", width = 3).place(x = 420, y = 120)
Label(root, text = ":", font = ("None 30 bold"), bg = "gray").place(x = 470, y = 110)

Min = IntVar()
Min.set("")
Entry(root, textvariable = Min, font = ("None 20 bold"), bg = "lightpink", width = 3).place(x = 490, y = 120)
Label(root, text = ":", font = ("None 30 bold"), bg = "gray").place(x = 540, y = 110)

Sec = IntVar()
Sec.set("")
Entry(root, textvariable = Sec, font = ("None 20 bold"), bg = "lightpink", width = 3).place(x = 560, y = 120)

Button(root, text = "Set Alarm", font = ("None 20 bold"), bg = "orange", bd = 5, command = alarm).place(x = 250, y = 190)

root.mainloop()

# Follow:- @python_with_shubham
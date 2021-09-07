# Required Module-1 :- pip install tk
# Required Module-2 :- pip install forex-python

from tkinter import *
from tkinter import ttk
from forex_python.converter import CurrencyRates

root = Tk()
root.geometry("660x350")
root.title("Currency Converter")
root.config(bg="gray75")
root.option_add("*TCombobox*Listbox*font", "None 10 bold")

def convert():
    Currency_Convert = CurrencyRates()
    orignal_currency = c1.get()  # Get the Orignal Currency
    converted_currency = c2.get() # Get the Currency in which you want to Convert Orignal Currency
    amount = float(C_input.get())  # Get the Amount of Orignal Currency
    rate = Currency_Convert.convert(orignal_currency, converted_currency, amount)
    return C_output.set(round(rate, 5)) # display the converted Currency into second EntryBox

Label(root, text="CURRENCY CONVERTER", font=("Arial 28 bold underline"), bg="gray75").place(x=100, y=2)

Label(root, text="Orignal Currency:-", font=("verdana 20 bold"), bg="gray75").place(x=35, y=80)
C_input = StringVar()
Entry(root, textvariable=C_input, font=("verdana 20 bold"),bg="khaki", width=8, bd=2, relief=RAISED).place(x=350, y=82)

currency1 = ["USD", "AUD", "CAD", "CHF", "INR", "JPY", "NZD", "EUR", "GBP", "NOK", "SGD", "CZK", "MXN", "PLN", "RUB", "TRY", "ZAR"]
c1 = ttk.Combobox(root, value=currency1, font=("verdana 19 bold"), width=5, state="readonly")
c1.set("Select")
c1.place(x=520, y=83)

Label(root, text="Converted Currency:-", font=("verdana 20 bold"), bg="gray75").place(x=10, y=150)
C_output = StringVar()
Entry(root, textvariable=C_output, font=("verdana 20 bold"), bg="seagreen1", width=8, bd=2, relief=RAISED).place(x=350, y=152)

currency2 = ["USD", "AUD", "CAD", "CHF", "INR", "JPY", "NZD", "EUR", "GBP", "NOK", "SGD", "CZK", "MXN", "PLN", "RUB", "TRY", "ZAR"]
c2 = ttk.Combobox(root, value=currency2, font=("verdana 19 bold"), width=5, state="readonly")
c2.set("Select")
c2.place(x=520, y=153)

Button(root, text="CONVERT", font=("verdana 20 bold"),bg="hotpink", bd=4, command=convert).place(x=260, y=240)

root.mainloop()

# Follow me on Instagram:- @python_with_shubham
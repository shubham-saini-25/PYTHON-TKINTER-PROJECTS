# Required Module-1 :- pip install tk
# Required Module-2 :- pip install forex-python

from tkinter import *
from tkinter import ttk
from forex_python.bitcoin import BtcConverter

root = Tk()
root.geometry("960x450")
root.title("Crypto Currency Converter")
root.config(bg="pink")
root.option_add("*TCombobox*Listbox*font", "None 10 bold")

bitcoin = BtcConverter()

# Convert Bitcoin into Currency
def convert_bit_to_cur():
    bit_currency = c1.get() 
    bit = float(bit_in.get())  
    bit_to_cur = bitcoin.convert_btc_to_cur(bit, bit_currency)
    return cur_out.set(round(bit_to_cur, 8))

# Convert Currency into Bitcoin
def convert_cur_to_bit():
    currency = c2.get()
    cur = float(cur_in.get())
    cur_to_bit = bitcoin.convert_to_btc(cur, currency)
    return bit_out.set(round(cur_to_bit, 5))

Label(root, text="CRYPTO CURRENCY CONVERTER", font=("Arial 30 bold underline"), bg="pink").place(x=140, y=10)

Label(root, text="Bitcoin to Currency:-", font=("verdana 20 bold"), bg="pink").place(x=10, y=100)

bit_in = StringVar()
Entry(root, textvariable=bit_in, font=("verdana 20 bold"), bg="khaki", width=8, bd=3, relief=RAISED).place(x=350, y=100)

cur_out = StringVar()
Entry(root, textvariable=cur_out, font=("verdana 20 bold"), bg="seagreen1", width=14, bd=3, relief=RAISED).place(x=660, y=99)

currency1 = ["USD", "AUD", "CAD", "CHF", "INR", "JPY", "NZD", "EUR", "GBP", "NOK", "SGD", "CZK", "MXN", "PLN", "RUB", "TRY", "ZAR"]
c1 = ttk.Combobox(root, value=currency1, font=("verdana 19 bold"), width=5, state="readonly")
c1.set("Select")
c1.place(x=520, y=101)

Label(root, text="Currency to Bitcoin:-", font=("verdana 20 bold"), bg="pink").place(x=10, y=280)

cur_in = StringVar()
Entry(root, textvariable=cur_in, font=("verdana 20 bold"), bg="seagreen1", width=14, bd=3, relief=RAISED).place(x=350, y=280)

bit_out = StringVar()
Entry(root, textvariable=bit_out, font=("verdana 20 bold"), bg="khaki", width=8, bd=3, relief=RAISED).place(x=770, y=279)

currency2 = ["USD", "AUD", "CAD", "CHF", "INR", "JPY", "NZD", "EUR", "GBP", "NOK", "SGD", "CZK", "MXN", "PLN", "RUB", "TRY", "ZAR"]
c2 = ttk.Combobox(root, value=currency2, font=("verdana 19 bold"), width=5, state="readonly")
c2.set("Select")
c2.place(x=635, y=281)

Button(root, text="CONVERT BITCOIN INTO CURRENCY", font=("verdana 17 bold"), bg="salmon1", bd=4, command=convert_bit_to_cur).place(x=260, y=175)

Button(root, text="CONVERT CURRENCY INTO BITCOIN", font=("verdana 17 bold"), bg="tan2", bd=4, command=convert_cur_to_bit).place(x=260, y=360)

root.mainloop()

# Follow me on Instagram:- @python_with_shubham
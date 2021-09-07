# Restaurant Bill Generating Software

# import the Required Modules
from tkinter import *
from tkinter import messagebox as msg
import random

# create Tkinter Window
root = Tk()
root.geometry("1380x700+0+0")
root.title("RESTAURANT BILLING SOFTWARE")
root.config(bg = "seagreen1")

# Specifies that only num values shows in Entry Box
def valid(char):
   if char.isdigit():
      return True
   else:
      return False
valid_num = (root.register(valid), '%P')

# It gives the Total of Items when we pressed Total Button
def total():
    
    if Quantity1.get() != 0:
        Total1.set(Quantity1.get()*float(Price1.get()))
    else:
        Total1.set("0")
    
    if Quantity2.get() != 0:
        Total2.set(Quantity2.get()*float(Price2.get()))
    else:
        Total2.set("0")
    
    if Quantity3.get() != 0:
        Total3.set(Quantity3.get()*float(Price3.get()))
    else:
        Total3.set("0")
    
    if Quantity4.get() != 0:
        Total4.set(Quantity4.get()*float(Price4.get()))
    else:
        Total4.set("0")
    
    if Quantity5.get() != 0:
        Total5.set(Quantity5.get()*float(Price5.get()))
    else:
        Total5.set("0")
    
    if Quantity6.get() != 0:
        Total6.set(Quantity6.get()*float(Price6.get()))
    else:
        Total6.set("0")
        
    if Quantity7.get() != 0:
        Total7.set(Quantity7.get()*float(Price7.get()))
    else:
        Total7.set("0")
    
    if Quantity8.get() != 0:
        Total8.set(Quantity8.get()*float(Price8.get()))
    else:
        Total8.set("0")
        
    if Quantity9.get() != 0:
        Total9.set(Quantity9.get()*float(Price9.get()))
    else:
        Total9.set("0")
    
    if Quantity10.get() != 0:
        Total10.set(Quantity10.get()*float(Price10.get()))
    else:
        Total10.set("0")
        
    if Quantity11.get() != 0:
        Total11.set(Quantity11.get()*float(Price11.get()))
    else:
        Total11.set("0")
    
    if Quantity12.get() != 0:
        Total12.set(Quantity12.get()*float(Price12.get()))
    else:
        Total12.set("0")
            
    if Quantity13.get() != 0:
        Total13.set(Quantity13.get()*float(Price13.get()))
    else:
        Total13.set("0")
    
    if Quantity14.get() != 0:
        Total14.set(Quantity14.get()*float(Price14.get()))
    else:
        Total14.set("0")
        
    if Quantity15.get() != 0:
        Total15.set(Quantity15.get()*float(Price15.get()))
    else:
        Total15.set("0")
    
    if Quantity16.get() != 0:
        Total16.set(Quantity16.get()*float(Price16.get()))
    else:
        Total16.set("0")
    
    if Quantity17.get() != 0:
        Total17.set(Quantity17.get()*float(Price17.get()))
    else:
        Total17.set("0")
    
    if Quantity18.get() != 0:
        Total18.set(Quantity18.get()*float(Price18.get()))
    else:
        Total18.set("0")
    
    if Quantity19.get() != 0:
        Total19.set(Quantity19.get()*float(Price19.get()))
    else:
        Total19.set("0")
    
    if Quantity20.get() != 0:
        Total20.set(Quantity20.get()*float(Price20.get()))
    else:
        Total20.set("0")
    
# It gives Customer details in Billing Area
def customer_details():
        billbox.delete(1.0, END)
        billbox.insert(END, "\n\t     FAMILY RESTAURANT")
        billbox.insert(END, "\n======================================")
        billbox.insert(END, f"\n  Customer Name\t   :   {C_Name.get()}\n   Phone Number\t     :   {P_number.get()}\n     Bill Number\t\t:         {Bill.get()}")
        billbox.insert(END, "\n======================================\n")
        billbox.insert(END, " Food Items\t\tQTY\tRate\tPrice")
        billbox.insert(END, "\n-------------------------------------------------------------------\n")

# It Gives the Total of Items in Billing Area
def bill():
    
    # Generate Random Number for Bill
    if Bill.get() == "":
            Bill.set(random.randint(1000,4999)) 
    
    # Display an error if Customer details is missing
    if C_Name.get() == "" or P_number.get() == "":
        msg.showerror("Customer Details", "Please Complete the Customer Details.")
    else:
        customer_details() 
            
        if Quantity1.get() != 0:
            billbox.insert(END, f" {L1.get()}\t\t{Quantity1.get()}\t{Price1.get()}\t{float(Total1.get())}\n")
            
        if Quantity2.get() != 0:
            billbox.insert(END, f" {L2.get()}\t\t{Quantity2.get()}\t{Price2.get()}\t{float(Total2.get())}\n")
        
        if Quantity3.get() != 0:
            billbox.insert(END, f" {L3.get()}\t\t{Quantity3.get()}\t{Price3.get()}\t{float(Total3.get())}\n")
        
        if Quantity4.get() != 0:
            billbox.insert(END, f" {L4.get()}\t\t{Quantity4.get()}\t{Price4.get()}\t{float(Total4.get())}\n")
            
        if Quantity5.get() != 0:
            billbox.insert(END, f" {L5.get()}\t\t{Quantity5.get()}\t{Price5.get()}\t{float(Total5.get())}\n")
            
        if Quantity6.get() != 0:
            billbox.insert(END, f" {L6.get()}\t\t{Quantity6.get()}\t{Price6.get()}\t{float(Total6.get())}\n")
        
        if Quantity7.get() != 0:
            billbox.insert(END, f" {L7.get()}\t\t{Quantity7.get()}\t{Price7.get()}\t{float(Total7.get())}\n")
        
        if Quantity8.get() != 0:
            billbox.insert(END, f" {L8.get()}\t\t{Quantity8.get()}\t{Price8.get()}\t{float(Total8.get())}\n")
        
        if Quantity9.get() != 0:
            billbox.insert(END, f" {L9.get()}\t\t{Quantity9.get()}\t{Price9.get()}\t{float(Total9.get())}\n")
        
        if Quantity10.get() != 0:
            billbox.insert(END, f" {L10.get()}\t\t{Quantity10.get()}\t{Price10.get()}\t{float(Total10.get())}\n")
            
        if Quantity11.get() != 0:
            billbox.insert(END, f" {L11.get()}\t\t{Quantity11.get()}\t{Price11.get()}\t{float(Total11.get())}\n")
            
        if Quantity12.get() != 0:
            billbox.insert(END, f" {L12.get()}\t\t{Quantity12.get()}\t{Price12.get()}\t{float(Total12.get())}\n")
            
        if Quantity13.get() != 0:
            billbox.insert(END, f" {L13.get()}\t\t{Quantity13.get()}\t{Price13.get()}\t{float(Total13.get())}\n")
        
        if Quantity14.get() != 0:
            billbox.insert(END, f" {L14.get()}\t\t{Quantity14.get()}\t{Price14.get()}\t{float(Total14.get())}\n")
            
        if Quantity15.get() != 0:
            billbox.insert(END, f" {L15.get()}\t\t{Quantity15.get()}\t{Price15.get()}\t{float(Total15.get())}\n")
            
        if Quantity16.get() != 0:
            billbox.insert(END, f" {L16.get()}\t\t{Quantity16.get()}\t{Price16.get()}\t{float(Total16.get())}\n")
            
        if Quantity17.get() != 0:
            billbox.insert(END, f" {L17.get()}\t\t{Quantity17.get()}\t{Price17.get()}\t{float(Total17.get())}\n")
            
        if Quantity18.get() != 0:
            billbox.insert(END, f" {L18.get()}\t\t{Quantity18.get()}\t{Price18.get()}\t{float(Total18.get())}\n")
            
        if Quantity19.get() != 0:
            billbox.insert(END, f" {L19.get()}\t\t{Quantity19.get()}\t{Price19.get()}\t{float(Total19.get())}\n")
        
        if Quantity20.get() != 0:
            billbox.insert(END, f" {L20.get()}\t\t{Quantity20.get()}\t{Price20.get()}\t{float(Total20.get())}\n")
        
        billbox.insert(END, "-------------------------------------------------------------------\n") 
    
        Total_Price = [Total1.get(), Total2.get(), Total3.get(), Total4.get(), Total5.get(), Total6.get(), Total7.get(), 
                        Total8.get(), Total9.get(), Total10.get(), Total11.get(), Total12.get(), Total13.get(), Total14.get(),
                            Total15.get(), Total16.get(),Total17.get(), Total18.get(), Total19.get(), Total20.get()]
    
        Total_Price_Sum = []
    
        Total_items = "1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20" 
    
        for i, v in enumerate(Total_Price):
            if Total_items.find(str(i)) > -1:
                Total_Price_Sum = Total_Price_Sum + [v]
    
        Tot = 0
    
        for i, v in enumerate(Total_Price_Sum):
            Tot = int(Tot) + int(v)

        billbox.insert(END, f"   Total Amount\t\t           :\t\t{float(Tot)}")
    
        billbox.insert(END, "\n-------------------------------------------------------------------\n")
    
        billbox.insert(END, "\n\t   Thank You, Visit again!!!\n")

# It Reset all the Entries   
def reset():
    C_Name.set("")  ,  P_number.set("")  ,  Bill.set(""), 
    
    # After Reset Phone and Bill number Entry, set them again for only get Int value not String
    Entry(root, validate = "key", validatecommand = valid_num, font = ("None 20 bold"), bg = "Khaki1").place(x = 760,y = 150)    
    
    Entry(root, validate = "key", validatecommand = valid_num, font = ("None 20 bold"), bg = "Khaki1", width = 8).place(x = 1210, y = 150)

    customer_details(),
    
    Quantity1.set("0")     ,     Total1.set("0"),
    Quantity2.set("0")     ,     Total2.set("0"),
    Quantity3.set("0")     ,     Total3.set("0"),
    Quantity4.set("0")     ,     Total4.set("0"),
    Quantity5.set("0")     ,     Total5.set("0"),
    Quantity6.set("0")     ,     Total6.set("0"),
    Quantity7.set("0")     ,     Total7.set("0"),
    Quantity8.set("0")     ,     Total8.set("0"),
    Quantity9.set("0")     ,     Total9.set("0"),
    Quantity10.set("0")    ,     Total10.set("0"),
    Quantity11.set("0")    ,     Total11.set("0")
    Quantity12.set("0")    ,     Total12.set("0"),
    Quantity13.set("0")    ,     Total13.set("0"),
    Quantity14.set("0")    ,     Total14.set("0"),
    Quantity15.set("0")    ,     Total15.set("0"),
    Quantity16.set("0")    ,     Total16.set("0"),
    Quantity17.set("0")    ,     Total17.set("0"),
    Quantity18.set("0")    ,     Total18.set("0"),
    Quantity19.set("0")    ,     Total19.set("0"),
    Quantity20.set("0")    ,     Total20.set("0"),
 
# It saves the Bill in text File when we press Save Button   
def save():
    info = msg.askyesno("Bill","Do you want to save the Bill.")
    if info > 0:
        bills = billbox.get(1.0, END)
        file1 = open(f"D:/PYTHON MODULES/TKINTER/TKINTER PROJECTS/RESTAURANT BILL  GENERATOR/BILLS/Bill - {Bill.get()}.txt", "w")
        file1.write(bills)
        file1.close()
        msg.showinfo("Thank You", f"Your Bill - {Bill.get()} Saved Successfully.")

# Create a Frame and Label for Restaurant  
Frame(root, width = 1360, height = 100, bg = "springgreen1", relief = GROOVE, bd = 10).place(x = 0, y = 0)
Label(root, text = "RESTAURANT  BILLING  SOFTWARE", font = ("None 40 bold underline"), bg = "springgreen1").place(x = 205, y = 10)

# Create a Frame and Label for Customer Details  
Frame(root, width = 1360, height = 95, bg = "springgreen1", relief = GROOVE, bd = 10).place(x = 0, y = 115)
Label(root, text = "Customer Details", font = ("None 22 bold"), bg = "springgreen1", fg = "midnightblue").place(x = 520, y = 100)

# Create a Label and EntryBox for Customer Name
Label(root, text = "Customer Name:-", font = ("None 20 bold"), bg = "springgreen1").place(x = 20, y = 150)
C_Name = StringVar()
Entry(root, textvariable = C_Name, font = ("None 20 bold"), bg = "Khaki1").place(x = 265, y = 150)

# Create a Label and EntryBox for Customer Phone Number
Label(root, text = "Phone No:-", font = ("None 20 bold"), bg = "springgreen1").place(x = 600, y = 150)
P_number = StringVar()
Entry(root, textvariable = P_number, validate = "key", validatecommand = valid_num, font = ("None 20 bold"), bg = "Khaki1").place(x = 760,y = 150)

# Create a Label and EntryBox for Bill Number
Label(root, text = "Bill No:-", font = ("None 20 bold"), bg = "springgreen1").place(x = 1090, y = 150)
Bill = StringVar()
Bill.set(random.randint(1000,4999))
Entry(root, textvariable = Bill, validate = "key", validatecommand = valid_num, font = ("None 20 bold"), bg = "Khaki1", width = 8).place(x = 1210, y = 150)

# Create a Frame and Label for Food Items
Frame(root, width = 465, height = 470, bg = "springgreen1", relief = GROOVE, bd = 10).place(x = 0, y = 225)
Label(root, text = "Food Items", font = ("None 22 bold"), bg = "springgreen1", fg = "midnightblue").place(x = 150, y = 210)

# Create Labels to Specifies the Items Name, Item Price, Item Quantity, Item Total
Label(root, text = "ITEMS", font = ("None 20 bold underline"), bg = "springgreen1").place(x = 40, y = 250)
Label(root, text = "PRICE", font = ("None 20 bold underline"), bg = "springgreen1").place(x = 175, y = 250)
Label(root, text = "QTY",   font = ("None 20 bold underline"), bg = "springgreen1").place(x = 275, y = 250)
Label(root, text = "TOTAL", font = ("None 20 bold underline"), bg = "springgreen1").place(x = 350, y = 250)

# Create Labels and Entryboxes for Item-1 to Item-10 (Line-309 to Line-427)

L1 = StringVar()
L1.set("ONION PIZZA")
Label(root, textvariable = L1 ,  font = ("None 15 bold"), bg = "springgreen1").place(x = 20, y = 300)
Price1 = IntVar()
Price1.set("150")
Entry(root, textvariable = Price1, font = ("None 15 bold"), width = 4, state = "readonly").place(x = 196, y = 300)
Quantity1 = IntVar()
Entry(root, textvariable = Quantity1, font = ("None 15 bold"), width = 4).place(x = 282, y = 300)
Total1 = IntVar()
Total1.set("0")
Entry(root, textvariable = Total1, font = ("None 15 bold"), width = 6, state = "readonly").place(x = 365, y = 300)

L2 = StringVar()
L2.set("TOMATO PIZZA")
Label(root, textvariable = L2, font = ("None 15 bold"), bg = "springgreen1").place(x = 13, y = 338)
Price2 = IntVar()
Price2.set("100")
Entry(root, textvariable = Price2, font = ("None 15 bold"), width = 4, state = "readonly").place(x = 196, y = 338)
Quantity2 = IntVar()
Entry(root, textvariable = Quantity2, font = ("None 15 bold"), width = 4).place(x = 282, y = 338)
Total2 = IntVar()
Total2.set("0")
Entry(root, textvariable = Total2, font = ("None 15 bold"), width = 6, state = "readonly").place(x = 365, y = 338)

L3 = StringVar()
L3.set("ICE-CREAM")
Label(root, textvariable = L3, font = ("None 15 bold"), bg = "springgreen1").place(x = 25, y = 378)
Price3 = IntVar()
Price3.set("25")
Entry(root, textvariable = Price3, font = ("None 15 bold"), width = 4, state = "readonly").place(x = 196, y = 378)
Quantity3 = IntVar()
Entry(root, textvariable = Quantity3, font = ("None 15 bold"), width = 4).place(x = 282, y = 378)
Total3 = IntVar()
Total3.set("0")
Entry(root, textvariable = Total3, font = ("None 15 bold"), width = 6, state = "readonly").place(x = 365, y = 378)

L4 = StringVar()
L4.set("BURGER")
Label(root, textvariable = L4, font = ("None 15 bold"), bg = "springgreen1").place(x = 30, y = 418)
Price4 = IntVar()
Price4.set("50")
Entry(root, textvariable = Price4, font = ("None 15 bold"), width = 4, state = "readonly").place(x = 196, y = 418)
Quantity4 = IntVar()
Entry(root, textvariable = Quantity4, font = ("None 15 bold"), width = 4).place(x = 282, y = 418)
Total4 = IntVar()
Total4.set("0")
Entry(root, textvariable = Total4, font = ("None 15 bold"), width = 6, state = "readonly").place(x = 365, y = 418)

L5 = StringVar()
L5.set("SANDWICH")
Label(root, textvariable = L5, font = ("None 15 bold"), bg = "springgreen1").place(x = 25, y = 458)
Price5 = IntVar()
Price5.set("20")
Entry(root, textvariable = Price5, font = ("None 15 bold"), width = 4, state = "readonly").place(x = 196, y = 458)
Quantity5 = IntVar()
Entry(root, textvariable = Quantity5, font = ("None 15 bold"), width = 4).place(x = 282, y = 458)
Total5 = IntVar()
Total5.set("0")
Entry(root, textvariable = Total5, font = ("None 15 bold"), width = 6, state = "readonly").place(x = 365, y = 458)

L6 = StringVar()
L6.set("PANCAKE")
Label(root, textvariable = L6, font = ("None 15 bold"), bg = "springgreen1").place(x = 27, y = 498)
Price6 = IntVar()
Price6.set("30")
Entry(root, textvariable = Price6, font = ("None 15 bold"), width = 4, state = "readonly").place(x = 196, y = 498)
Quantity6 = IntVar()
Entry(root, textvariable = Quantity6, font = ("None 15 bold"), width = 4).place(x = 282, y = 498)
Total6 = IntVar()
Total6.set("0")
Entry(root, textvariable = Total6, font = ("None 15 bold"), width = 6, state = "readonly").place(x = 365, y = 498)

L7 = StringVar()
L7.set("NOODLES")
Label(root, textvariable = L7, font = ("None 15 bold"), bg = "springgreen1").place(x = 25, y = 538)
Price7 = IntVar()
Price7.set("50")
Entry(root, textvariable = Price7, font = ("None 15 bold"), width = 4, state = "readonly").place(x = 196, y = 538)
Quantity7 = IntVar()
Entry(root, textvariable = Quantity7, font = ("None 15 bold"), width = 4).place(x = 282, y = 538)
Total7 = IntVar()
Total7.set("0")
Entry(root, textvariable = Total7, font = ("None 15 bold"), width = 6, state = "readonly").place(x = 365, y = 538)

L8 = StringVar()
L8.set("PAV BHAAJI")
Label(root, textvariable = L8, font = ("None 15 bold"), bg = "springgreen1").place(x = 18, y = 578)
Price8 = IntVar()
Price8.set("20")
Entry(root, textvariable = Price8, font = ("None 15 bold"), width = 4, state = "readonly").place(x = 196, y = 578)
Quantity8 = IntVar()
Entry(root, textvariable = Quantity8, font = ("None 15 bold"), width = 4).place(x = 282, y = 578)
Total8 = IntVar()
Total8.set("0")
Entry(root, textvariable = Total8, font = ("None 15 bold"), width = 6, state = "readonly").place(x = 365, y = 578)

L9 = StringVar()
L9.set("SAMOSA")
Label(root, textvariable = L9, font = ("None 15 bold"), bg = "springgreen1").place(x = 26, y = 615)
Price9 = IntVar()
Price9.set("10")
Entry(root, textvariable = Price9, font = ("None 15 bold"), width = 4, state = "readonly").place(x = 196, y = 615)
Quantity9 = IntVar()
Entry(root, textvariable = Quantity9, font = ("None 15 bold"), width = 4).place(x = 282, y = 615)
Total9 = IntVar()
Total9.set("0")
Entry(root, textvariable = Total9, font = ("None 15 bold"), width = 6, state = "readonly").place(x = 365, y = 615)

L10 = StringVar()
L10.set("MASALA DOSA")
Label(root, textvariable = L10, font = ("None 15 bold"), bg = "springgreen1").place(x = 11, y = 652)
Price10 = IntVar()
Price10.set("80")
Entry(root, textvariable = Price10, font = ("None 15 bold"), width = 4, state = "readonly").place(x = 196, y = 652)
Quantity10 = IntVar()
Entry(root, textvariable = Quantity10, font = ("None 15 bold"), width = 4).place(x = 282, y = 652)
Total10 = IntVar()
Total10.set("0")
Entry(root, textvariable = Total10, font = ("None 15 bold"), width = 6, state = "readonly").place(x = 365, y = 652)

# Create a Frame and Label for Drink Items  
Frame(root, width = 455, height = 470, bg = "springgreen1", relief = GROOVE, bd = 10).place(x = 470, y = 225)
Label(root, text = "Drink Items", font = ("None 22 bold"), bg = "springgreen1", fg = "midnightblue").place(x = 610, y = 210)

# Create Labels to Specifies the Items Name, Item Price, Item Quantity, Item Total
Label(root, text = "ITEMS",    font = ("None 20 bold underline"), bg = "springgreen1").place(x = 515, y = 250)
Label(root, text = "PRICE", font = ("None 20 bold underline"), bg = "springgreen1").place(x = 640, y = 250)
Label(root, text = "QTY",    font = ("None 20 bold underline"), bg = "springgreen1").place(x = 740, y = 250)
Label(root, text = "TOTAL", font = ("None 20 bold underline"), bg = "springgreen1").place(x = 815, y = 250)

# Create Labels and Entryboxes for Item-11 to Item-20 (Line-441 to Line-559)

L11 = StringVar()
L11.set("MILK SHAKE")
Label(root, textvariable = L11,  font = ("None 15 bold"), bg = "springgreen1").place(x = 497, y = 300)
Price11 = IntVar()
Price11.set("20")
Entry(root, textvariable = Price11, font = ("None 15 bold"), width = 4, state = "readonly").place(x = 660, y = 300)
Quantity11 = IntVar()
Entry(root, textvariable = Quantity11, font = ("None 15 bold"), width = 4).place(x = 748, y = 300)
Total11 = IntVar()
Total11.set("0")
Entry(root, textvariable = Total11, font = ("None 15 bold"), width = 6, state = "readonly").place(x = 830, y = 300)

L12 = StringVar()
L12.set("MANGO SHAKE")
Label(root, textvariable = L12, font = ("None 15 bold"), bg = "springgreen1").place(x = 489, y = 338)
Price12 = IntVar()
Price12.set("30")
Entry(root, textvariable = Price12, font = ("None 15 bold"), width = 4, state = "readonly").place(x = 660, y = 338)
Quantity12 = IntVar()
Entry(root, textvariable = Quantity12, font = ("None 15 bold"), width = 4).place(x = 748, y = 338)
Total12 = IntVar()
Total12.set("0")
Entry(root, textvariable = Total12, font = ("None 15 bold"), width = 6, state = "readonly").place(x = 830, y = 338)

L13 = StringVar()
L13.set("BANANA SHAKE")
Label(root, textvariable = L13, font = ("None 15 bold"), bg = "springgreen1").place(x = 489, y = 378)
Price13 = IntVar()
Price13.set("30")
Entry(root, textvariable = Price13, font = ("None 15 bold"), width = 4, state = "readonly").place(x = 660, y = 378)
Quantity13 = IntVar()
Entry(root, textvariable = Quantity13, font = ("None 15 bold"), width = 4).place(x = 748, y = 378)
Total13 = IntVar()
Total13.set("0")
Entry(root, textvariable = Total13, font = ("None 15 bold"), width = 6, state = "readonly").place(x = 830, y = 378)

L14 = StringVar()
L14.set("ORANGE JUICE")
Label(root, textvariable = L14, font = ("None 15 bold"), bg = "springgreen1").place(x = 489, y = 418)
Price14 = IntVar()
Price14.set("40")
Entry(root, textvariable = Price14, font = ("None 15 bold"), width = 4, state = "readonly").place(x = 660, y = 418)
Quantity14 = IntVar()
Entry(root, textvariable = Quantity14, font = ("None 15 bold"), width = 4).place(x = 748, y = 418)
Total14 = IntVar()
Total14.set("0")
Entry(root, textvariable = Total14, font = ("None 15 bold"), width = 6, state = "readonly").place(x = 830, y = 418)

L15 = StringVar()
L15.set("CHERRY JUICE")
Label(root, textvariable = L15, font = ("None 15 bold"), bg = "springgreen1").place(x = 493, y = 458)
Price15 = IntVar()
Price15.set("50")
Entry(root, textvariable = Price15, font = ("None 15 bold"), width = 4, state = "readonly").place(x = 660, y = 458)
Quantity15 = IntVar()
Entry(root, textvariable = Quantity15, font = ("None 15 bold"), width = 4).place(x = 748, y = 458)
Total15 = IntVar()
Total15.set("0")
Entry(root, textvariable = Total15, font = ("None 15 bold"), width = 6, state = "readonly").place(x = 830, y = 458)

L16 = StringVar()
L16.set("LEMON JUICE")
Label(root, textvariable = L16, font = ("None 15 bold"), bg = "springgreen1").place(x = 495, y = 498)
Price16 = IntVar()
Price16.set("20")
Entry(root, textvariable = Price16, font = ("None 15 bold"), width = 4, state = "readonly").place(x = 660, y = 498)
Quantity16 = IntVar()
Entry(root, textvariable = Quantity16, font = ("None 15 bold"), width = 4).place(x = 748, y = 498)
Total16 = IntVar()
Total16.set("0")
Entry(root, textvariable = Total16, font = ("None 15 bold"), width = 6, state = "readonly").place(x = 830, y = 498)

L17 = StringVar()
L17.set("PAPAYA JUICE")
Label(root, textvariable = L17, font = ("None 15 bold"), bg = "springgreen1").place(x = 491, y = 538)
Price17 = IntVar()
Price17.set("40")
Entry(root, textvariable = Price17, font = ("None 15 bold"), width = 4, state = "readonly").place(x = 660, y = 538)
Quantity17 = IntVar()
Entry(root, textvariable = Quantity17, font = ("None 15 bold"), width = 4).place(x = 748, y = 538)
Total17 = IntVar()
Total17.set("0")
Entry(root, textvariable = Total17, font = ("None 15 bold"), width = 6, state = "readonly").place(x = 830, y = 538)

L18 = StringVar()
L18.set("LICHI JUICE")
Label(root, textvariable = L18, font = ("None 15 bold"), bg = "springgreen1").place(x = 500, y = 578)
Price18 = IntVar()
Price18.set("50")
Entry(root, textvariable = Price18, font = ("None 15 bold"), width = 4, state = "readonly").place(x = 660, y = 578)
Quantity18 = IntVar()
Entry(root, textvariable = Quantity18, font = ("None 15 bold"), width = 4).place(x = 748, y = 578)
Total18 = IntVar()
Total18.set("0")
Entry(root, textvariable = Total18, font = ("None 15 bold"), width = 6, state = "readonly").place(x = 830, y = 578)

L19 = StringVar()
L19.set("APPLE SHAKE")
Label(root, textvariable = L19, font = ("None 15 bold"), bg = "springgreen1").place(x = 493, y = 615)
Price19 = IntVar()
Price19.set("40")
Entry(root, textvariable = Price19, font = ("None 15 bold"), width = 4, state = "readonly").place(x = 660, y = 615)
Quantity19 = IntVar()
Entry(root, textvariable = Quantity19, font = ("None 15 bold"), width = 4).place(x = 748, y = 615)
Total19 = IntVar()
Total19.set("0")
Entry(root, textvariable = Total19, font = ("None 15 bold"), width = 6, state = "readonly").place(x = 830, y = 615)

L20 = StringVar()
L20.set("VANILLA SHAKE")
Label(root, textvariable = L20, font = ("None 15 bold"), bg = "springgreen1").place(x = 485, y = 652)
Price20 = IntVar()
Price20.set("50")
Entry(root, textvariable = Price20, font = ("None 15 bold"), width = 4, state = "readonly").place(x = 660, y = 652)
Quantity20 = IntVar()
Entry(root, textvariable = Quantity20, font = ("None 15 bold"), width = 4).place(x = 748, y = 652)
Total20 = IntVar()
Total20.set("0")
Entry(root, textvariable = Total20, font = ("None 15 bold"), width = 6, state = "readonly").place(x = 830, y = 652)

# Create a Frame and Label for Billing Area
F = Frame(root, bg = "springgreen1", relief = GROOVE, bd = 10)
F.place(x = 930, y = 225, width = 310, height = 470)
Label(F, text = "Billing Area", font = ("None 22 bold"), bg = "springgreen1", width = 15, relief = GROOVE, bd = 8).pack()

# Add a Scrollbar in Billing Area
scrollbar = Scrollbar(F, orient = VERTICAL)
billbox = Text(F, yscrollcommand = scrollbar, font = ("utsaah 13 bold"))
scrollbar.pack(side = RIGHT, fill = Y)
scrollbar.config(command = billbox.yview)
billbox.pack(ipady = 5)

# Call the Customer_details() Function in the Billing Area
customer_details()

# Create a Frame for Buttons
Frame(root, width = 115, height = 400, bg = "springgreen1", relief = GROOVE, bd = 8).place(x = 1242, y = 268)

# Create Buttons for Performing Different Tasks
Button(root, text = "Total",    font = ("None 16 bold"), command = total, bg = "olivedrab1" , activebackground = "olivedrab1", bd = 3, width = 5).place(x = 1260, y = 285)
Button(root, text = "Get Bill", font = ("None 16 bold"), command = bill,  bg = "steelblue2" , activebackground = "steelblue2", bd = 3, width = 6).place(x = 1252, y = 365)
Button(root, text = "Save",     font = ("None 16 bold"), command = save,  bg = "yellow2" ,    activebackground = "yellow2",    bd = 3, width = 5).place(x = 1260, y = 445)
Button(root, text = "Clear",    font = ("None 16 bold"), command = reset, bg = "salmon" ,     activebackground = "salmon",     bd = 3, width = 5).place(x = 1260, y = 525)
Button(root, text = "Exit",     font = ("None 16 bold"), command = exit,  bg = "skyblue" ,    activebackground = "skyblue",    bd = 3, width = 5).place(x = 1260, y = 605)

# Close the Root window
root.mainloop()

# Follow :- @python_with_shubham
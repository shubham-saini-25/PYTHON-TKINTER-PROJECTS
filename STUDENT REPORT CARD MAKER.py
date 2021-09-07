# STUDENT REPORT CARD MAKING APP

from tkinter import *
from tkinter import ttk
from tkinter import messagebox as msg

root = Tk()
root.title("STUDENT REPORT CARD")
# Download icons in '.ico' format from https://iconarchive.com/"
root.iconbitmap("D:/PYTHON MODULES/TKINTER/TKINTER PROJECTS/ICONs/Student.ico")
root.option_add("*TCombobox*font","Arial 15 bold")
root.geometry("1355x700+0+0")
root.config(bg = "steelblue2")

# Create a Function for Calculate the Marks and Percentage
def calculate_marks():
       M = Maths.get()
       C = Chemistry.get()
       P = Physics.get()
       E = English.get()
       H = Hindi.get()
       grand_total = M + C + P + E + H
       Grand_total.set(grand_total)
       
       # It gives the Percentage
       Per = round((grand_total/500)*100,2)
       Percentage.set(Per)
       
       # It gives the CGPA
       CGPA.set(round(Per/9.5,1))
       
       # It Display the Garde of Maths according to Marks
       if(M <= 100  and M >= 91):
              Maths_Grade.set("A1")
       elif(M <= 90  and M >= 81):  
              Maths_Grade.set("A2")
       elif(M <= 80  and M >= 71):   
              Maths_Grade.set("B1")
       elif(M <= 70  and M >= 61):  
              Maths_Grade.set("B2")
       elif(M <= 60  and M >= 51):   
              Maths_Grade.set("C1")
       elif(M <= 50  and M >= 41):   
              Maths_Grade.set("C2")
       elif(M <= 40  and M >= 33):   
              Maths_Grade.set("D")
       else:
              Maths_Grade.set("F")
       
       # It Display the Garde of Chemistry according to Marks
       if(C <= 100  and C >= 91):
              Chemistry_Grade.set("A1")
       elif(C <= 90  and C >= 81):  
              Chemistry_Grade.set("A2")
       elif(C <= 80  and C >= 71):   
              Chemistry_Grade.set("B1")
       elif(C <= 70  and C >= 61):  
              Chemistry_Grade.set("B2")
       elif(C <= 60  and C >= 51):   
              Chemistry_Grade.set("C1")
       elif(C <= 50  and C >= 41):   
              Chemistry_Grade.set("C2")
       elif(C <= 40  and C >= 33):   
              Chemistry_Grade.set("D")
       else:
              Chemistry_Grade.set("F")
       
       # It Display the Garde of Physics according to Marks
       if(P <= 100  and P >= 91):
              Physics_Grade.set("A1")
       elif(P <= 90  and P >= 81):  
              Physics_Grade.set("A2")
       elif(P <= 80  and P >= 71):   
              Physics_Grade.set("B1")
       elif(P <= 70  and P >= 61):  
              Physics_Grade.set("B2")
       elif(P <= 60  and P >= 51):   
              Physics_Grade.set("C1")
       elif(P <= 50  and P >= 41):   
              Physics_Grade.set("C2")
       elif(P <= 40  and P >= 33):   
              Physics_Grade.set("D")
       else:
              Physics_Grade.set("F")
              
       # It Display the Garde of English according to Marks
       if(E <= 100  and E >= 91):
              English_Grade.set("A1")
       elif(E <= 90  and E >= 81):  
              English_Grade.set("A2")
       elif(E <= 80  and E >= 71):   
              English_Grade.set("B1")
       elif(E <= 70  and E >= 61):  
              English_Grade.set("B2")
       elif(E <= 60  and E >= 51):   
              English_Grade.set("C1")
       elif(E <= 50  and E >= 41):   
              English_Grade.set("C2")
       elif(E <= 40  and E >= 33):   
              English_Grade.set("D")
       else:
              English_Grade.set("F")
              
       # It Display the Garde of Hindi according to Marks
       if(H <= 100  and H >= 91):
              Hindi_Grade.set("A1")
       elif(H <= 90  and H >= 81):  
              Hindi_Grade.set("A2")
       elif(H <= 80  and H >= 71):   
              Hindi_Grade.set("B1")
       elif(H <= 70  and H >= 61): 
              Hindi_Grade.set("B2")
       elif(H <= 60  and H >= 51):   
              Hindi_Grade.set("C1")
       elif(H <= 50  and H >= 41):   
              Hindi_Grade.set("C2")
       elif(H <= 40  and H >= 33):   
              Hindi_Grade.set("D")
       else:
              Hindi_Grade.set("F")
       
       # It Display the Division according to Marks
       if(Per >= 75):
              Division.set("Dictinction")
       elif(Per < 75 and Per > 60):
              Division.set("FIRST")
       elif(Per < 60 and Per > 50):
              Division.set("SECOND")
       elif(Per < 50 and Per > 40):
              Division.set("THIRD")
       else:
              Division.set("FAIL")
              
# It Copy the root window data into root1 window
def save():
       root1 = Tk()
       root1.title("STUDENT REPORT CARD")
       root1.iconbitmap("D:/PYTHON MODULES/TKINTER/TKINTER PROJECTS/ICONs/Student.ico")
       root1.config(bg = "khaki1")
       root1.geometry("1355x700+0+0")
       
       # Create a PanedWindow for Student Details
       PanedWindow(root1, width = 1200, height = 290, bg = "khaki1", relief = GROOVE, bd = 10).place(x = 90, y = 20)
       
       # Create the Labels for Student Details
       Label(root1, text = "Student Details", font = ("Arial 30 bold underline"),bg = "khaki1").place(x = 550, y = 00)
       Label(root1, text = "Name:",           font = ("Arial 17 bold"),bg = "khaki1").place(x = 120, y = 60)
       Label(root1, text = "Roll Number:",    font = ("Arial 17 bold"),bg = "khaki1").place(x = 715, y = 60)
       Label(root1, text = "Father Name:",    font = ("Arial 17 bold"),bg = "khaki1").place(x = 120, y = 105)
       Label(root1, text = "Mother Name:",    font = ("Arial 17 bold"),bg = "khaki1").place(x = 715, y = 105)
       Label(root1, text = "School Name:",    font = ("Arial 17 bold"),bg = "khaki1").place(x = 120, y = 155)
       Label(root1, text = "Class:",          font = ("Arial 17 bold"),bg = "khaki1").place(x = 715, y = 155)
       Label(root1, text = "Date of Birth:",  font = ("Arial 17 bold"),bg = "khaki1").place(x = 120, y = 205)
       Label(root1, text = "Gender:",         font = ("Arial 17 bold"),bg = "khaki1").place(x = 715, y = 205)
       Label(root1, text = "Phone:",          font = ("Arial 17 bold"),bg = "khaki1").place(x = 120, y = 255)
       Label(root1, text = "Email:",          font = ("Arial 17 bold"),bg = "khaki1").place(x = 715, y = 255)
       
       # Here we get the Output of Student Details from root window
       Label(root1, text = Name.get(),         font = ("Arial 18 bold"),bg = "khaki1", fg = "mediumblue").place(x = 325, y = 60)
       Label(root1, text = Roll_num.get(),     font = ("Arial 18 bold"),bg = "khaki1", fg = "mediumblue").place(x = 920, y = 60)
       Label(root1, text = Mr.get(),           font = ("Arial 18 bold"),bg = "khaki1", fg = "mediumblue").place(x = 325, y = 105)
       Label(root1, text = F_name.get(),       font = ("Arial 18 bold"),bg = "khaki1", fg = "mediumblue").place(x = 370, y = 105)
       Label(root1, text = Mrs.get(),          font = ("Arial 18 bold"),bg = "khaki1", fg = "mediumblue").place(x = 920, y = 105)
       Label(root1, text = M_name.get(),       font = ("Arial 18 bold"),bg = "khaki1", fg = "mediumblue").place(x = 976, y = 105)
       Label(root1, text = School_name.get(),  font = ("Arial 18 bold"),bg = "khaki1", fg = "mediumblue").place(x = 325, y = 155)
       Label(root1, text = Class.get(),        font = ("Arial 18 bold"),bg = "khaki1", fg = "mediumblue").place(x = 920, y = 155)
       Label(root1, text = date.get(),         font = ("Arial 18 bold"),bg = "khaki1", fg = "mediumblue").place(x = 325, y = 205)
       Label(root1, text = "-",                font = ("Arial 18 bold"),bg = "khaki1").place(x = 358, y = 205)
       Label(root1, text = month.get(),        font = ("Arial 18 bold"),bg = "khaki1", fg = "mediumblue").place(x = 375, y = 205)
       Label(root1, text = "-",                font = ("Arial 18 bold"),bg = "khaki1").place(x = 510, y = 205)
       Label(root1, text = year.get(),         font = ("Arial 18 bold"),bg = "khaki1", fg = "mediumblue").place(x = 530, y = 205)
       Label(root1, text = gender.get(),       font = ("Arial 18 bold"),bg = "khaki1", fg = "mediumblue").place(x = 920, y = 205)
       Label(root1, text = Country_code.get(), font = ("Arial 18 bold"),bg = "khaki1").place(x = 325, y = 255)
       Label(root1, text = Phone.get(),        font = ("Arial 18 bold"),bg = "khaki1", fg = "mediumblue").place(x = 380, y = 255)
       Label(root1, text = Email.get(),        font = ("Arial 18 bold"),bg = "khaki1", fg = "mediumblue").place(x = 920, y = 255)
       
       # Create a PanedWindow for Student Result
       PanedWindow(root1, width = 1200, height = 360, bg = "khaki1", relief = GROOVE, bd = 10).place(x = 90, y = 330)
       
       # Create the Labels for Student Result
       Label(root1, text = "Student Grades", font = ("Arial 30 bold underline"),bg = "khaki1").place(x = 550, y = 310)
       Label(root1, text = "SUBJECTS",       font = ("Arial 18 bold underline"),bg = "khaki1").place(x = 160, y = 370)
       Label(root1, text = "MATHEMATICS",    font = ("Arial 15 bold"),bg = "khaki1").place(x = 147, y = 420)
       Label(root1, text = "CHEMISTRY",      font = ("Arial 15 bold"),bg = "khaki1").place(x = 160, y = 460)
       Label(root1, text = "PHYSICS",        font = ("Arial 15 bold"),bg = "khaki1").place(x = 165, y = 500)
       Label(root1, text = "ENGLISH",        font = ("Arial 15 bold"),bg = "khaki1").place(x = 165, y = 540)
       Label(root1, text = "HINDI",          font = ("Arial 15 bold"),bg = "khaki1").place(x = 175, y = 580)
       Label(root1, text = "GRAND TOTAL:-",  font = ("Arial 18 bold underline"),bg = "khaki1").place(x = 130, y = 630)
       Label(root1, text = "MARKS OBTAINED", font = ("Arial 18 bold underline"),bg = "khaki1").place(x = 350, y = 370)
       Label(root1, text = "TOTAL MARKS",    font = ("Arial 18 bold underline"),bg = "khaki1").place(x = 600, y = 370)
       Label(root1, text = "GRADE",          font = ("Arial 18 bold underline"),bg = "khaki1").place(x = 800, y = 370)
       Label(root1, text = "PERCENTAGE",     font = ("Arial 18 bold underline"),bg = "khaki1").place(x = 910, y = 370)
       Label(root1, text = "CGPA",           font = ("Arial 18 bold underline"),bg = "khaki1").place(x = 952, y = 495)
       Label(root1, text = "DIVISION:-",     font = ("Arial 18 bold underline"),bg = "khaki1").place(x = 790, y = 628)
       
       # Set the Maximum Marks as 100 in the root1 window
       Label(root1, text = "100", font = ("Arial 17 bold"),bg = "khaki1").place(x = 660, y = 420)
       Label(root1, text = "100", font = ("Arial 17 bold"),bg = "khaki1").place(x = 660, y = 460)
       Label(root1, text = "100", font = ("Arial 17 bold"),bg = "khaki1").place(x = 660, y = 500)
       Label(root1, text = "100", font = ("Arial 17 bold"),bg = "khaki1").place(x = 660, y = 540)
       Label(root1, text = "100", font = ("Arial 17 bold"),bg = "khaki1").place(x = 660, y = 580)
       Label(root1, text = "500", font = ("Arial 20 bold"),bg = "khaki1").place(x = 657, y = 630)
       
       # Here we get the Output of Marks, Percentage, CGPA, Division, Grades from root window
       Label(root1, text = Maths.get(),           font = ("Arial 16 bold"),bg = "khaki1", fg = "mediumblue").place(x = 430, y = 420)
       Label(root1, text = Chemistry.get(),       font = ("Arial 16 bold"),bg = "khaki1", fg = "mediumblue").place(x = 430, y = 460)
       Label(root1, text = Physics.get(),         font = ("Arial 16 bold"),bg = "khaki1", fg = "mediumblue").place(x = 430, y = 500)
       Label(root1, text = English.get(),         font = ("Arial 16 bold"),bg = "khaki1", fg = "mediumblue").place(x = 430, y = 540)
       Label(root1, text = Hindi.get(),           font = ("Arial 16 bold"),bg = "khaki1", fg = "mediumblue").place(x = 430, y = 580)
       Label(root1, text = Grand_total.get(),     font = ("Arial 18 bold"),bg = "khaki1", fg = "mediumblue").place(x = 422, y = 630)
       Label(root1, text = Maths_Grade.get(),     font = ("Arial 16 bold"),bg = "khaki1", fg = "mediumblue").place(x = 830, y = 420)
       Label(root1, text = Chemistry_Grade.get(), font = ("Arial 16 bold"),bg = "khaki1", fg = "mediumblue").place(x = 830, y = 460)
       Label(root1, text = Physics_Grade.get(),   font = ("Arial 16 bold"),bg = "khaki1", fg = "mediumblue").place(x = 830, y = 500)
       Label(root1, text = English_Grade.get(),   font = ("Arial 16 bold"),bg = "khaki1", fg = "mediumblue").place(x = 830, y = 540)
       Label(root1, text = Hindi_Grade.get(),     font = ("Arial 16 bold"),bg = "khaki1", fg = "mediumblue").place(x = 830, y = 580)
       Label(root1, text = Percentage.get(),      font = ("Arial 25 bold"),bg = "khaki1", fg = "mediumblue").place(x = 955, y = 420)
       Label(root1, text = CGPA.get(),            font = ("Arial 25 bold"),bg = "khaki1", fg = "mediumblue").place(x = 965, y = 545)
       Label(root1, text = Division.get(),        font = ("Arial 20 bold"),bg = "khaki1", fg = "mediumblue").place(x = 930, y = 628)
       
# Define a Function for validate Roll Number, Phone and All integaers Values
def valid(char):
   if char.isdigit():
      return True
   else:
      return False
valid_num = (root.register(valid), '%P')

# Define a Function for Reset the all values When we Press the Reset Button
def reset():
       Name.set("")
       Roll_num.set("")
       F_name.set("")
       M_name.set("")
       School_name.set("")
       Class.set("Select Class")
       date.set("1")
       month.set("January")
       year.set("2021")
       gender.set("Select Gender")
       Phone.set("")
       Email.set("")
       Maths.set("")
       Chemistry.set("")
       Physics.set("")
       English.set("")
       Hindi.set("")
       Grand_total.set("")
       Maths_Grade.set("")
       Chemistry_Grade.set("")
       Physics_Grade.set("")
       English_Grade.set("")
       Hindi_Grade.set("")
       Percentage.set("")
       Division.set("")
       CGPA.set("")

# Crete a PanedWindow for Student Details in root window
PanedWindow(root, width = 1200, height = 290, bg = "steelblue2", relief = GROOVE, bd = 10).place(x = 90, y = 20)

# Create the Labels for root window
Label(root, text = "Student Details", font = ("Arial 30 bold"), bg = "steelblue2").place(x = 550, y = 00)
Label(root, text = "Name:",           font = ("Arial 17 bold"), bg = "steelblue2").place(x = 120, y = 60)
Label(root, text = "Roll Number:",    font = ("Arial 17 bold"), bg = "steelblue2").place(x = 715, y = 60)
Label(root, text = "Father Name:",    font = ("Arial 17 bold"), bg = "steelblue2").place(x = 120, y = 105)
Label(root, text = "Mother Name:",    font = ("Arial 17 bold"), bg = "steelblue2").place(x = 715, y = 105)
Label(root, text = "School Name:",    font = ("Arial 17 bold"), bg = "steelblue2").place(x = 120, y = 155)
Label(root, text = "Class:",          font = ("Arial 17 bold"), bg = "steelblue2").place(x = 715, y = 155)
Label(root, text = "Date of Birth:",  font = ("Arial 17 bold"), bg = "steelblue2").place(x = 120, y = 205)
Label(root, text = "Gender:",         font = ("Arial 17 bold"), bg = "steelblue2").place(x = 715, y = 205)
Label(root, text = "Phone:",          font = ("Arial 17 bold"), bg = "steelblue2").place(x = 120, y = 255)
Label(root, text = "Email:",          font = ("Arial 17 bold"), bg = "steelblue2").place(x = 715, y = 255)

Name = StringVar()            # Get the Input from user for Name 
Entry(root, textvariable = Name, font = ("Arial 15 bold"), width = 30).place(x = 325, y = 60)

Roll_num = StringVar()        # Get the Input from user for Roll_num 
Entry(root, textvariable = Roll_num, validate = "key", validatecommand = valid_num, font = ("Arial 15 bold"), width = 30).place(x = 920, y = 60)


Mr = StringVar()              # Set the Personal Title for Father_name
Mr.set("Mr.")
Entry(root, textvariable = Mr, font = ("Arial 15 bold"), state = "readonly", width = 4).place(x = 325, y = 105)

F_name = StringVar()          # Get the Input from user for Father_name 
Entry(root, textvariable = F_name, font = ("Arial 15 bold"), width = 25).place(x = 380, y = 105)


Mrs = StringVar()             # Set the Personal Title for Mother_name
Mrs.set("Mrs.")
Entry(root, textvariable = Mrs, font = ("Arial 15 bold"), state = "readonly", width = 4).place(x = 920, y = 105)

M_name = StringVar()          # Get the Input from user for Mother_name 
Entry(root, textvariable = M_name, font = ("Arial 15 bold"), width = 25).place(x = 975, y = 105)

School_name = StringVar()     # Get the Input from user for School_name 
Entry(root, textvariable = School_name, font = ("Arial 15 bold"), width = 30).place(x = 325, y = 155)

Class = [i for i in range(1,13)]       # It gives the Options to Select Classes from 1 to 12 in the Class Entry
Class = ttk.Combobox(root, value = Class, font = ("Arial 15 bold"), state = "readonly")
Class.set("Select Class")
Class.place(x = 920, y = 155)

date = [i for i in range(1,32)]        #  It gives the Options to Select Dates from 1 to 31 in the Date Entry
date = ttk.Combobox(root, value = date, font = ("Arial 15 bold"), state = "readonly", width = 3)
date.set("1")
date.place(x = 325, y = 205)

#  It gives the Options to Select Month in the Month Entry
month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
month = ttk.Combobox(root, value = month, font = ("Arial 15 bold"), state = "readonly", width = 12)
month.set("January")
month.place(x = 398, y = 205)

year = [i for i in range(1981, 2022)]        # It gives the Options to Select Year the Year Entry
year = ttk.Combobox(root, value = year, font = ("Arial 15 bold"), state = "readonly", width = 6)
year.set("2021")
year.place(x = 570, y = 205)

gender = ['Male', 'Female']      # It gives the Options to Select Gender either Male or Female in Gender Entry
gender = ttk.Combobox(root, value = gender, font = ("Arial 15 bold"), state = "readonly")
gender.set("Select Gender")
gender.place(x = 920, y = 205)

Country_code = StringVar()      # Set the Country code as +91 for INDIA in the Country_code Entry for Phone Numbers
Country_code.set("+91")
Entry(root, textvariable = Country_code, font = ("Arial 15 bold"), state = "readonly", width = 4).place(x = 325, y = 255)

Phone = StringVar()             # Get the Input from user for Phone 
Entry(root, textvariable = Phone, validate = "key", validatecommand = valid_num, font = ("Arial 15 bold"), width = 25).place(x = 380, y = 255)

Email = StringVar()             # Get the Input from user for Email 
Entry(root, textvariable = Email, font = ("Arial 15 bold"), width = 30).place(x = 920, y = 255)

# Crete a PanedWindow for Student Result in root window
PanedWindow(root, width = 1200, height = 360, bg = "steelblue2", relief = GROOVE, bd = 10).place(x = 90, y = 330)

# Crete the Labels for Student Result in root window
Label(root, text = "Student Grades", font = ("Arial 30 bold"), bg = "steelblue2").place(x = 550, y = 310)
Label(root, text = "SUBJECTS",      font = ("Arial 18 bold underline"), bg = "steelblue2").place(x = 160, y = 370)
Label(root, text = "MATHEMATICS",   font = ("Arial 15 bold"), bg = "steelblue2").place(x = 147, y = 420)
Label(root, text = "CHEMISTRY",     font = ("Arial 15 bold"), bg = "steelblue2").place(x = 160, y = 460)
Label(root, text = "PHYSICS",       font = ("Arial 15 bold"), bg = "steelblue2").place(x = 165, y = 500)
Label(root, text = "ENGLISH",       font = ("Arial 15 bold"), bg = "steelblue2").place(x = 165, y = 540)
Label(root, text = "HINDI",         font = ("Arial 15 bold"), bg = "steelblue2").place(x = 175, y = 580)
Label(root, text = "GRAND TOTAL:-", font = ("Arial 18 bold underline"), bg = "steelblue2").place(x = 130, y = 630)
Label(root, text = "MARKS OBTAINED", font = ("Arial 18 bold underline"), bg = "steelblue2").place(x = 350, y = 370)

Maths = IntVar()              # Get the Input from user for Mathematics Marks 
Maths.set("")
Entry(root, textvariable = Maths, validate = "key", validatecommand = valid_num, font = ("Arial 15 bold"), width = 5).place(x = 430, y = 420)

Chemistry = IntVar()          # Get the Input from user for Chemistry Marks 
Chemistry.set("")
Entry(root, textvariable = Chemistry, validate = "key", validatecommand = valid_num, font = ("Arial 15 bold"), width = 5).place(x = 430, y = 460)

Physics = IntVar()            # Get the Input from user for Physics Marks 
Physics.set("")
Entry(root, textvariable = Physics, validate = "key", validatecommand = valid_num, font = ("Arial 15 bold"), width = 5).place(x = 430, y = 500)

English = IntVar()            # Get the Input from user for English Marks 
English.set("")
Entry(root, textvariable = English, validate = "key", validatecommand = valid_num, font = ("Arial 15 bold"), width = 5).place(x = 430, y = 540)

Hindi = IntVar()              # Get the Input from user for Hindi Marks 
Hindi.set("")
Entry(root, textvariable = Hindi, validate = "key", validatecommand = valid_num, font = ("Arial 15 bold"), width = 5).place(x = 430, y = 580)

Grand_total = IntVar()        # Display the Grand Total of Marks of All Subjects  
Grand_total.set("")
Entry(root, textvariable = Grand_total, font = ("Arial 18 bold"), width = 5, state = "readonly").place(x = 425, y = 630)

# Create a Label for Total Marks in the root window
Label(root, text = "TOTAL MARKS", font = ("Arial 18 bold underline"), bg = "steelblue2").place(x = 600, y = 370)
Total_marks = StringVar()      # Set the Maximum Marks as 100 in the root window
Total_marks.set("100")
Entry(root, textvariable = Total_marks, font = ("Arial 15 bold"), width = 5, state = "readonly").place(x = 660, y = 420)
Entry(root, textvariable = Total_marks, font = ("Arial 15 bold"), width = 5, state = "readonly").place(x = 660, y = 460)
Entry(root, textvariable = Total_marks, font = ("Arial 15 bold"), width = 5, state = "readonly").place(x = 660, y = 500)
Entry(root, textvariable = Total_marks, font = ("Arial 15 bold"), width = 5, state = "readonly").place(x = 660, y = 540)
Entry(root, textvariable = Total_marks, font = ("Arial 15 bold"), width = 5, state = "readonly").place(x = 660, y = 580)
Grand_Total = IntVar()
Grand_Total.set("500")
Entry(root, textvariable = Grand_Total, font = ("Arial 18 bold"), width = 5, state = "readonly").place(x = 655, y = 630)

# Create a Label for Grades in the root window
Label(root, text = "GRADE", font = ("Arial 18 bold underline"), bg = "steelblue2").place(x = 800, y = 370)
Maths_Grade = StringVar()          # Display the Grade of Mathematics according to Marks
Entry(root, textvariable = Maths_Grade, font = ("Arial 15 bold"), width = 5, state = "readonly").place(x = 830, y = 420)

Chemistry_Grade = StringVar()      # Display the Grade of Chemistry according to Marks
Entry(root, textvariable = Chemistry_Grade, font = ("Arial 15 bold"), width = 5, state = "readonly").place(x = 830, y = 460)

Physics_Grade = StringVar()        # Display the Grade of Physics according to Marks
Entry(root, textvariable = Physics_Grade, font = ("Arial 15 bold"), width = 5, state = "readonly").place(x = 830, y = 500)

English_Grade = StringVar()        # Display the Grade of English according to Marks
Entry(root, textvariable = English_Grade, font = ("Arial 15 bold"), width = 5, state = "readonly").place(x = 830, y = 540)

Hindi_Grade = StringVar()          # Display the Grade of Hindi according to Marks
Entry(root, textvariable = Hindi_Grade, font = ("Arial 15 bold"), width = 5, state = "readonly").place(x = 830, y = 580)

# Create a Label for Percentage in the root window
Label(root, text = "PERCENTAGE", font = ("Arial 18 bold underline"), bg = "steelblue2").place(x = 910, y = 370)
Percentage = StringVar()           # Display the Percentage according to Grand Total
Entry(root, textvariable = Percentage, font = ("Arial 20 bold"), width = 6, state = "readonly").place(x = 945, y = 420, height = 50)

# Create a Label for CGPA in the root window
Label(root, text = "CGPA", font = ("Arial 18 bold underline"), bg = "steelblue2").place(x = 952, y = 495)
CGPA = StringVar()                 # Display the CGPA according to Percentage
Entry(root, textvariable = CGPA, font = ("Arial 20 bold"), width = 6, state = "readonly").place(x = 942, y = 545, height = 50)

# Create a Label for Division in the root window
Label(root, text = "DIVISION:-", font = ("Arial 18 bold underline"), bg = "steelblue2").place(x = 790, y = 628)
Division = StringVar()             # Display the Division according to Percentage
Entry(root, textvariable = Division, font = ("Arial 18 bold"), width = 10, state = "readonly").place(x = 930, y = 623, height = 40)

# Create a Button for Calculate the Result in the root window
Button(root, text = "CALCULATE", font = ("Arial 18 bold"), command = calculate_marks, bg = "greenyellow",
       activebackground = "olivedrab2", width = 10, bd = 5).place(x = 1100, y = 370) 

# Create a Button for Reset the All Entries in the root window
Button(root, text = "RESET", font = ("Arial 18 bold"), command = reset, bg = "orange",
       activebackground = "sienna2", bd = 5).place(x = 1130, y = 450) 

# Create a Button to Save the Result and Display the Result in the root1 window 
Button(root, text = "SAVE", font = ("Arial 18 bold"), command = save, bg = "palegreen2",
       activebackground = "yellowgreen", bd = 5).place(x = 1138, y = 530) 

# Create a Button for Exit from the root window
Button(root, text = "EXIT", font = ("Arial 18 bold"), command = exit, bg = "tomato2",
       activebackground = "coral2", bd = 5).place(x = 1143, y = 610) 

root.mainloop()
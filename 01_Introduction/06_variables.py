# This code created by codingwithamar@gmail.com
# Path : python_system_programming/introduction/06_variables.py
'''
Subject : Variables in Python
'''

print('''Defination : A variable is a named memory location used to store data values in a Python program.
Variables allow us to store, modify, and retrieve data during program execution.''')
print("Syntax : variable_name = value\n")

print("Types of Variables(By DataTypes)")
"""Varibale Creation and initialization"""
no = 11 #Considered as a integer variables
name = "Sarvadnya"  #Considered as a string variables
float_value = 3.14   #Considered as float varibales varibles
complex_value = 5e20   #Considered as complex value varibales
is_student = True      #Considered as a Boolean Varibales
print(no)
print(name)
print(float_value)
print(complex_value)
print(is_student)

print("\nTypes of Varibales(By Scope)")
print("1.Local Varibales")
def displayLocal():     #function Defination
    name = "name is a local varibale used only inside displayLocal function"    #Local Variables
    print(name)
displayLocal()

print("\n2.Global Variables")
surname = "surname is a global variables access any function of program"    #Declaired globally, access whole program

def displayGlobal():    #function Defination
    print(surname)
displayGlobal()

print("\nVALID VARIABLES")
print("Kranti")
print("jyoti")
print("_year")
print("Teacher1")
print("total_2family_Members")
print("SHALA")

print("\nINVALID VARIABLES")
print("1name    -   #Start with number")
print("student-name     -   #conatain '-'")
print("class    -   #keyword not allowed")

print("\nEXAMPLES")
print("Single Value Assign")
name = "KrantiJyoti"
year = "1930"
print("Name : ",name)
print("Year : ",year)

print("\nMultiple Value Assign")
firstName, middleName, surName = "AMAR", "BHARAT", "BHANDARE"
print(firstName, middleName, surName, sep="-")

print("\nAssign Same Value to Multiple Variables")
x = y = z = 1000
print(x, y, z)
# This code created by codingwithamar@gmail.com
# Path : python_system_programming/introduction/07_input_output.py
'''
Subject : Input and Output In Python
'''

print("Defination : Input means taking data from the user, and Output means displaying data to the user.")
print('''input() → for taking input     print() → for displaying output''')
print("Syntax : variable = input('Message')\n")

#End of input
value = input()
print(value)        #EOFError   

#Simple Input
name = input("Enter your pet name :")       #Enter your name: Amar
print("Your Pet Name is : ",name)           #Amar   #Python Stored name = "Amar"

#Problem Without Type Casting
age = input("Enter age: ")
print(age + 10)     #Type Error #Python Sense "20" + 10
#Correct Way
age = int(input("Enter age: "))     #Enter age: 20
print(age + 10)                     #30

#Using Float
salary = float(input("Enter salary: "))     #Enter salary: 45000.50
print(salary)                               #45000.5

#Taking Multiple Values in One Line
a, b = input("Enter two numbers: ").split()
print(a)
print(b)

#Multiple Integers
a, b = map(int, input("Enter two numbers: ").split())
print(a + b)


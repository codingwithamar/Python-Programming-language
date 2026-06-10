# This code created by codingwithamar@gmail.com
# Path : python_system_programming/introduction/08_type_casting.py
'''
Subject : Type Casting in Python
'''

print('''Defination : Type Casting is the process of converting one data type into another data type.
Python provides built-in functions to convert data from one type to another.''')

print("\nWhy Type Casting is Needed?")
print("The input() function always returns a string.")
age = input("Enter age(Enter Number/integer) : ")
print("\n",type(age))
print("\n We Enter Integer but output show 'str', To perform numeric operations, we must convert the string into an integer or float, inshort 'TypeCasting'\n")

print("Types of Type Casting")

print("1. Implicit Type Casting")
a = 10
b = 1.9

result = a + b

print("A (int) = ",a)
print("B (float) = ",b)
print("Result (float) : ",result)   #Python automatically converts int to float.
print("\nResult data type is : ", type(result))
print("\n#Python automatically converts one data type into another that is called Implicit Data Casting")

print("\n2. Explicit Type Casting")
num = "100"
print("num(str) = ",num)
print("\nnum data type before casting : ",type(num))
num = int(num)  #explicit type casting
print("\nnum data type after casting : ",type(num))
print("\nThe programmer manually converts the data type using built-in functions thats called 'Explicit Type Casting'\n")

print("Convert string datatypes to another data types")
Value = "100"
print("\n\nBefore conversion Value(str) = ",Value)
print("----------After Conversion------------")
print(int(Value))
print(float(Value))
print(str(Value))
print(bool(Value))
print(complex(int(Value)))
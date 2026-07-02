# This code created by codingwithamar@gmail.com
# Path : python_system_programming/02_Data_Types/01_numeric_data_types.py
'''
Subject : Numeric Data types in Python(int, float, complex)
'''
print("Used to store numeric values.\n")

print("---------integer-----------")

#Whole numbers, positive or negative, with no size limit.
ivalue = 10
ivalue1 = -50
ivalue2 = 0
ivalue3 = 10_000_000   # underscores allowed for readability Underscores are ignored by Python.
big = 10 ** 100   # googol — no problem with big value

print("\nValue = ",ivalue)    #10
print("Value1 = ",ivalue1)  #-50
print("Value2 = ",ivalue2)  #0
print("Value3 = ",ivalue3)  #10_000_000
print("Big Value = ", big)        # 10000000000000000000000000000000000000000...

print(type(ivalue))   # <class 'int'>
print(type(ivalue1))   # <class 'int'>
print(type(ivalue3))   # <class 'int'>
print(type(ivalue2))   # <class 'int'>
print(type(big))   # <class 'int'>

print("\nNumeric objects cannot be modified after creation in old memory address python allocate new address space")
a = 10
print(id(a))

a = a + 5       
print(id(a))

print("\nArithmatic Operations Allow")
a1 = 15
b1 = 4

print(a1 + b1)  #19
print(a1 - b1)  #10
print(a1 * b1)  #60
print(a1 / b1)  #3.75
print(a1 // b1) #3
print(a1 % b1)  #3
print(a1 ** b1) #50625

print("\nConversion In Numerics")

binary  = 0b1010    # base 2  → 10  #Code - 0b
octal   = 0o12      # base 8  → 10  #Code - 0o
hexa    = 0xA       # base 16 → 10  #Code - 0xA

print("Conversion - \nIn Binary(0b1010) : ", binary, "\nIn Octal(0o12) : ", octal, "\nIn Hexa(0xA) : ", hexa)   # 10 10 10

print("\nCheck Type of Variable and get return in boolean")
x = 10
y = 10.34
z = "amar"
print(isinstance(x, int))   #True
print(isinstance(y, float)) #True
print(isinstance(z, float)) #False

#isinsitance() example
import numbers
print(isinstance(10, float))            #false
print(isinstance(10, numbers.Number))   # True
print(isinstance(3.14, numbers.Number)) # True

import numbers

isinsistancevalue = 25 #int
isinsistancevalue1 = 3.14  # float

print(isinstance(isinsistancevalue1, numbers.Number))    # True
print(isinstance(isinsistancevalue1, numbers.Complex))   # True
print(isinstance(isinsistancevalue1, numbers.Real))      # True
print(isinstance(isinsistancevalue1, numbers.Rational))  # False ← float is NOT rational
print(isinstance(isinsistancevalue1, numbers.Integral))  # False ← float is NOT integral

print(isinstance(isinsistancevalue, numbers.Number))    # True
print(isinstance(isinsistancevalue, numbers.Complex))   # True
print(isinstance(isinsistancevalue, numbers.Real))      # True
print(isinstance(isinsistancevalue, numbers.Rational))  # True
print(isinstance(isinsistancevalue, numbers.Integral))  # True

if isinstance(isinsistancevalue, (int, float)):
    print("Valid Number")
else:
    print("Invalid Number")

print("Conversion in numeric")
print(int(5.9))     #5
print(int("100"))   #100
print(int(True))    #1

#Invalid Conversions
#int("abc")      #ValueError
#int(3 + 4j)     #TypeError
print("\n isinstance vs type")
print(type(isinsistancevalue) == int)               # True  — exact type check
print(isinstance(isinsistancevalue, int))           # True  — also checks subclasses
print(isinstance(isinsistancevalue, numbers.Real))  # True  — works across hierarchy

print("\n---------float-------------")
value2 = 111.11 #Decimal Values Allowed
print("Value2 = ",value2)
print(type(value2))

print("\n---------complex-----------")
value3 = 2 + 3j #real + imaginary(j) Values Allowed
print("Value3 = ",value3)
print(type(value3))

print("\n--------Numeric Operation-----------")
a = 10
b = 3
print("A = ",a)
print("B = ",b)
print("Addition",a + b)   # Addition
print("Substraction", a - b)   # Subtraction
print("Multiplication", a * b)   # Multiplication
print("Division", a / b)   # Division
print("Modulus", a % b)   # Modulus

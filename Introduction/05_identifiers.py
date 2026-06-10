# This code created by codingwithamar@gmail.com
# Path : python_system_programming/introduction/05_identifiers.py

"""
Subject:
Identifiers are user-defined names used for variables,
functions, classes, modules, and other objects.
They cannot be Python keywords and must follow naming rules.
"""

# Variable Identifiers
name = "Amar"
age = 20

# Function Identifier
def display():
    pass

# Class Identifier
class Student:
    pass

print("=== Rule 1: Valid Identifiers ===")
print("\nExamples:")
print("student_name")
print("emp123")
print("total_marks")

print("\n=== Rule 2: Cannot Start With a Number ===")
# 1name = "Amar"   # Invalid
print("1name  -> Invalid")
print("name1  -> Valid")

print("\n=== Rule 3: Special Characters Not Allowed ===")
print("student-name  -> Invalid")
print("total@marks   -> Invalid")

print("\n=== Rule 4: Keywords Not Allowed ===")
print("class -> Invalid")
print("if    -> Invalid")

print("\n=== Rule 5: Case Sensitive ===")
Name = "Damini"
name = "Gauri"

print("Name =", Name)
print("name =", name)

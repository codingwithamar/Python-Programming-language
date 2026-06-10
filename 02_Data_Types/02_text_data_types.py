# This code created by codingwithamar@gmail.com
# Path : python_system_programming/02_Data_Types/02_text_data_types.py
'''
Subject : Text Data types in Python(str)
'''
print("The Text Data Type in Python is represented by the str (String) type, A string is a sequence of characters its initialized with single,double,triple quotes\n")

print("----------Using Single Quotes------------")
name = 'Amar'
print("Name = ", name)
print(type(name))

print("\n----------Using Double Quotes------------")
name = "Amar"
print("Name = ", name)
print(type(name))

print("\n----------Using Triple Quotes------------")
name = """I
            AM
                AMAR"""
print("Name = ", name)
print(type(name))

print("\n-------------------String Operation-------------------------")
print("-------Concatenation--------")
first_name = "Amar"
last_name = "Bhandare"
print(first_name + " " + last_name)

print("\n-----Repetation-----")
print("PYTHON "*3)


print("\n------Length of String-------")
name = "Amar"
print("NAME = ",name)
print(len(name))

print("\n------Indexing-------")
#Indexing See Below
#   A  m  a  r
#   0  1  2  3
name = "Amar"
print(name[0])
print(name[3])

print("\n------Slicing---------")
name = "Python"
print(name[0:3])

print("\n------Capitalization------")
Surname = "BhanDare"
print("Surname = ",Surname)
print(Surname.upper())
print(Surname.lower())
print(Surname.title())

fullName = "Amar bharat bhandare"
print(fullName.upper())
print(fullName.lower())
print(fullName.title())





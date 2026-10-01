# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : Attributes.py
# Path    : Python-Programming-Language/03_Variables in Python/Attributes.py
# Subject : Variables in Python
# Description : Attribute
# =============================================================================

class Student:
    def __init__(self, name, age):  #__init__ use for object initialization
        self.name = name
        self.age = age

def main():
    s1 = Student("Amar", 20)
    s2 = Student("Rahul", 21)

    print(s1.name)
    print(s2.age)

if __name__ == "__main__":
    main()
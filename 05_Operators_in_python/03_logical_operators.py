# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 03_logical_operators.py
# Path    : Python-Programming-Language/05_Operators_in_python/03_logical_operators.py
# Subject : Logical Operator
# Description : Combine conditions(and, or, not)
# =============================================================================

def main():
    Amar = 80
    Akshay = 100
    Hari = 80

    #AND : both condition True
    if 90 < Amar and Akshay:
        print("both Students marks greater than 90 ")
    else:
        print("Both students marks not greater than 90  ")

    #OR : Either one Condition is true
    if 90 < Amar or Akshay:
        print("both Students marks greater than 90 ")
    else:
        print("Both students marks not greater than 90 ")

    #not : Flipse True to False and False to True
    if not Hari > 90:
        print("hari's marks are not greater then 90")

if __name__ == "__main__":
    main()
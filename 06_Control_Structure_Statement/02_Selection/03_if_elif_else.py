# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 03_if_elif_else.py
# Path    : Python-Programming-Language/06_Control_Structure_Statement/02_Selection/03_if_elif_else.py
# Subject : Control Structure Statements - Selection
# Description : if-elif-else Statement
# =============================================================================

def main():
    Marks = 81

    if Marks >= 90:
        grade = 'A'
    elif Marks >= 65:
        grade = 'B'
    elif Marks >= 35:
        grade = 'C'
    else:
        grade = 'Fail'

    print(grade)

    #short hand Statement
    Mark = 18

    Short_hand_grade = 'A' if Mark >= 90 else 'B' if Mark >= 65 else 'C' if Mark >= 35 else 'Fail'

    print(Short_hand_grade)

if __name__ == "__main__":
    main()
# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 04_Nested_if.py
# Path    : Python-Programming-Language/06_Control_Structure_Statement/02_Selection/04_Nested_if.py
# Subject : Control Structure Statements - Selection
# Description : nested-if Statement
# =============================================================================

def main():
    age = 25
    citizen = 'Indian'

    if age >= 18:
        if citizen == 'Indian':
            print("Eligible for Vote")
    else:
        print("Not Eligible for Vote")
        
if __name__ == "__main__":
    main()
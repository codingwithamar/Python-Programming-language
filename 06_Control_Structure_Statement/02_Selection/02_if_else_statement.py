# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 02_if_else_statement.py
# Path    : Python-Programming-Language/06_Control_Structure_Statement/02_Selection/01_if_else_statement.py
# Subject :  Control Structure Statements - Selection
# Description : if else Statement
# =============================================================================

def main():
    age = 21

    if age >= 18:
        print("Adult")
    else:
        print("Minor")

    #Short Hand if-else Statement
    print("Adult") if age >= 18 else print("Minor")

if __name__ == "__main__":
    main()
# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 05_Logical_operators_in_conditions.py
# Path    : Python-Programming-Language/06_Control_Structure_Statement/02_Selection/05_Logical_operators_in_conditions.py
# Subject : Control Structure Statements - Selection
# Description : Logical operator in conditions
# =============================================================================

def main():
    age = 25
    salary = 50000
    #________________________________________________________________________________
    #						'and Operator'

    if age >= 18 and salary >= 30000:
        print("Condition satisfied")
    #________________________________________________________________________________
    
    #________________________________________________________________________________
    #						'or Operator'

    if age >= 18 or salary >= 30000:
        print("Condition satisfied")
    #________________________________________________________________________________
    
    #________________________________________________________________________________
    #						'not Operator'

    logged_in = False

    if not logged_in:
        print("Please login")
    #________________________________________________________________________________
    

if __name__ == "__main__":
    main()
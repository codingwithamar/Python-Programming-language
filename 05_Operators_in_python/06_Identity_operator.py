# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 06_Identity_operator.py
# Path    : Python-Programming-Language/05_Operators_in_python/06_Identity_operator.py
# Subject : Identity Operator
# Description : Identity operators in Python are used to check whether two variables 
# refer to the same object in memory, not whether they have the same value.( is, is not )
# =============================================================================

def main():

    a = [1, 2, 3]
    b = [1, 2, 3]
    c = a
    print(a == b)   # True  → values Same
    print(a is b)   # False → Different objects in memory
    print(a is c)   # True  → same object

if __name__ == "__main__":
    main()
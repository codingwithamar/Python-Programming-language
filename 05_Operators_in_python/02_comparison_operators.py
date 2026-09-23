# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 02_comparison_operators.py
# Path    : Python-Programming-Language/05_Operators_in_python/02_comparison_operators.py
# Subject : Comaprison Operators
# Description : compare two things, answer is True/False (==, !=, >, <, >=, <=)
# =============================================================================

from datetime import datetime

def main():
    x = 5
    y = 8
    print(x == y)   # False
    print(x != y)   # True
    print(x < y)    # True
    print(x > y)    # False
    print(x >= y)   # False
    print(x <= y)   # True

if __name__ == "__main__":
    main()
# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 2_min_BuiltIn_Function.py
# Path    : Python-Programming-Language/07_Functions_in_Python/02_Function_Categories/01_Built_in_functions/04_Calculations_builtIn_functions/2_Totals_Functions/2_min_BuiltIn_Function.py
# Subject : Built-in functions in python
# Description : min( ), max( ) - Return the smallest and the largest item.
# =============================================================================

def main():
    print("Syntax :\nmin(iterable, *, key=None, default=...)\nmin(a, b, c, ..., key=None)")

    print(min([4, 8, 1, 9]))      # 1
    print(max([4, 8, 1, 9]))      # 9
    print(min(5, 2, 8))           # 2 -> you can pass values directly
    print(max("apple", "banana")) # banana -> strings compare alphabetically

if __name__ == "__main__":
    main()
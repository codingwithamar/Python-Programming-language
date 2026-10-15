# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 13_format_BuiltIn_Function.py
# Path    : Python-Programming-Language/07_Functions_in_Python/02_Function_Categories/01_Built_in_functions/04_Calculations_builtIn_functions/3_Numbers_and_Unicodes_Functions/13_format_BuiltIn_Function.py
# Subject : Built-in functions in python
# Description : format() - Converts a value into a string using a format specification. 
# It is the same mini-language used inside f-strings after the colon.
# =============================================================================

def main():
    print("Syntax : format(value, format_spec='')")

    print(format(3.14159, ".2f"))     # 3.14
    print(format(42, "05d"))          # 00042
    print(format(1234567, ","))       # 1,234,567
    print(format(0.256, ".1%"))       # 25.6%
    print(format(255, "x"))           # ff
    print(format("hi", ">6"))         # "    hi" (right-aligned in 6 spaces)

if __name__ == "__main__":
    main()
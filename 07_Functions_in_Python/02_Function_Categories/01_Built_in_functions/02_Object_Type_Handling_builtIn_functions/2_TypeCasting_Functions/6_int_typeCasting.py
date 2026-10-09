# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 6_int_type_conversion.py
# Path    : Python-Programming-Language/07_Functions_in_Python/02_Function_Ctaegories/01_Built_in_functions/02_Object_Type_Handling_builtIn_functions/6_int_type_conversion.py
# Subject : TypeCasting Built-In functions
# Description : int() : Converts a value to an integer, or creates 0 with no arguments.
# =============================================================================

def main():
    print(int("25"))         # 25
    print(int(3.99))         # 3 -> truncates, does not round
    print(int())             # 0
    print(int("1010", 2))     # 10 -> parses "1010" as base 2 (binary)
    print(int("ff", 16))       # 255 -> parses "ff" as base 16 (hex)
    print(int("  42  "))       # 42 -> leading/trailing whitespace is ignored

    try:
        int("abc")
    except ValueError as e:
        print("Conversion failed:", e)

    try:
        int("3.5")             # fails -> int() cannot parse a decimal string directly
    except ValueError as e:
        print("Conversion failed:", e)

if __name__ == "__main__":
    main()
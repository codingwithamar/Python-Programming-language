# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 7_float_typeCasting.py
# Path    : Python-Programming-Language/07_Functions_in_Python/02_Function_Categories/01_Built_in_functions/02_Object_Type_Handling_builtIn_functions/TypeCasting Functions/7_float_typeCasting.py
# Subject : TypeCasting Built-In Functions
# Description : float() - Converts a value to a floating-point number.
# =============================================================================

def main():
    print(float("3.14"))       # 3.14
    print(float(5))              # 5.0
    print(float())                # 0.0
    print(float("inf"))          # inf -> represents infinity
    print(float("-inf"))         # -inf
    print(float("nan"))          # nan -> "Not a Number"

    x = float("nan")
    print(x)          # True -> special check needed, since nan != nan
    print(float("  2.5e3  "))    # 2500.0 -> supports scientific notation and whitespace

if __name__ == "__main__":
    main()
# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : round_BuiltIN_Function.py
# Path    : Python-Programming-Language/07_Functions_in_Python/02_Function_Categories/01_Built_in_functions/04_Calculations_builtIn_functions/1_Math_Functions/round_BuiltIN_Function.py
# Subject : Built-in functions in python
# Description : round() - Rounds a number to a given number of decimal places.
# =============================================================================

def main():
    print("Syntax :\nround(number)\nround(number, ndigits)")

    print(round(3.7))          # 4
    print(round(3.2))          # 3
    print(round(3.14159, 2))   # 3.14
    print(round(1234, -2))     
    # 1200 -> a negative number rounds to hundreds, thousands, etc.

    # 1. Python uses "round half to even" (also called banker's rounding)
    print(round(0.5))     # 0
    print(round(1.5))     # 2
    print(round(2.5))     # 2   -> not 3
    print(round(3.5))     # 4
    print(round(-2.5))    # -2
    # When the value is exactly halfway, it goes to the nearest EVEN number

    # 2. Return type
    print(round(5.7))         # 6    -> int (no ndigits given)
    print(round(5.0, 1))      # 5.0  -> float (ndigits given)

    # 3. Float storage can surprise you
    print(round(2.675, 2))    # 2.67, not 2.68
    # 2.675 is stored as 2.67499999... inside the computer

    # 4. For money, use Decimal and choose the rounding rule yourself
    from decimal import Decimal, ROUND_HALF_UP
    price = Decimal("2.675")
    print(price.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))   # 2.68

if __name__ == "__main__":
    main()
# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : pow_BuiltIN_Function.py
# Path    : Python-Programming-Language/07_Functions_in_Python/02_Function_Categories/01_Built_in_functions/04_Calculations_builtIn_functions/1_Math_Functions/pow_BuiltIN_Function.py
# Subject : Built-in functions in python
# Description : pow() - Raises a number to a power. It does the same job as the ** operator, with an extra option for modulo.
# =============================================================================

def main():
    print("Syntax:\npow(base, exp)\npow(base, exp, mod)")

    print(pow(2, 3))       # 8
    print(2 ** 3)          # 8 -> same result
    print(pow(2, -2))      # 0.25 -> negative power gives a float
    print(pow(9, 0.5))     # 3.0 -> square root

    # 1. Three-argument form: (base ** exp) % mod, calculated fast
    print(pow(2, 3, 5))        # 3, because 8 % 5 = 3

    # Very large numbers: this finishes instantly
    print(pow(3, 200, 13))     # 9
    # Doing (3 ** 200) % 13 builds a huge number first, which is slower

    # 2. Modular inverse (Python 3.8+): the number x where (base * x) % mod == 1
    print(pow(3, -1, 11))      # 4, because 3 * 4 = 12 and 12 % 11 = 1

    # 3. A negative base with a fractional power gives a complex number
    print(pow(-8, 1 / 3))      # a complex number, not -2.0

    # 4. Difference from math.pow
    import math
    print(pow(2, 3))           # 8   -> int stays int
    print(math.pow(2, 3))      # 8.0 -> math.pow always returns float

if __name__ == "__main__":
    main()
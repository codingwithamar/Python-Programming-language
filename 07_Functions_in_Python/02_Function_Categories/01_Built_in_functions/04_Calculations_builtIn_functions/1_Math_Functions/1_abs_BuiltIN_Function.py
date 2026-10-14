# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : abs_BuiltIN_Function.py
# Path    : Python-Programming-Language/07_Functions_in_Python/02_Function_Categories/01_Built_in_functions/04_Calculations_builtIn_functions/1_Math_Functions/abs_BuiltIN_Function.py
# Subject : Built-in functions in python
# Description : abs() - Returns the absolute value, which is the size of a number without its sign. 
# =============================================================================

def main():
    print(abs(-5))        # 5
    print(abs(-3.5))      # 3.5
    print(abs(7))         # 7
    print(abs(3 + 4j))    # 5.0 -> for complex numbers, it gives the magnitude

    # 1. Check if two numbers are close (the gap between them, ignoring sign)
    a = 100.0
    b = 100.4
    print(abs(a - b) < 0.5)       # True

    # 2. Better for floats: math.isclose
    import math
    print(0.1 + 0.2 == 0.3)               # False
    print(abs((0.1 + 0.2) - 0.3) < 1e-9)  # True
    print(math.isclose(0.1 + 0.2, 0.3))   # True

    # 3. Your own class can support abs() by defining __abs__
    class Vector:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def __abs__(self):
            return (self.x ** 2 + self.y ** 2) ** 0.5

    print(abs(Vector(3, 4)))      # 5.0

if __name__ == "__main__":
    main()
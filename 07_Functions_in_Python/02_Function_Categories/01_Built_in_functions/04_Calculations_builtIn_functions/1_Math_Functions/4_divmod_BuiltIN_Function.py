# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : divmod_BuiltIN_Function.py
# Path    : Python-Programming-Language/07_Functions_in_Python/02_Function_Categories/01_Built_in_functions/04_Calculations_builtIn_functions/1_Math_Functions/divmod_BuiltIN_Function.py
# Subject : Built-in functions in python
# Description : divmod() - Returns the quotient and the remainder together, as a tuple. divmod(a, b) is the same as (a // b, a % b).
# =============================================================================

def main():
    print(divmod(17, 5))     # (3, 2) -> 17 = 3 * 5 + 2

    quotient, remainder = divmod(17, 5)
    print(quotient, remainder)    # 3 2

    # 1. Convert seconds into hours, minutes, seconds
    def format_duration(total_seconds):
        minutes, seconds = divmod(total_seconds, 60)
        hours, minutes = divmod(minutes, 60)
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

    print(format_duration(3725))     # 01:02:05

    # 2. Negative numbers: the remainder takes the sign of the divisor
    print(divmod(-17, 5))      # (-4, 3), because -4 * 5 + 3 = -17
    print(divmod(17, -5))      # (-4, -3)

    # 3. Works with floats too
    print(divmod(7.5, 2))      # (3.0, 1.5)

    # 4. Dividing by zero raises an error
    # divmod(5, 0)   -> ZeroDivisionError

if __name__ == "__main__":
    main()
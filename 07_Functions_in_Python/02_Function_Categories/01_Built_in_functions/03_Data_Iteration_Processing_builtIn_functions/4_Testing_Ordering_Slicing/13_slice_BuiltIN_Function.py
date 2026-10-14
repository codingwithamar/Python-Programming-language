# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 13_slice_BuiltIN_Function.py
# Path    : Python-Programming-Language/07_Functions_in_Python/02_Function_Categories/01_Built_in_functions/03_Data_Iteration_Processing_builtIn_functions/4_Testing_Ordering_Slicing/13_slice_BuiltIN_Function.py
# Subject : Built-in functions in python
# Description : slice() - Creates a slice object that you can store in a variable and reuse. It is the same thing Python builds when you write x[1:4].
# =============================================================================

def main():
    print("slice(stop)\nslice(start, stop, step)")

    data = [10, 20, 30, 40, 50]

    s = slice(1, 4)
    print(data[s])          # [20, 30, 40]
    print(data[1:4])        # [20, 30, 40] -> same result

    print(data[slice(None, None, 2)])    # [10, 30, 50] -> same as data[::2]

    line = "2026-10-13 ERROR Disk full"

    DATE = slice(0, 10)
    LEVEL = slice(11, 16)
    MESSAGE = slice(17, None)

    print(line[DATE], line[LEVEL], line[MESSAGE], sep=" | ")
    # 2026-10-13 | ERROR | Disk full

if __name__ == "__main__":
    main()
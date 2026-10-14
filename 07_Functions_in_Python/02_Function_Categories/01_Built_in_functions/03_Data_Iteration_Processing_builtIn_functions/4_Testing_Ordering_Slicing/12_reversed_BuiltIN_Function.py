# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 12_reversed_BuiltIN_Function.py
# Path    : Python-Programming-Language/07_Functions_in_Python/02_Function_Categories/01_Built_in_functions/03_Data_Iteration_Processing_builtIn_functions/4_Testing_Ordering_Slicing/12_reversed_BuiltIN_Function.py
# Subject : Built-in functions in python
# Description : reversed() - Returns an iterator that goes through a sequence backwards.
# =============================================================================

def main():
    print(list(reversed([1, 2, 3])))      # [3, 2, 1]
    print("".join(reversed("hello")))     # olleh

    for i in reversed(range(3)):
        print(i)                          # 2 1 0

if __name__ == "__main__":
    main()
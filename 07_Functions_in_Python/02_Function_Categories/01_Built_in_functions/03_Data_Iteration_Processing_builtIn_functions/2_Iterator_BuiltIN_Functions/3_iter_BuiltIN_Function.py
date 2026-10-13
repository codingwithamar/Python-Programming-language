# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 3_iter_BuiltIN_Function.py
# Path    : Python-Programming-Language/07_Functions_in_Python/02_Function_Categories/01_Built_in_functions/03_Data_Iteration_Processing_builtIn_functions/1_Size_and_Number_Sequences/3_iter_BuiltIN_Function.py
# Subject : Built-in functions in python
# Description : iter() - Gets an iterator from an iterable. A for loop calls iter() for you behind the scenes.
# =============================================================================

def main():
    numbers = [10, 20, 30]
    it = iter(numbers)

    print(next(it))    # 10
    print(next(it))    # 20
    print(next(it))    # 30

if __name__ == "__main__":
    main()
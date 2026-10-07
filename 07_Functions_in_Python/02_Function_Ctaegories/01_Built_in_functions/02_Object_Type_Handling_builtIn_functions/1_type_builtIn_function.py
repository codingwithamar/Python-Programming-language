# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 01_type_function.py
# Path    : Python-Programming-Language/07_Functions_in_Python/02_Function_Ctaegories/01_Built_in_functions/01_type_function.py
# Subject : Built-in-function in Python
# Description : type() function - it used for see the data type of the function
# =============================================================================

def main():
    #________________________________________________________________________________
        #						        '1. type() function'
        # Basic type() example 1:
        x = 10
        print(type(x))          # <class 'int'>
        print(type(5))          # <class 'int'>
        print(type("hello"))    # <class 'str'>
        print(type([1, 2, 3]))  # <class 'list'>

        # %% Example 2: Validating input types before processing

        def process(value):
            if type(value) is list:
                return sum(value)
            elif type(value) is str:
                return value.upper()
            return value
    
        print(process([1, 2, 3]))   # 6
        print(process("hello"))     # HELLO
        #________________________________________________________________________________

if __name__ == "__main__":
    main()
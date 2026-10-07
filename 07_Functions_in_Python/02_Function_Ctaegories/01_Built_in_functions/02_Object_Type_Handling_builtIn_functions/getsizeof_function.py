# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 05_getsizeof_function.py
# Path    : Python-Programming-Language/07_Functions_in_Python/02_Function_Ctaegories/01_Built_in_functions/05_getsizeof_function.py
# Subject : Built-in functions in python
# Description : The getsizeof( ) : function returns the memory size(in bytes) occupied by an object.
# =============================================================================

import sys

def main():
    x = 10
    print(sys.getsizeof(x))


if __name__ == "__main__":
    main()
# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : convertor.py
# Path    : Python-Programming-Language/08_Modules_And_Packages_In_Python/3_Use_of_Modules/convertor.py
# Subject : Modules and Packages in Python
# Description : Modules / Use of Modules(Supoorting File of 2_Use_of_Modules.py)
# =============================================================================

"""Temperature tools."""

__all__ = ["c_to_f", "f_to_c"]      # names exported by "from converter import *"

print("converter loaded")           # runs only on the first import

def c_to_f(c):
    return c * 9 / 5 + 32

def f_to_c(f):
    return (f - 32) * 5 / 9

def _round2(x):                     # leading underscore: private helper
    return round(x, 2)

if __name__ == "__main__":          # runs only when this file is run directly
    print(c_to_f(100))
    print(f_to_c(212))

'''
OUTPUT :
converter loaded
212.0
100.0
'''
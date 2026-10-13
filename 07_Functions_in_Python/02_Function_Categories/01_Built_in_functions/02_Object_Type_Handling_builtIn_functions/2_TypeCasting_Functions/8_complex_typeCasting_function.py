# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 8_complex_typeCasting.py
# Path    : Python-Programming-Language/07_Functions_in_Python/02_Function_Categories/01_Built_in_functions/02_Object_Type_Handling_builtIn_functions/TypeCasting Functions/8_complex_typeCasting.py
# Subject : TypeCasting Built-In Functions
# Description : complex() - Creates a complex number with a real and imaginary part.
# =============================================================================

def main():
    c1 = complex(2, 3)        # 2 + 3j
    c2 = complex("4+5j")       # parsed from a string
    print(c1, c2)
    
    c = complex(3, 4)
    print(c.real)         # 3.0
    print(c.imag)          # 4.0
    print(abs(c))           # 5.0 -> magnitude: sqrt(real^2 + imag^2)
    print(c.conjugate())    # (3-4j)

if __name__ == "__main__":
    main()
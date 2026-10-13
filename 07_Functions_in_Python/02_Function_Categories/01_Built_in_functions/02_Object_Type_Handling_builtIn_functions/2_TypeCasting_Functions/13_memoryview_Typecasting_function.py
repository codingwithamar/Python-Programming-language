# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 13_memoryview_Typecasting.py
# Path    : Python-Programming-Language/07_Functions_in_Python/02_Function_Categories/01_Built_in_functions/02_Object_Type_Handling_builtIn_functions/TypeCasting Functions/13_memoryview_Typecasting.py
# Subject : Typecasting Built-In Function
# Description : memoryview() - Creates a view into another object’s memory buffer without copying the data. Mainly used with bytes/bytearray for performance-sensitive operations. 
# =============================================================================

def main():
    data = bytearray(b"hello world")
    mv = memoryview(data)
    print(mv[0:5])             # <memory at ...>
    print(bytes(mv[0:5]))       # b'hello'

    data = bytearray(b"0123456789")
    mv = memoryview(data)

    # Modify the original data through the memoryview, with no extra copy
    mv[0:3] = b"ABC"
    print(data)       # bytearray(b'ABC3456789')


if __name__ == "__main__":
    main()
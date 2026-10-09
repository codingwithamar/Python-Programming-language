# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 12_bytearray_typeCasting.py
# Path    : Python-Programming-Language/07_Functions_in_Python/02_Function_Categories/01_Built_in_functions/02_Object_Type_Handling_builtIn_functions/TypeCasting Functions/12_bytearray_typeCasting.py
# Subject : TypeCasting Built-In Functions
# Description : bytearray() - Like bytes(), but mutable — you can change individual byte values after creation.
# =============================================================================

def main():
    ba = bytearray("hello", "utf-8")
    print(ba)              # bytearray(b'hello')

    ba = bytearray(b"hello")
    ba[0] = 72                # change 'h' (104) to 'H' (72)
    print(ba)                 # bytearray(b'Hello')
    print(ba.decode("utf-8")) # Hello

    # Building binary data incrementally
    buffer = bytearray()
    buffer.extend(b"part1-")
    buffer.extend(b"part2")
    print(buffer)              # bytearray(b'part1-part2')

if __name__ == "__main__":
    main()
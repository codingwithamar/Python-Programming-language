# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 11_bytes_typeCasting.py
# Path    : Python-Programming-Language/07_Functions_in_Python/02_Function_Categories/01_Built_in_functions/02_Object_Type_Handling_builtIn_functions/TypeCasting Functions/11_bytes_typeCasting.py
# Subject : TypeCasting BUilt-In Functions
# Description : bytes() - Creates an immutable sequence of bytes. 
# =============================================================================

def main():
    b1 = bytes("hello", "utf-8")      # encode a string into bytes
    b2 = bytes([65, 66, 67])            # from a list of integers (0-255)
    b3 = bytes(5)                        # 5 zero bytes

    print(b1, b2, b3)

    text = "hello"
    encoded = text.encode("utf-8")      # another common way to get bytes
    print(encoded)                        # b'hello'

    decoded = encoded.decode("utf-8")    # converting back to string
    print(decoded)                        # hello

    # Common in automation: reading binary file data
    with open("file.bin", "rb") as f:
        data = f.read()
        print(type(data))                 # <class 'bytes'>

if __name__ == "__main__":
    main()
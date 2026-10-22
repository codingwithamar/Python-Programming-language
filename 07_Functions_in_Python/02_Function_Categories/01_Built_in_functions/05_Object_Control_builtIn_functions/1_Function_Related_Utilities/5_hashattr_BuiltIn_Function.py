# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 5_hashattr_BuiltIn_Function.py
# Path    : Python-Programming-Language/07_Functions_in_Python/02_Function_Categories/01_Built_in_functions/05_Object_Control_builtIn_functions/1_Function_Related_Utilities/5_hashattr_BuiltIn_Function.py
# Subject : Built-in functions in python
# # Description : hasattr(obj, name) checks whether an attribute exists on an object.
# =============================================================================

import math
import io

def main():

    print(hasattr("abc", "upper"))     # True
    print(hasattr(5, "append"))        # False
    print(hasattr(math, "pi"))         # True
    print(hasattr(math, "e2"))         # False

    # Duck typing: accept a file object or a file path
    def read_text(source):
        if hasattr(source, "read"):        # behaves like a file
            return source.read()
        with open(source) as f:            # otherwise treat it as a path
            return f.read()

    print(read_text(io.StringIO("text from memory")))     # text from memory
    # read_text("notes.txt") would read a real file

    class User:
        def __init__(self, name):
            self.name = name

    u = User("Amar")
    print(hasattr(u, "name"))      # True
    print(hasattr(u, "age"))       # False

if __name__ == "__main__":
    main()
# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 9_bool_typeCasting.py
# Path    : Python-Programming-Language/07_Functions_in_Python/02_Function_Categories/01_Built_in_functions/02_Object_Type_Handling_builtIn_functions/TypeCasting Functions/9_bool_typeCasting.py
# Subject : Typecasting Built-In Functions
# Description : Bool() : Converts a value to True or False, based on Python’s truthy/falsy rules.
# =============================================================================

def main():
    print(bool(1))          # True
    print(bool(0))           # False
    print(bool(""))           # False
    print(bool("hello"))       # True
    print(bool([]))           # False -> empty list is falsy
    print(bool([0]))           # True  -> non-empty list is truthy, even if it contains 0
    print(bool(None))          # False
    print(bool({}))             # False -> empty dict
    print(bool({"a": 1}))       # True

if __name__ == "__main__":
    main()
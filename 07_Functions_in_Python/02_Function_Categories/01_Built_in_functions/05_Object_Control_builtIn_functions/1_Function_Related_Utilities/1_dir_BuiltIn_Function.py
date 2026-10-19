# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 1_dir_BuiltIn_Function.py
# Path    : Python-Programming-Language/07_Functions_in_Python/02_Function_Categories/01_Built_in_functions/05_Object_Control_builtIn_functions/1_Inspecting_and_changing_attributes/1_dir_BuiltIn_Function.py
# Subject : Built-in functions in python
# Description : dir() - Returns a sorted list of the names (attributes and methods) available on an object.
# =============================================================================

print("""
Syntax :
dir()          # names in the current scope
dir(object)    # names available on that object
""")

def main():
    print([n for n in dir([]) if not n.startswith("_")])
    # ['append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

    print("upper" in dir(str))      # True
    print("append" in dir(str))     # False
    print(type(dir()))              # <class 'list'>

#%%

class User:
    role = "guest"

    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hi, {self.name}"

u = User("Amar")
print([n for n in dir(u) if not n.startswith("_")])
# ['greet', 'name', 'role']  -> instance data AND class data

# dir() with no argument lists names in the current scope
a = 1
b = 2
print([n for n in dir() if n in ("a", "b")])     # ['a', 'b']

# Find all string methods that start with "is"
print([n for n in dir(str) if n.startswith("is")][:4])
# ['isalnum', 'isalpha', 'isascii', 'isdecimal']

if __name__ == "__main__":
    main()
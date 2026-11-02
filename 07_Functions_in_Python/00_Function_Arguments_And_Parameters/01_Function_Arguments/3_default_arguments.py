# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 3_default_arguments.py
# Path    : Python-Programming-Language/07_Functions_in_Python/00_Function_Arguments/3_default_arguments.py
# Subject : Function arguments in python
# Description : Default Arguments in Python
# =============================================================================

def main():
#%% Basic Example
    def greet(name, greeting="Hello"):
        return f"{greeting}, {name}!"

    print(greet("Amar"))                 # Hello, Amar!
    print(greet("Amar", "Welcome"))      # Welcome, Amar!
    print(greet("Amar", greeting="Hi"))  # Hi, Amar!

#%% Advanced Examples
    # Rule: parameters with defaults must come AFTER those without
    # def f(a=1, b): ...     # SyntaxError: non-default argument follows default argument

    # Trap: default values are created ONCE, when the function is defined
    def add_item(item, items=[]):          # DANGER
        items.append(item)
        return items

    print(add_item("a"))      # ['a']
    print(add_item("b"))      # ['a', 'b']   <- the same list is reused

    # Fix: use None
    def add_item_safe(item, items=None):
        if items is None:
            items = []
        items.append(item)
        return items

    print(add_item_safe("a"))     # ['a']
    print(add_item_safe("b"))     # ['b']

    # Another trap: a default that depends on time
    import time

    def stamp(when=time.time()):          # fixed once, at definition
        return when

    def stamp_ok(when=None):
        return time.time() if when is None else when

if __name__ == "__main__":
    main()


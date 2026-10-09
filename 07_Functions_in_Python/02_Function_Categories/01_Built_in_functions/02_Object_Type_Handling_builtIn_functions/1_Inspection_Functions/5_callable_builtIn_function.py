# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 5_callable_builtIn_function.py
# Path    : Python-Programming-Language/07_Functions_in_Python/02_Function_Ctaegories/01_Built_in_functions/02_Object_Type_Handling_builtIn_functions/5_callable_builtIn_function.py
# Subject :Inspection Built-In function
# Description : callable() : Checks whether an object can be "called" using () — meaning it behaves like a function.
# =============================================================================

def greet():
    return "Hello"

print(callable(greet))      # True -> functions are callable
print(callable(5))          # False -> an integer is not callable
print(callable("hello"))    # False

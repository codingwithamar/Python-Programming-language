# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 01_Basic_Concept_of_Function.py
# Path    : Python-Programming-Language/07_Functions_in_Python/Group1_Build_the_function/01_Basic_Concept_of_Function.py
# Subject : User Defined FUnctions
# Description : Basic Concept of User Define Function
# =============================================================================

def main():
#%% Basic Concepts
    # Without a function (repeated code)
    print("Total:", 100 + 100 * 0.18)
    print("Total:", 250 + 250 * 0.18)
    print("Total:", 400 + 400 * 0.18)

    # With a function (written once)
    def total_with_tax(price, rate=0.18):
        return price + price * rate

    for price in (100, 250, 400):
        print("Total:", total_with_tax(price))

#%% Basic Examples
    def greet():
        print("Hello, welcome!")

    greet()                  # Hello, welcome!
    greet()                  # you can call it again

    def add(a, b):
        return a + b

    print(add(5, 3))         # 8
    print(add(10, 20))       # 30

#%% Advanced Examples
    # 1. def runs when Python reaches it, so order matters
    # say_hi()                 # NameError: the name does not exist yet

    def say_hi():
        return "hi"

    print(say_hi())            # hi

    # 2. A function is an object. The name is a normal variable.
    print(type(say_hi))        # <class 'function'>
    print(say_hi.__name__)     # say_hi
    alias = say_hi             # no brackets: the function object, not a call
    print(alias())             # hi

    # 3. Calling versus not calling
    print(say_hi)              # <function say_hi at 0x...>  -> the function object
    print(say_hi())            # hi                          -> the result of calling it

    # 4. No overloading: a later def with the same name replaces the earlier one
    def total(a, b):
        return a + b

    def total(a, b, c):
        return a + b + c

    print(total(1, 2, 3))      # 6
    # total(1, 2)              # TypeError: missing 1 required positional argument: 'c'

    # 5. A function can be created conditionally
    import sys

    if sys.version_info >= (3, 8):
        def note():
            return "modern Python"
    else:
        def note():
            return "old Python"

    print(note())              # modern Python

    # 6. An empty body needs a placeholder
    def todo_later():
        pass                   # does nothing, but the body is not empty

    # 7. A function can call another function
    def square(x):
        return x * x

    def sum_of_squares(a, b):
        return square(a) + square(b)

    print(sum_of_squares(3, 4))    # 25

    # 8. A function can be defined inside another function
    def outer():
        def inner():
            return "inside"
        return inner()

    print(outer())             # inside

if __name__ == "__main__":
    main()
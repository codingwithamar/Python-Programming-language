# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 00_User_define_function_basic.py
# Path    : Python-Programming-Language/07_Functions_in_Python/Group1_Build_the_function/00_User_define_function_basic.py
# Subject : User Define Function
# Description : Syntax and Basic Example
# =============================================================================

def main():
    def add (a, b):      #<- header: keyword, name, parameters, colon
        """Add two numbers."""   #<- docstring
        result = a + b           #<- body (must be indented)
        return result            #<- return value

    print(add(10,20))          #30  <- Function call with arguments

    def greet():
        print("Jai Ganesh...")

    greet()          # calling the function
    greet()          # you can call it again

    # def runs at the moment Python reaches it, so the order matters
    # say_hi()          # NameError: the name does not exist yet

    def say_hi():
        return "Hello"

    print(say_hi())     # Hello

    # A function name is a normal variable. It can be reassigned.
    def total(a, b):
        return a + b

    def total(a, b, c):          # Python has NO overloading, the later def replaces the earlier one
        return a + b + c

    print(total(1, 2, 3))        # 6
    # print(total(1, 2))         # TypeError: missing 1 required positional argument: 'c'

    # A function can be created inside an if statement
    import sys
    if sys.version_info >= (3, 8):
        def version_note():
            return "letest Python Version"
    else:
        def version_note():
            return "old Python Version "

    print(version_note())        # letest Python Version

if __name__ == "__main__":
    main()
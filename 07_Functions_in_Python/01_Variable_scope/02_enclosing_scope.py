# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 02_enclosing_scope.py
# Path    : Python-Programming-Language/07_Functions_in_Python/01_Variable_scope/02_enclosing_scope.py
# Subject : Variable scope in python
# Description : enclosing scope
# =============================================================================

def main():
    # Example 1 : This applies when one function is defined inside another function. The inner function can read variables from the outer function automatically,  
    def outer1():
        x1 = "global x1"

        def inner1():
            print(x1)  # child access parent data but cannot modified

        inner1()

    outer1()

    print()
    # Example 2 : if want to modified them needs a "nonlocal" keyword. 
    y = "global y"  #global variable

    def outer2():
        x2 = "enclosing y"   #enclosing variables

        def inner2():
            nonlocal y
            y = "changed by inner2"  # modified enclosing varibale

        inner2()
        print("Inside outer2, y =", y)     # "changed by inner"

    outer2()
    print("Outside outer2, y =", y)              # "global y" -> unchanged

    print()

    #Example 3:
    #Python treats variables with the same name in different scopes as completely 
    #separate variables unless you use global/nonlocal to explicitly link them.

    value = "global value"

    def show_value():
        value = "local value"     # a brand new local variable, does not touch the global one
        print("Inside function:", value)    #Inside function: local value

    show_value()
    print("Outside function:", value)   #Outside function: global value

if __name__ == "__main__":
    main()
# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 00_Demonstartion_of_User_Define_Function.py
# Path    : Python-Programming-Language/07_Functions_in_Python/02_Function_Categories/02_User_defined_functions/01_User_Define_Function_Basics/00_Demonstartion_of_User_Define_Function.py
# Subject : User Define Function
# Description : Demonstartion_of_User_Define_Function
# =============================================================================

def main():
#   Syntax :
#   def function_name(parameters):
#       """Docstring (optional)."""
#       body (indented)
#       return value        # optional

    print("---- Marvellous Infosystems -----")
    print("Demonstration of Advanced Functions")

    # 1) Function which accepts nothing and returns nothing
    def Marvellous1():
        print("Inside Marvellous1")

    # 2) Function which accepts value and returns nothing
    def Marvellous2(value):
        print("Inside Marvellous2")
        print("Accepted value is", value)

    # 3) Function which accepts value and returns value
    def Marvellous3(value):
        print("Inside Marvellous3")
        print("Accepted value is", value)
        return value + 1

    # 4) Function which accepts multiple values and returns multiple values
    def Marvellous4(value1, value2):
        print("Inside Marvellous4")
        add = value1 + value2
        sub = value1 - value2
        return add, sub  # Returns a tuple

    # 5) Function which calls another function defined outside it
    def Marvellous5():
        print("Inside Marvellous5")
        Marvellous1()

    # 6) Function which contains another nested function inside it
    def Marvellous6():
        print("Inside Marvellous6")

        def InnerFun():
            print("Inside InnerFun")

        InnerFun()  # Call the nested function

    # Function calls for the above functions
    no = 11

    Marvellous1()

    Marvellous2(no)

    ret = Marvellous3(no)
    print("Return value is", ret)

    Marvellous5()

    ret1, ret2 = Marvellous4(10, 4)
    print("Addition is", ret1)
    print("Subtraction is", ret2)

    Marvellous6()

if __name__ == "__main__":
    main()


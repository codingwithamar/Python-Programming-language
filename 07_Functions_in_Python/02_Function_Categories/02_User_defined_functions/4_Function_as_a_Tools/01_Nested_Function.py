# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 01_Nested_Function.py
# Path    : Python-Programming-Language/07_Functions_in_Python/02_Function_Categories/02_User_defined_functions/4_Function_as_a_Tools/01_Nested_Function.py
# Subject : User Defined Function
# Description : Nested Function
# =============================================================================

def main():
#%% Basic Concept
    def outer_function():

        def inner_function():
            print("I am Inner Function")

        print("I am Outer Function")

        inner_function()

    outer_function()

    #OUTPUT :
    #I am Outer Function
    #I am Inner Function

#%% Basic Examples
    def outer_function(a):

        def inner_function(b):
            return a + b

        result = inner_function(20)

        return result

    answer = outer_function(10)

    print(answer)

#%% Advanced Example
    def outer_function():

        def inner_function():
            print("Hello from Inner Function")

        return inner_function

    result = outer_function()

    result()

if __name__ == "__main__":
    main()
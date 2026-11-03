# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 01_Nested_Function.py
# Path    : Python-Programming-Language/07_Functions_in_Python/02_Function_Categories/02_User_defined_functions/4_Function_as_a_Tools/01_Nested_Function.py
# Subject : User Defined Functions
# Description : Nested Function
# =============================================================================

def main():
    # Nested function: the inner function can read the outer variable
    def outer():
        message = "Hello"

        def inner():
            print(message)         # reads outer's variable

        inner()

    outer()                        # Hello

    # Closure: the inner function outlives the outer function
    def make_multiplier(factor):
        def multiplier(x):
            return x * factor      # "factor" is remembered
        return multiplier

    double = make_multiplier(2)
    triple = make_multiplier(3)

    print(double(10))              # 20
    print(triple(10))              # 30


if __name__ == "__main__":
    main()
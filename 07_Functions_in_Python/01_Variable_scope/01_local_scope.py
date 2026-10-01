# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 01_local_scope.py
# Path    : Python-Programming-Language/07_Functions_in_Python/01_Variable_scope/01_local_scope.py
# Subject : Variable Scope
# Description : 1. local scope variable
# =============================================================================

def main():
    #Example 1 :
    def wish():
        message = "Hello"       # local variable
        print(message)

    wish()
    # print(message)            # NameError: message is not defined here
    # message only exists inside greet(). Trying to use it outside the function causes an error.

    #Example 2 :
    def calculate_total(price, quantity):
        tax_rate = 0.1                     # local variable
        subtotal = price * quantity        # local variable
        tax = subtotal * tax_rate          # local variable
        total = subtotal + tax             # local variable
        return total

    result = calculate_total(100, 3)
    print("Total:", result)
    # subtotal, tax_rate, tax, total -> none of these exist outside the function

if __name__ == "__main__":
    main()
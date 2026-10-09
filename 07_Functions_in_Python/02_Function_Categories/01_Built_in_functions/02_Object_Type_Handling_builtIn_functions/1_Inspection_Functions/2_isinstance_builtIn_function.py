# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 03_isinsatnce_function.py
# Path    : Python-Programming-Language/07_Functions_in_Python/02_Function_Ctaegories/01_Built_in_functions/03_isinsatnce_function.py
# Subject : Inspection Built-in functions in python
# Description : isinstance():checks whether an object belongs to a specific type or class (including its subclasses). It returns True or False.
# =============================================================================

def main():
#   Syntax : isinstance(object, classinfo)

# %% Example 1 : Basic usecase
    x = 10
    print(isinstance(x,int))    # True
    print(isinstance(x,str))    # False

# %% Example 2: Using isinstance() for input validation in a function that accepts mixed types

def total_price(items):
    if not isinstance(items,(list,tuple)):
        raise TypeError("items must be a list or tuple")

    total = 0
    for item in items:
        if not isinstance(item,(int,float)):
            raise TypeError(f"{item} is not a number")
        total += item
    return total

#items = [10,20,amar]   # RAISE ERROR
#items = (10,20,30)     #Worked
items = [10,20,30]      #Worked

print(items)
print(total_price(items))

if __name__ == "__main__":
    main()
# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : shop.py
# Path    : Python-Programming-Language/08_Modules_And_Packages_In_Python/6_Module_Attributes/shop.py
# Subject : # Subject : Modules and Packages in Python
# Description : __name__ – Module Name - Basic Example
# Dependency File : 1__name__ModuleName.py and 1i__name__ModuleName.py
# =============================================================================

# This shop.py is support file for 1__name__ModuleName.py and 1i__name__ModuleName.py

print("my name is:", __name__)

# Function
def hello():
    return "hello from shop Function"

def total(a, b):
    return a + b

# Class
class Cart:
    print("Hello from class")
    def __init__(self, item):
        self.item = item

if __name__ == "__main__":
    print("running directly")
    print(hello())

'''
OUTPUT : If we directly Run code
    my name is: __main__
    running directly
    hello from shop
'''
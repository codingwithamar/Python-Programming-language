# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 1i__name__ModuleName.py
# Path    : Python-Programming-Language/08_Modules_And_Packages_In_Python/6_Module_Attributes/1i__name__ModuleName.py
# Subject : # Subject : Modules and Packages in Python
# Description : __name__ – Module Name - Advanced Example
# =============================================================================

# Uses the setup from section 0
import shop
import sys
import json

# 1. Every module knows its own name
print(shop.__name__)                         # shop
print(json.__name__)                         # json
print(json.decoder.__name__)                 # json.decoder   (a submodule has a dotted name)

# 2. The name is also the key in sys.modules
print(sys.modules["shop"] is shop)           # True
print(sys.modules["__main__"].__name__)      # __main__

# 3. Functions and classes remember the module they were defined in
print(shop.total.__module__)                 # shop
print(shop.Cart.__module__)                  # shop
def local_function():
    pass
print(local_function.__module__)             # __main__   (defined in the running script)

# 4. A guard in a real script
def main():
    print("running the program")

if __name__ == "__main__":
    main()

# 5. Why the guard matters: without it, importing a file would run its program code
#    "import shop" must not start a download, delete files, or print a menu.

# 6. Use __name__ for logging, so each module has its own logger
import logging
logger = logging.getLogger(__name__)
print(logger.name)                           # __main__ here, "shop" if the line is inside shop.py

# 7. A file can print its own name even inside a package:  __name__ gives the FULL dotted path
#    shopping/cart.py  imported as shopping.cart  -> __name__ == "shopping.cart"

# 8. __name__ of a module run with  python -m package.module  is "__main__"
#    (and  __package__ tells you the package, so relative imports still work)

# 9. __name__ is just a string and can be read, but should not be changed
print(type(shop.__name__))                   # <class 'str'>

# 10. Do not confuse these
print(__name__ == "__main__")                # True when this very file is run directly


'''
OUTPUT : 
        my name is: shop
        Hello from class
        shop
        json
        json.decoder
        True
        __main__
        shop
        shop
        __main__
        running the program
        __main__
        <class 'str'>
        True
'''

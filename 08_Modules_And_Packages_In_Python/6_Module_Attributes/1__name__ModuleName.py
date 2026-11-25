# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 1__name__ModuleName.py
# Path    : Python-Programming-Language/08_Modules_And_Packages_In_Python/6_Module_Attributes/1__name__ModuleName.py
# Subject : # Subject : Modules and Packages in Python
# Description : __name__ – Module Name - Basic Example
# Dependency File : shop.py
# =============================================================================

import shop                  # prints: my name is: shop   (the guard stays quiet)
print(shop.__name__)         # shop
print(__name__)              # __main__

'''
OUTPUT: If we directly Run code
    my name is: __main__
    running directly
hello from shop
'''
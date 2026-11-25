# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 2__file__ModuleFileLocation.py
# Path    : Python-Programming-Language/08_Modules_And_Packages_In_Python/6_Module_Attributes/2__file__ModuleFileLocation.py
# Subject : # Subject : Modules and Packages in Python
# Description : __file__ - Module File Location - Basic Concept Example
# =============================================================================

import json
import os

print(json.__file__)                  # e.g. /usr/lib/python3.12/json/__init__.py
print(os.__file__)                    # e.g. /usr/lib/python3.12/os.py

import sys
print(hasattr(sys, "__file__"))       # False   -> built-in module, no file

# In your own file:
# where_am_i.py
print(__file__)                       # the path of this file

'''
OUTPUT : 
        /usr/lib/python3.14/json/__init__.py
        /usr/lib/python3.14/os.py
        False
        /home/sumaney/Desktop/GitHub/Python-Programming-Language/08_Modules_And_Packages_In_Python/6_Module_Attributes/2__file__ModuleFileLocation.py
'''



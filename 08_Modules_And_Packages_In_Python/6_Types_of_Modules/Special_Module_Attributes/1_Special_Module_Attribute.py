# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 1_Special_Module_Attribute.py
# Path    : Python-Programming-Language/08_Modules_And_Packages_In_Python/6_Types_of_Modules/Special_Module_Attributes/1_Special_Module_Attribute.py
# Subject : # Subject : Modules and Packages in Python
# Description : Special module attributes
# =============================================================================

import sys
import os
import math
import json

modules = [sys, os, math, json]

for module in modules:
    print(f"Module       : {module.__name__}")
    print(f"File         : {getattr(module, '__file__', None)}")
    print(f"Origin       : {module.__spec__.origin}")
    print("-" * 40)

    '''
    OUTPUT :
    Module       : sys
    File         : None
    Origin       : built-in
    ----------------------------------------
    Module       : os
    File         : /usr/lib/python3.14/os.py
    Origin       : frozen
    ----------------------------------------
    Module       : math
    File         : None
    Origin       : built-in
    ----------------------------------------
    Module       : json
    File         : /usr/lib/python3.14/json/__init__.py
    Origin       : /usr/lib/python3.14/json/__init__.py
    ----------------------------------------
    '''
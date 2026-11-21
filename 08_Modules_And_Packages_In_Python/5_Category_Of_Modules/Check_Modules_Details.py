# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : Check_Modules_Details.py
# Path    : Python-Programming-Language/08_Modules_And_Packages_In_Python/5_Category_Of_Modules/Check_Modules_Details.py
# Subject : Modules and Packages in Python
# Description : Check Category of Modules and packages
# =============================================================================

import sys
import math
import json

# Built-in modules
print("Built-in Modules:")
print(sys.builtin_module_names)

# Check whether a module is built-in
print("\nIs sys built-in?")
print("sys" in sys.builtin_module_names)

print("\nIs math built-in?")
print("math" in sys.builtin_module_names)

# Inspect module names
print("\nMath module members:")
print(dir(math))

print("\nJSON module members:")
print(dir(json))
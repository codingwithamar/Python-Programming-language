# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 2_Built_In_Model.py
# Path    : Python-Programming-Language/08_Modules_And_Packages_In_Python/6_Types_of_Modules/1_Built_in_Modules/2_Built_In_Model.py
# Subject : Modules and Packages in Python
# Description : Basic Built In Modules Example
# =============================================================================

#Basic Example
import sys

print("sys" in sys.builtin_module_names)        # True
print("builtins" in sys.builtin_module_names)   # True
print(hasattr(sys, "__file__"))                 # False  -> a built-in module has no file
print(sys.__spec__.origin)                      # built-in

#%% Advanced Examples

import sys
import builtins

# 1. See the loader that handles built-in modules
print(sys.__spec__.loader.__name__)             # BuiltinImporter

# 2. The list of built-in module names (it depends on how your Python was built)
print(len(sys.builtin_module_names) > 5)        # True
print(isinstance(sys.builtin_module_names, tuple))   # True

# 3. "builtins" is the module behind len, print, range, Exception ...
print(builtins.len is len)                      # True

# 4. Built-in modules are found first, before any folder is searched
#    A file named sys.py in your folder can NOT replace the real sys module.





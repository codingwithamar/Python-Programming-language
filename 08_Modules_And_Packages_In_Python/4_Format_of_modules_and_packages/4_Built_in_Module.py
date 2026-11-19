# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 4_Built_in_Module.py
# Path    : Python-Programming-Language/08_Modules_And_Packages_In_Python/4_Format_of _modules_and_packages/4_Built_in_Module.py
# Subject : Format of Modules and Packages
# Description : Built-in Module(sys, builtins, _thread)
# =============================================================================

import sys
import builtins

print(sys.version)
print(builtins.len([10, 20, 30]))

#   OUTPUT : 
#   3.14.4 (main, Aug 20 2026, 10:41:58) [GCC 15.2.0]
#   3

'''
How to recognize it?
Python provides sys.builtin_module_names, 
a tuple containing the names of modules compiled into the interpreter.
'''
import sys

print("sys" in sys.builtin_module_names)
print("builtins" in sys.builtin_module_names)

#   OUTPUT :
#       True
#       True

'''
For built-in modules, sys.__spec__.origin is normally "built-in" and __file__ is usually absent.
You can inspect an individual module too:
'''
import sys

print(sys.__name__)
print(sys.__spec__.origin)
print(hasattr(sys, "__file__"))

#   OUTPUT :
#       sys
#       built-in
#       False
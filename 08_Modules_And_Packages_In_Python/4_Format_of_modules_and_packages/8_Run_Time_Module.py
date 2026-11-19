# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 8_Run_Time_Module.py
# Path    : Python-Programming-Language/08_Modules_And_Packages_In_Python/4_Format_of_modules_and_packages/8_Run_Time_Module.py
# Subject : Format of Modules and Packages
# Description : Run-time Module (Dynamically Created Module)
# =============================================================================

import types

# Create a module object dynamically
my_module = types.ModuleType("my_module")

# Add a variable to the module
my_module.name = "Amar"

# Add a function to the module
def greet():
    return "Hello, Amar!"

my_module.greet = greet

# Access module members
print(my_module.name)
print(my_module.greet())

'''
OUTPUT :
    Amar
    Hello, Amar!
'''


#   How to recognize it?
print(type(my_module))
print(my_module.__name__)
print(hasattr(my_module, "__file__"))

'''
OUTPUT :
    <class 'module'>
    my_module
    False
'''

#   How to use it?
import sys
import types

# Create a module
my_module = types.ModuleType("my_module")

# Add a function
my_module.greet = lambda: "Hello from dynamic module!"

# Register it
sys.modules["my_module"] = my_module

# Import the registered module
import my_module

print(my_module.greet())

'''
OUTPUT :
    Hello from dynamic module!
'''
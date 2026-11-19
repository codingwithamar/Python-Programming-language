# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 6_Packages.py
# Path    : Python-Programming-Language/08_Modules_And_Packages_In_Python/4_Format_of_modules_and_packages/6_Packages.py
# Subject : Format of Modules and Packages
# Description : Packages(__init__.py)
# =============================================================================

#   File1 : mypackage/calculator.py
def add(a, b):
    return a + b

#   File2 : mypackage/geometry.py
def area_rectangle(length, width):
    return length * width

#   File3 : main.py
from mypackage import calculator
from mypackage import geometry

print(calculator.add(10, 20))
print(geometry.area_rectangle(10, 5))

# OUTPUT :
#    30
#    50


#   How to recognize a Package?
import json

print(json.__name__)
print(json.__path__)


#   What is __init__.py?
mypackage/__init__.py
print("mypackage initialized")

#   How to use a Package?
import mypackage.calculator

print(mypackage.calculator.add(5, 10))
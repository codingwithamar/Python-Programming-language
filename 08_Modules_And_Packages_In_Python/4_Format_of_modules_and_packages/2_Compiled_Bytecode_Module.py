# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 2_Compiled_Bytecode_Module.py
# Path    : Python-Programming-Language/08_Modules_And_Packages_In_Python/4_Format_of _modules_and_packages/2_Compiled_Bytecode_Module.py
# Subject : Format of Modules and Packages
# Description : Compiled Bytecode Module(.pyc file)
# =============================================================================

'''
***  How to recognize it?  ***
import calculator

print(calculator.__file__)
print(calculator.__cached__)

'''

#   File 1 - calculator.py
def add(a, b):
    return a + b

#   File 2 - main.py
import calculator

print(calculator.add(10, 20))

'''
Normally, you do not manually import .pyc files. Python's import system manages bytecode caching automatically.
You can also explicitly compile Python files using:
    python3 -m compileall
'''
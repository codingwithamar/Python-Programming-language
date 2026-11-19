# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 1_Python_Source_Module.py
# Path    : Python-Programming-Language/08_Modules_And_Packages_In_Python/4_Format_of _modules_and_packages/1_Python_Source_Module.py
# Subject : Format of Modules and Packages
# Description : Python Source Modules(.py file)
# =============================================================================

'''
*** How to Recognise this : ***
    import calculator

    print(calculator.__file__)
    print(calculator.__name__)

*** If we run above then we get path of that File ***
    /home/user/project/calculator.py
    calculator
'''



#  File 1 : calculator.py

PI = 3.14159

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

class Calculator:
    def subtract(self, a, b):
        return a - b


#  File 2 : main.py

import calculator

print(calculator.PI)
print(calculator.add(10, 20))
print(calculator.multiply(5, 4))

obj = calculator.Calculator()
print(obj.subtract(20, 5))



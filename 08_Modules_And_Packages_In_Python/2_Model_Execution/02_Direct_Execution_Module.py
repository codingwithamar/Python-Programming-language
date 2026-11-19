# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 02_Direct_Execution_Module.py
# Path    : Python-Programming-Language/08_Modules_And_Packages_In_Python/1_Basics_of_Modules/02_Direct_Execution_Module.py
# Subject : Modules and Packages in Python
# Description : Modules / Model Execution / Direct Execution
# =============================================================================

print("greet.py is running, __name__ =", __name__)

def hello(name):
    return "Hello, " + name

if __name__ == "__main__":
    print(hello("Amar"))        # runs only when the file is run directly
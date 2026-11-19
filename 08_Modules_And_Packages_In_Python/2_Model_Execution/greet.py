# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : greet.py
# Path    : Python-Programming-Language/08_Modules_And_Packages_In_Python/1_Basics_of_Modules/greet.py
# Subject : Reference code 
# Description : Supporting code file for 03_import_Execution_Module.py
# =============================================================================
print("greet.py is running, __name__ =", __name__)

def hello(name):
    return "Hello, " + name

if __name__ == "__main__":
    print(hello("Amar"))        # runs only when the file is run directly
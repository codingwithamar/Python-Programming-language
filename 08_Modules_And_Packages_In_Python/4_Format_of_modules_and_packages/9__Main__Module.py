# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 9__Main__Module.py
# Path    : Python-Programming-Language/08_Modules_And_Packages_In_Python/4_Format_of_modules_and_packages/9__Main__Module.py
# Subject : Format of Modules and Packages
# Description : __main__ Module
# =============================================================================

#   Example 1: Direct Execution
#   File: app.py

print(__name__)

if __name__ == "__main__":
    print("Program is running directly")

'''
OUTPUT :
    __main__
    Program is running directly
'''

#   Example 2: Importing the Same File
#   File : main.py

import app

print("Inside main.py")

'''
OUTPUT :
    app
    Program is running directly
    Inside main.py
'''

#   How to use it?
def main():
    print("Application started")

if __name__ == "__main__":
    main()

    


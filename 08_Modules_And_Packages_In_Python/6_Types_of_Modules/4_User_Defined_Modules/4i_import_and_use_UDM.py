# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 4i_import_and_use_UDM.py
# Path    : Python-Programming-Language/08_Modules_And_Packages_In_Python/6_Types_of_Modules/4_User_Defined_Modules/4i_import_and_use_UDM.py
# Subject : Modules and Packages in Python
# Description : User Defined Modules(Import and Use in Another File)
# =============================================================================

# Import user-defined module
import create_UDM

# Access module variable
print(create_UDM.PI)

# Call module functions
print(create_UDM.add(10, 20))
print(create_UDM.multiply(5, 4))
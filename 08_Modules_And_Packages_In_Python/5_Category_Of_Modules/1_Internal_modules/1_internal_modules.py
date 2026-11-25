# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 1_internal_modules.py
# Path    : Python-Programming-Language/08_Modules_And_Packages_In_Python/5_Category_Of_Modules/1_Internal_modules/1_internal_modules.py
# Subject : Modules and Packages in Python
# Description : Category of modules/1) internal modules
# =============================================================================

# Public module
import functools

# Internal implementation module
import _functools

print(functools)
print(_functools)

'''
OUTPUT :
<module 'functools' from '/usr/lib/python3.14/functools.py'>
<module '_functools' (built-in)>
'''

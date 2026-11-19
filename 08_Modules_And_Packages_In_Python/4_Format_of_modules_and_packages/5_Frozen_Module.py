# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 5_Frozen_Module.py
# Path    : Python-Programming-Language/08_Modules_And_Packages_In_Python/4_Format_of_modules_and_packages/5_Frozen_Module.py
# Subject : Format of Modules and Packages
# Description : Frozen Module(importlib._bootstrap, importlib._bootstrap_external)
# =============================================================================

import importlib._bootstrap

module = importlib._bootstrap

print(module.__name__)
print(module.__spec__.origin)   # module.__spec__.origin == "frozen"
print(module.__file__)

#OUTPUT :
#   importlib._bootstrap
#   frozen
#   /usr/lib/python3.14/importlib/_bootstrap.py
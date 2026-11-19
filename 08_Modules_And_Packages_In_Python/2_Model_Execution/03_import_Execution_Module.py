# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 03_import_Execution_Module.py
# Path    : Python-Programming-Language/08_Modules_And_Packages_In_Python/1_Basics_of_Modules/03_import_Execution_Module.py
# Subject : Modules and Packages in Python
# Description : Modules / Model Execution / Import Execution
# =============================================================================

import greet                    # runs greet.py once
import greet                    # nothing happens: already in sys.modules

print(greet.hello("Riya"))
print("greet" in __import__("sys").modules)   # True


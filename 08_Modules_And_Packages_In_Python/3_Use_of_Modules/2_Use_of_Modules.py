# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 2_Use_of_Modules.py
# Path    : Python-Programming-Language/08_Modules_And_Packages_In_Python/3_Use_of_Modules/2_Use_of_Modules.py
# Subject : Enter Subject
# Description : Description
# =============================================================================

import sys
import converter
import converter                    # second import does not run the file again

print(converter.c_to_f(100))
print("converter" in sys.modules)
print(converter.__name__)


'''
OUTPUT :
converter loaded
212.0
True
converter
'''
'''
What this shows:
A module runs only once. Python stores it in sys.modules, and later imports reuse it.
The if __name__ == "__main__": block is skipped on import, so the module can act as both a library and a script.
__all__ controls what from converter import * brings in. _round2 stays private by convention.
'''
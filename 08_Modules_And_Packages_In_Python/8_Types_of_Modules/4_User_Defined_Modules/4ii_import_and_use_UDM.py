# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 4ii_import_and_use_UDM.py
# Path    : Python-Programming-Language/08_Modules_And_Packages_In_Python/6_Types_of_Modules/4_User_Defined_Modules/4ii_import_and_use_UDM.py
# Subject : Modules and Packages in Python
# Description : User Defined Modules Advanced Examples
# =============================================================================

import sys
import pathlib
import tempfile

folder = tempfile.mkdtemp()
pathlib.Path(folder, "tools.py").write_text(
    "def double(x):\n"
    "    return x * 2\n"
    "\n"
    'if __name__ == "__main__":\n'
    '    print("tools.py is running directly")\n'
)
sys.path.insert(0, folder)               # make the folder importable

import tools                             # the guard stops the print, because we only imported it
print(tools.double(21))                  # 42
print(tools.__name__)                    # tools          (when imported)
print(__name__)                          # __main__       (the file you run)
print(tools.__file__.endswith("tools.py"))     # True

# Running the file directly:  python tools.py   -> prints: tools.py is running directly
# Importing the file:         import tools      -> prints nothing from the guard

# TRAP: do not name your file like a standard module
#   A file called random.py or json.py in your folder hides the real one.
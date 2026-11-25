# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 2i___file__ModuleFileLocation.py
# Path    : Python-Programming-Language/08_Modules_And_Packages_In_Python/6_Module_Attributes/2i___file__ModuleFileLocation.py
# Subject : # Subject : Modules and Packages in Python
# Description : __file__ - Module File Location - Advanced Example
# =============================================================================

# Uses the setup from section 0
import os           # Standard Library Function - OS Related Operations
import pathlib      # Standard Library Function - Work with Filesystem Path
import shop         # User Defined Function

# 1. See the path of the module
print(shop.__file__.endswith("shop.py"))             # True

# 2. The folder that contains the module (the safe way to find files next to your code)
here = pathlib.Path(shop.__file__).resolve().parent
print(here.exists())    # True
print(here.name)        # 6_module Atrributes

# 3. Read a data file stored next to the module
(here / "settings.txt").write_text("debug=true\n")      # File Check/Created and Write inside
settings = (here / "settings.txt").read_text()          # File Data Read and store into settings variable
print(settings.strip())                                 # debug=true

# 4. The old os.path way
print(os.path.dirname(os.path.abspath(shop.__file__)) == str(here))   # True

# 5. In a script, use __file__ to build paths. Do NOT depend on the current working folder
BASE = (pathlib.Path(__file__).resolve().parent 
        if "__file__" in globals() 
        else pathlib.Path.cwd())
print(BASE.exists())                                 # True
# os.getcwd() is where you STARTED Python. It can be a different folder from the script's folder.

# 6. Compiled bytecode location (Python 3.x): __cached__
print(shop.__cached__.endswith(".pyc"))              # True  (the __pycache__/shop.cpython-XYZ.pyc file)

# 7. When __file__ is missing
import sys
import types
print(hasattr(sys, "__file__"))                      # False
print(getattr(sys, "__file__", "no file"))           # no file
runtime = types.ModuleType("runtime")
print(hasattr(runtime, "__file__"))                  # False

# 8. For a package, __file__ is the __init__.py and __path__ is the folder list
import json
print(json.__file__.endswith("__init__.py"))         # True
print(list(json.__path__)[0] == os.path.dirname(json.__file__))   # True

# 9. Show where a module came from (a handy debug tool)
import importlib.util
spec = importlib.util.find_spec("shop")
print(spec.origin == shop.__file__)                  # True   (spec.origin is the same path)

# 10. Reading a resource that ships INSIDE a package: prefer importlib.resources
#     from importlib.resources import files
#     text = files("mypackage").joinpath("data.txt").read_text()
#     It also works when the package is installed as a zip file.


'''
OUTPUT : 
        my name is: shop
        Hello from class
        True
        True
        6_Module_Attributes
        debug=true
        True
        True
        True
        False
        no file
        False
        True
        True
        True
'''
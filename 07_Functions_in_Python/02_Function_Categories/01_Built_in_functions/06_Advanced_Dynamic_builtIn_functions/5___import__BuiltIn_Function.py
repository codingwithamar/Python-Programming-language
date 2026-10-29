# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 5___import__BuiltIn_Function.py
# Path    : Python-Programming-Language/07_Functions_in_Python/02_Function_Categories/01_Built_in_functions/06_Advanced_Dynamic_builtIn_functions/5___import__BuiltIn_Function.py
# Subject : Advanced Built-in functions in python
# Description : __import__() is the low-level function that the import statement calls behind the scenes.
# =============================================================================

def main():
#%% Basic Examples
    import sys

    # 1. Import a module by its name as a string
    math = __import__("math")
    print(type(math))              # <class 'module'>
    print(math.sqrt(16))           # 4.0
    print(math.__name__)           # math
    #__import__() स्वतः module object return करतो.

    # 2. The same result as the import statement
    import math as math2
    print(math is math2)           # True -> same cached module object

    # 3. The name can be stored in a variable
    name = "os"
    os_module = __import__(name)
    print(os_module.name)          # posix (Linux/Mac) or nt (Windows)

    # 4. Imported modules are cached
    print("math" in sys.modules)   # True
    print(__import__("json") is __import__("json"))    # True -> second call returns the cached module

    # 5. Errors
    try:
        __import__("no_such_module")
    except ModuleNotFoundError as error:
        print(error)               # No module named 'no_such_module'

#%% Advanced Examples
    import sys
    import builtins

    # 1. Trap with dotted names: the TOP package is returned
    top = __import__("xml.dom")
    print(top.__name__)                     # xml  (not xml.dom)

    sub = __import__("xml.dom", fromlist=["minidom"])
    print(sub.__name__)                     # xml.dom
    print(sub.minidom.__name__)             # xml.dom.minidom -> fromlist also loaded the submodule

    # 2. The "from ... import ..." form written by hand
    _temp = __import__("collections", fromlist=["OrderedDict"])
    OrderedDict = _temp.OrderedDict
    print(OrderedDict)                      # <class 'collections.OrderedDict'>

    # 3. Load a function from a text path (plugin pattern)
    def load_function(dotted_path):
        module_name, function_name = dotted_path.rsplit(".", 1)
        module = __import__(module_name, fromlist=[function_name])
        return getattr(module, function_name)

    print(load_function("math.sqrt")(25))                  # 5.0
    print(load_function("json.dumps")({"a": 1}))           # {"a": 1}

    # 4. The recommended way for the same job
    import importlib

    module = importlib.import_module("xml.dom.minidom")
    print(module.__name__)                  # xml.dom.minidom -> gives exactly the module you asked for

    # 5. Handle a missing module safely
    def try_import(name):
        try:
            return importlib.import_module(name)
        except ImportError:
            print(f"Module '{name}' is not installed")
            return None

    try_import("some_missing_package")      # Module 'some_missing_package' is not installed

    # 6. The import statement really calls __import__ (shown by replacing it for a moment)
    original_import = builtins.__import__

    def logging_import(name, globals=None, locals=None, fromlist=(), level=0):
        print("Importing:", name)
        return original_import(name, globals, locals, fromlist, level)

    builtins.__import__ = logging_import
    try:
        import colorsys                     # prints: Importing: colorsys
    finally:
        builtins.__import__ = original_import     # ALWAYS restore it

    # 7. Relative imports use level (only works inside a package)
    # Inside a file in package "shop":
    #   from . import utils        ->  __import__("", globals(), locals(), ["utils"], 1)
    #   from .. import config      ->  __import__("", globals(), locals(), ["config"], 2)
    #   level=1 means "this package", level=2 means "the parent package"

if __name__ == "__main__":
    main()
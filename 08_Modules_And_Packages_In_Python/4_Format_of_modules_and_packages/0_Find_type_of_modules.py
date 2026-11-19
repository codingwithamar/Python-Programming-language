# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 0_Find_type_of_modules.py
# Path    : Python-Programming-Language/08_Modules_And_Packages_In_Python/4_Format_of_modules_and_packages/0_Find_type_of_modules.py
# Subject : Format of Modules and Packages
# Description : This function names the source and the form of any module. It runs on Python 3.10 and newer.
# =============================================================================

import sys
import pathlib
import tempfile
import importlib.util
from importlib import machinery

def describe(name):
    if name in sys.builtin_module_names:
        return "built-in module (inside the interpreter)"

    spec = importlib.util.find_spec(name)
    if spec is None:
        return "not found"

    # How is it stored?
    if spec.loader is machinery.FrozenImporter:
        how = "frozen module"
    elif isinstance(spec.loader, machinery.ExtensionFileLoader):
        how = "C extension module"
    elif isinstance(spec.loader, machinery.SourcelessFileLoader):
        how = "compiled .pyc only"
    elif spec.origin is None and spec.submodule_search_locations is not None:
        how = "namespace package"
    elif spec.submodule_search_locations is not None:
        how = "package (folder with __init__.py)"
    else:
        how = "Python source file (.py)"

    # Where does it come from?
    top = name.split(".")[0]
    origin = spec.origin or ""
    if top in sys.stdlib_module_names:
        where = "standard library"
    elif "site-packages" in origin or "dist-packages" in origin:
        where = "third-party"
    else:
        where = "your own (local) module"
    return f"{where}, {how}"

# Prepare a local module and a namespace package
root = tempfile.mkdtemp()
pathlib.Path(root, "mytool.py").write_text("x = 1\n")
pathlib.Path(root, "ns_pkg").mkdir()
pathlib.Path(root, "ns_pkg", "part.py").write_text("y = 2\n")
sys.path.insert(0, root)

print(describe("sys"))          # built-in module (inside the interpreter)
print(describe("json"))         # standard library, package (folder with __init__.py)
print(describe("json.tool"))    # standard library, Python source file (.py)
print(describe("mytool"))       # your own (local) module, Python source file (.py)
print(describe("ns_pkg"))       # your own (local) module, namespace package
print(describe("no_such_mod"))  # not found
print(describe("pip"))          # third-party, package (folder with __init__.py)   (if pip is installed)
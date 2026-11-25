# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 4i__dict__ModuleNamespace.py
# Path    : Python-Programming-Language/08_Modules_And_Packages_In_Python/6_Module_Attributes/4i__dict__ModuleNamespace.py
# Subject : # Subject : Modules and Packages in Python
# Description :  __dict__	: Module Namespace - Advanced Example
# =============================================================================
# Uses the setup from section 0
import gst as shop
import types

# 1. The special names are inside the dictionary
for key in ("__name__", "__doc__", "__file__", "__package__", "__spec__"):
    print(key, "->", key in shop.__dict__)           # all True

# 2. vars(), dir(), and __dict__
print(vars(shop) is shop.__dict__)                    # True
print("TAX" in dir(shop))                             # True   (dir gives a sorted list of names)

# 3. Read, add, change, and remove names through the dictionary
shop.__dict__["DISCOUNT"] = 0.1
print(shop.DISCOUNT)                                  # 0.1
shop.TAX = 0.20                                       # same as  shop.__dict__["TAX"] = 0.20
print(shop.__dict__["TAX"], shop.total(100))          # 0.2 120.0
del shop.DISCOUNT
print("DISCOUNT" in shop.__dict__)                    # False

# 4. A module's data is SHARED by every importer
shop.items.append("pen")
import gst as another_name
print(another_name.items)     # ['pen']
print(shop is another_name)   # True
print(shop.__dict__ is another_name.__dict__)  # True

# 5. Pick out functions and classes by type
functions = [n for n, v in vars(shop).items() if isinstance(v, types.FunctionType)]
classes = [n for n, v in vars(shop).items() if isinstance(v, type)]
print(functions, classes)                             # ['total'] ['Cart']

# 6. Call a function by its name stored in a string (plugin and command pattern)
command = "total"
print(vars(shop)[command](100))                       # 120.0
print(getattr(shop, command)(100))                    # 120.0   (the same, and clearer)

# 7. The current file's own namespace: globals()
x = 5
print(globals()["x"])                                 # 5
print(globals() is sys_modules_main if (sys_modules_main := __import__("sys").modules["__main__"].__dict__) else None)   # True

# 8. __dict__ of a function, class, and instance are different things
class Demo:
    a = 1
    def __init__(self):
        self.b = 2
d = Demo()
print(d.__dict__)                                     # {'b': 2}
print("a" in Demo.__dict__)                           # True
print(type(Demo.__dict__).__name__)                   # mappingproxy   (read-only for classes)
print(type(shop.__dict__).__name__)                   # dict           (editable for modules)

# 9. __builtins__ lives inside the namespace and gives access to len, print, etc.
print("__builtins__" in shop.__dict__)                # True

# 10. Create a module and fill its namespace by hand
m = types.ModuleType("demo")
m.__dict__.update({"x": 10, "double": lambda v: v * 2})
print(m.x, m.double(4))                               # 10 8

# 11. Run code INSIDE a module's namespace
exec("y = x + 1", m.__dict__)
print(m.y)                                            # 11

# 12. Wildcard imports use the namespace and __all__
#     from shop import *   imports every public name (not starting with "_"),
#     or only the names listed in  __all__ = ["total", "Cart"]  if the module defines it.

# 13. Reload resets the namespace code (names are redefined, old extra names stay)
import importlib
shop.extra = "added by hand"
importlib.reload(shop)
print(hasattr(shop, "extra"))                         # True   (reload keeps old names in the same dict)

'''
OUTPUT : 
        __name__ -> True
        __doc__ -> True
        __file__ -> True
        __package__ -> True
        __spec__ -> True
        True
        True
        0.1
        0.2 120.0
        False
        ['pen']
        True
        True
        ['total'] ['Cart']
        120.0
        120.0
        5
        True
        {'b': 2}
        True
        mappingproxy
        dict
        True
        10 8
        11
        True
'''

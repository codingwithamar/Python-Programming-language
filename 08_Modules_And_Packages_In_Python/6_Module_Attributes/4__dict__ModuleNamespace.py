# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 4__dict__ModuleNamespace.py
# Path    : Python-Programming-Language/08_Modules_And_Packages_In_Python/6_Module_Attributes/4__dict__ModuleNamespace.py
# Subject : # Subject : Modules and Packages in Python
# Description :  __dict__	: Module Namespace - Basic Example
# =============================================================================

import gst

print(type(gst.__dict__))                 # <class 'dict'>
print(gst.__dict__["TAX"])                # 0.18
print(gst.TAX == gst.__dict__["TAX"])    # True

# the names that YOU defined (skip the special ones)
names = [n for n in gst.__dict__ if not n.startswith("__")]
print(names)                               # ['TAX', 'items', 'total', 'Cart']

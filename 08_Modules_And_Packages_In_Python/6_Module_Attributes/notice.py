# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : notice.py
# Path    : Python-Programming-Language/08_Modules_And_Packages_In_Python/6_Module_Attributes/notice.py
# Subject : # Subject : Modules and Packages in Python
# Dependency File : 3__doc__ModuleDocstring.py
# =============================================================================

# notice.py
"""Notice For helpers: prices and discounts."""

def total(price):
    """Return the price with tax."""
    return price * 1.18

class Cart:
    print("Hello from class")
    def __init__(self, item):
        self.item = item
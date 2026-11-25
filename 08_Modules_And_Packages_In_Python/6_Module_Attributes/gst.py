# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : gst.py
# Path    : Python-Programming-Language/08_Modules_And_Packages_In_Python/6_Module_Attributes/gst.py
# Subject : # Subject : Modules and Packages in Python
# Description : Support file for 4__dict__moduleNamespace.py
# =============================================================================

"""Shop helpers: prices and discounts."""

TAX = 0.18
items = []


def total(price):
    """Return the price with tax."""
    return price * (1 + TAX)


class Cart:
    pass


if __name__ == "__main__":
    print("gst.py is running directly")
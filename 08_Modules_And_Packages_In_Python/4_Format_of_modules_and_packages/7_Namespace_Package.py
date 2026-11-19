# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 7_Namespace_Package.py
# Path    : Python-Programming-Language/08_Modules_And_Packages_In_Python/4_Format_of_modules_and_packages/7_Namespace_Package.py
# Subject : Format of Modules and Packages
# Description : Namespace Package
# =============================================================================

# Example
import sys

sys.path.extend(["location_A", "location_B"])

import company.sales.report
import company.accounts.invoice

print(company.__path__)


#   How to recognize it?
import company

print(company.__name__)
print(company.__file__)
print(company.__spec__.origin)
print(list(company.__path__))

'''
OUTPUT : 
    company
    None
    None
    ['.../location_A/company', '.../location_B/company']
'''


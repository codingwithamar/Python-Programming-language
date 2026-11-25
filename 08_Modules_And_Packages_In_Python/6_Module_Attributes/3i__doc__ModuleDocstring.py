# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 3i__doc__ModuleDocstring.py
# Path    : Python-Programming-Language/08_Modules_And_Packages_In_Python/6_Module_Attributes/3i__doc__ModuleDocstring.py
# Subject : # Subject : Modules and Packages in Python
# Description :  __doc__ - Module Documentation - Advanced Example
# =============================================================================

# Uses the setup from section 0
import notice
import math
import inspect
import pathlib
import tempfile
import sys

# 1. Read the module docstring and the function docstring
print(notice.__doc__)                          # notice helpers: prices and discounts.
print(notice.total.__doc__)                    # Return the price with tax.
print(notice.Cart.__doc__)                     # None   (the class has no docstring)

# 2. Standard modules have docstrings too
print(math.__doc__.splitlines()[0])          # This module provides access to the mathematical functions defined by the C standard.
print(len(math.__doc__) > 0)                 # True

# 3. The cleaned text (indentation removed)
print(inspect.getdoc(notice))                  # notice helpers: prices and discounts.

# 4. A string that is not first is NOT the docstring
folder2 = tempfile.mkdtemp()
pathlib.Path(folder2, "late_doc.py").write_text(
    "import os\n"
    '"""This is NOT the module docstring."""\n'
)
sys.path.insert(0, folder2)
import late_doc
print(late_doc.__doc__)                      # None

# 5. A comment is not a docstring
pathlib.Path(folder2, "comment_only.py").write_text("# only a comment\nx = 1\n")
import comment_only
print(comment_only.__doc__)                  # None

# 6. A multi-line module docstring (a common style)
pathlib.Path(folder2, "report_tool.py").write_text(
    '"""Report tool.\n'
    "\n"
    "Functions:\n"
    "    build()  - create the report\n"
    "    send()   - email the report\n"
    '"""\n'
)
import report_tool
print(report_tool.__doc__)
# Report tool.
#
# Functions:
#     build()  - create the report
#     send()   - email the report

# 7. Use the docstring as the help text of a command line program
import argparse
parser = argparse.ArgumentParser(description=report_tool.__doc__.splitlines()[0])
print(parser.description)                    # Report tool.

# 8. In the running script, the docstring is available as __doc__ too
print(__doc__)                               # None here (this example file has no docstring)

# 9. Python run with the -OO flag removes docstrings
#    python -OO script.py   -> __doc__ becomes None

# 10. You can set a docstring by hand
notice.__doc__ = "New text."
print(notice.__doc__)                          # New text.


'''
OUTPUT : 
        Hello from class
        Notice For helpers: prices and discounts.
        Return the price with tax.
        None
        This module provides access to the mathematical functions
        True
        Notice For helpers: prices and discounts.
        None
        None
        Report tool.

        Functions:
            build()  - create the report
            send()   - email the report

        Report tool.
        None
        New text.
'''
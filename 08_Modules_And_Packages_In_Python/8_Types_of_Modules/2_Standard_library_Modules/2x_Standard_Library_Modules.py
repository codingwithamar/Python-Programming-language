# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 2x_Standard_Library_Modules.py
# Path    : Python-Programming-Language/08_Modules_And_Packages_In_Python/6_Types_of_Modules/2_Standard_library_Modules/2x_Standard_Library_Modules.py
# Subject : Modules and Packages in Python
# Description : Advanced Standard Library Modules
# =============================================================================

import sys
import json
import importlib.machinery

# 1. The official list of standard library names (Python 3.10+)
print("json" in sys.stdlib_module_names)        # True
print("requests" in sys.stdlib_module_names)    # False
print(len(sys.stdlib_module_names) > 100)       # True

# 2. Many standard modules are plain Python files you can read
print(json.__file__.endswith("__init__.py"))    # True   (json is a package)

# 3. Some are compiled C extensions. Python knows these file endings
print(importlib.machinery.SOURCE_SUFFIXES)      # ['.py']
print(importlib.machinery.BYTECODE_SUFFIXES)    # ['.pyc']
print(importlib.machinery.EXTENSION_SUFFIXES)   # e.g. ['.cpython-312-x86_64-linux-gnu.so', '.abi3.so', '.so']
                                                # (Windows uses .pyd; the text depends on your system)

# 4. The docs list the standard library by topic. Examples:
#    text and data: string, re, json, csv     numbers: math, random, statistics, decimal
#    files and OS: os, pathlib, shutil, glob  time: time, datetime, sched
#    concurrency: threading, multiprocessing, asyncio, concurrent.futures
#    tools: logging, argparse, unittest, subprocess, sqlite3

# 5. Python 3.13 removed some very old standard modules (PEP 594, the "dead batteries"),
#    for example cgi and telnetlib. Check the docs for your Python version.
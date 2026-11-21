# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : calculator.py
# Path    : Python-Programming-Language/08_Modules_And_Packages_In_Python/5_Types_of_Modules/1_Built_in_Modules/calculator.py
# Subject : Modules and Packages in Python
# Description : Built In Modules
# =============================================================================

import sys

# Get the Python version
print(sys.version)

# Get the platform information
print(sys.platform)

# Get the built-in module names
print(sys.builtin_module_names)

'''
OUTPUT :
3.14.4 (main, Aug 20 2026, 10:41:58) [GCC 15.2.0]
linux
('_abc', '_ast', '_bisect', '_blake2', '_codecs', '_collections', '_contextvars', 
'_csv', '_datetime', '_elementtree', '_functools', '_heapq', '_imp', '_io', '_json', 
'_locale', '_md5', '_opcode', '_operator', '_pickle', '_posixsubprocess', '_random', 
'_sha1', '_sha2', '_sha3', '_signal', '_socket', '_sre', '_stat', '_statistics', 
'_string', '_struct', '_suggestions', '_symtable', '_sysconfig', '_thread', '_tokenize',
'_tracemalloc', '_types', '_typing', '_warnings', '_weakref', 'array', 'atexit', 'binascii',
'builtins', 'cmath', 'errno', 'faulthandler', 'fcntl', 'gc', 'grp', 'itertools', 'marshal',
'math', 'posix', 'pwd', 'pyexpat', 'select', 'sys', 'syslog', 'time', 'unicodedata', 'zlib')
'''
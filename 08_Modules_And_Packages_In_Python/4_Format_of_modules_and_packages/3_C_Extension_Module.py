# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 3_C_Extension_Module.py
# Path    : Python-Programming-Language/08_Modules_And_Packages_In_Python/4_Format_of _modules_and_packages/3_C_Extension_Module.py
# Subject : Format of Modules and Packages
# Description : C Extension Module (.so / .pyd)
# =============================================================================

'''
***  Recognizing an Extension Module  ***
    import math
    import _socket

    print(math.__file__)
    print(_socket.__file__)

*** Exact paths and extensions depend on your installation, On a typical Linux CPython installation, output paths may look like ***
            *** If we run above then we get path of that File ***

    /usr/lib/python3.14/lib-dynload/math.cpython-314-x86_64-linux-gnu.so
    /usr/lib/python3.14/lib-dynload/_socket.cpython-314-x86_64-linux-gnu.so
'''

import math

print(math.sqrt(144))
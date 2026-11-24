# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 3_Third_Party_Modules.py
# Path    : Python-Programming-Language/08_Modules_And_Packages_In_Python/6_Types_of_Modules/3_Third_Party_Modules_or_Packages/3_Third_Party_Modules.py
# Subject : Modules and Packages in Python
# Description : Third Party Modules(install them with pip from PyPI (the Python Package Index)). 
# =============================================================================

#   $ pip install requests

import requests

response = requests.get("https://www.python.org")
print(response.status_code)      # 200

#   Check where it was installed:
import requests
print(requests.__file__)
# e.g. /home/amar/.venv/lib/python3.12/site-packages/requests/__init__.py

#   Common pip commands:
#   pip install requests            # install
#   pip install requests==2.31.0    # install an exact version
#   pip list                        # show everything installed
#   pip show requests               # version, location, dependencies
#   pip uninstall requests          # remove

#%% Basic Example
import numpy as np
a = np.array([1, 2, 3])

print(a * 2)


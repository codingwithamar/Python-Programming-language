# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 3x_Third_Party_Modules.py
# Path    : Python-Programming-Language/08_Modules_And_Packages_In_Python/6_Types_of_Modules/3x_Third_Party_Modules_or_Packages/3_Third_Party_Modules.py
# Subject : Modules and Packages in Python
# Description : Third Party Modules
# =============================================================================

import site
import sys
import importlib.metadata as metadata

# 1. Where third-party modules live
print(site.getsitepackages())                  # e.g. ['/usr/lib/python3/site-packages']

# 2. Is a package installed, and which version? (works for any installed package)
try:
    print(metadata.version("pip"))             # e.g. 24.0
except metadata.PackageNotFoundError:
    print("pip is not installed")

# 3. The pip name and the import name can differ
#    pip install pillow            ->  import PIL
#    pip install beautifulsoup4    ->  import bs4
#    pip install scikit-learn      ->  import sklearn
#    pip install PyYAML            ->  import yaml
print(metadata.packages_distributions().get("yaml"))   # ['PyYAML'] (only if it is installed)

# 4. Use a virtual environment to keep each project's packages separate
#    python -m venv .venv
#    source .venv/bin/activate         (Windows: .venv\Scripts\activate)
#    python -m pip install requests
#    python -m pip freeze > requirements.txt
#    python -m pip install -r requirements.txt

# 5. A virtual environment has its own site-packages
print(sys.prefix != sys.base_prefix)           # True inside a virtual environment

# 6. Third-party code can run on import, so install only from sources you trust.

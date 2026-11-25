# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 3_Standard_Library_Modules.py
# Path    : Python-Programming-Language/08_Modules_And_Packages_In_Python/6_Types_of_Modules/2_Standard_library_Modules/3_Standard_Library_Modules.py
# Subject : Modules and Packages in Python
# Description : Standard Library Modules
# =============================================================================

import math
import os
import json
from pathlib import Path
from datetime import datetime

# Mathematical operation
print(math.sqrt(25))

# Get current working directory
print(os.getcwd())

# Convert Python dictionary into JSON text
data = {"name": "Amar", "age": 30}
print(json.dumps(data))

# Get current date and time
print(datetime.now())

# Create a path object
file_path = Path("data.txt")
print(file_path.name)
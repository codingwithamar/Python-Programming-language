# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 6_delattr_BuiltIn_Function.py
# Path    : Python-Programming-Language/07_Functions_in_Python/02_Function_Categories/01_Built_in_functions/05_Object_Control_builtIn_functions/1_Function_Related_Utilities/6_delattr_BuiltIn_Function.py
# Subject : Built-in functions in python
# Description : delattr() - deletes an attribute using its name as a string.
# =============================================================================

from types import SimpleNamespace

def main():
    def task():
        pass

    task.retries = 3
    delattr(task, "retries")
    print(hasattr(task, "retries"))     # False

    # Remove secrets before saving or sharing
    config = SimpleNamespace(host="localhost", user="amar", password="secret")

    for name in ["password", "token"]:
        if hasattr(config, name):          # "token" does not exist, so it is skipped
            delattr(config, name)

    print(config)       # namespace(host='localhost', user='amar')

    class Session:
        def __init__(self):
            self.user = "amar"
            self.temp = "remove me"

    s = Session()
    delattr(s, "temp")
    print(vars(s))      # {'user': 'amar'}

if __name__ == "__main__":
    main()
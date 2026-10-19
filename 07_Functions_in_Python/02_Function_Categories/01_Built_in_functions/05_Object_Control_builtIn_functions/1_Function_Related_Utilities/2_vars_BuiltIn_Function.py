# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 2_vars_BuiltIn_Function.py
# Path    : Python-Programming-Language/07_Functions_in_Python/02_Function_Categories/01_Built_in_functions/05_Object_Control_builtIn_functions/1_Inspecting_and_changing_attributes/2_vars_BuiltIn_Function.py
# Subject : Built-in functions in python
# Description : vars() - Returns the __dict__ of an object: its own attributes as names with values.
# =============================================================================

def main():
    print("""Syntax : \nvars()\t\t\t# current scope \nvars(object)\t\t# available on that object
    """)

    x = 10
    print(vars()["x"])                 # 10 -> vars() with no argument works like locals()
    print("bit_length" in vars(int))   # True -> vars() of a class shows its own names

    try:
        vars(5)
    except TypeError as error:
        print("TypeError:", error)     # an int value has no __dict__


#%%
    import argparse
    import json

    # 1. Command-line arguments as a dictionary
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", default="localhost")
    parser.add_argument("--port", type=int, default=8080)

    args = parser.parse_args([])
    print(vars(args))             # {'host': 'localhost', 'port': 8080}

    # 2. Convert an object to JSON
    class Config:
        def __init__(self, host, port):
            self.host = host
            self.port = port

    cfg = Config("localhost", 8080)
    print(json.dumps(vars(cfg)))  # {"host": "localhost", "port": 8080}

    # 3. vars() is the real dictionary, so changing it changes the object
    vars(cfg)["port"] = 9090
    print(cfg.port)               # 9090

    # 4. Functions can hold attributes too
    def task():
        pass

    task.retries = 3
    print(vars(task))             # {'retries': 3}

if __name__ == "__main__":
    main()
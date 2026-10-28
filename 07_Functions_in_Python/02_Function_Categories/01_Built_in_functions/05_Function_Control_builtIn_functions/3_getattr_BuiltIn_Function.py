# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 3_getattr_BuiltIn_Function.py
# Path    : Python-Programming-Language/07_Functions_in_Python/02_Function_Categories/01_Built_in_functions/05_Object_Control_builtIn_functions/3_getattr_BuiltIn_Function.py
# Subject : Built-in functions in python
# Description : getattr() - getattr(obj, name, default) gets the value of an attribute using its name as a string.
# =============================================================================

def main():

    print(getattr("hello", "upper")())           # HELLO -> same as "hello".upper()
    print(getattr([1, 2, 2, 2, 3], "count")(2))     # 3
    print(getattr(5, "real"))                    # 5
    print(getattr("abc", "missing", "default"))  # default -> no error, because a default is given
    print(getattr(int, "__name__"))              # int

#%% Advanced Examples
import math

# 1. Choose a function by a text name (from config, user input, etc.)
for op in ["floor", "ceil", "sqrt"]:
    print(op, getattr(math, op)(10.5))
# floor 10
# ceil 11
# sqrt 3.24037034920393

# 2. Command dispatcher: replaces a long if/elif chain
class Handler:
    def do_start(self):
        return "Starting..."

    def do_stop(self):
        return "Stopping..."

    def do_unknown(self):
        return "Unknown command"

handler = Handler()

def run_command(command):
    method = getattr(handler, f"do_{command}", handler.do_unknown)
    return method()

print(run_command("start"))     # Starting...
print(run_command("delete"))    # Unknown command
print(run_command("stop"))      # stop

if __name__ == "__main__":
    main()
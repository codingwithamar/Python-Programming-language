# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 4_setattr_BuiltIn_Function.py
# Path    : Python-Programming-Language/07_Functions_in_Python/02_Function_Categories/01_Built_in_functions/05_Object_Control_builtIn_functions/1_Function_Related_Utilities/4_setattr_BuiltIn_Function.py
# Subject : Built-in functions in python
# Description : setattr() - setattr(obj, name, value) sets an attribute using its name as a string. If the attribute does not exist, it is created.
# =============================================================================

def main():
    print("Syntax : setattr(object, name, value)")

    task = lambda: "done"          # a function is an object, so it can hold attributes
    setattr(task, "retries", 3)
    print(task.retries)            # 3
    print(task())                  # done

    try:
        setattr("abc", "color", "red")     # built-in str does not allow new attributes
    except AttributeError:
        print("AttributeError: str cannot get new attributes")


if __name__ == "__main__":
    main()
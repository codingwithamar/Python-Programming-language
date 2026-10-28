# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 10_object_BuiltIn_Function.py
# Path    : Python-Programming-Language/07_Functions_in_Python/02_Function_Categories/01_Built_in_functions/05_Object_Control_builtIn_functions/10_object_BuiltIn_Function.py
# Subject : Built-in functions in python
# Description : Description
# =============================================================================

def main():
    o = object()

    print(type(o))                      # <class 'object'>
    print(isinstance(5, object))        # True
    print(isinstance("hi", object))     # True
    print(isinstance(len, object))      # True -> even functions are objects

    class User:
        pass

    print(issubclass(User, object))     # True -> User inherits from object automatically
    print(User.__mro__)                 # (<class '__main__.User'>, <class 'object'>)

    # A plain object() cannot hold new attributes
    try:
        o.name = "Amar"
    except AttributeError as error:
        print(error)                    # 'object' object has no attribute 'name'
#%%
    # 1. Unique "missing" marker, also called a sentinel
    MISSING = object()

    def get_setting(settings, key, default=MISSING):
        if key in settings:
            return settings[key]
        if default is MISSING:
            raise KeyError(f"'{key}' is required")
        return default

    config = {"debug": None}
    print(get_setting(config, "debug"))          # None -> the key exists, and None is its real value
    print(get_setting(config, "port", 8080))     # 8080
    # get_setting(config, "port") raises KeyError

    # 2. See what object gives to every class
    print([n for n in dir(object) if not n.startswith("__")])   # []  -> only special (dunder) names
    print([n for n in dir(object) if n in ("__init__", "__new__", "__repr__", "__str__",
                                        "__eq__", "__hash__", "__setattr__", "__getattribute__")])

    # 3. Default behavior that comes from object
    class Plain:
        pass

    a = Plain()
    b = Plain()
    print(a == b)                 # False -> default __eq__ compares identity
    print(a == a)                 # True
    print(hash(a) == hash(a))     # True -> default __hash__ is based on identity
    print(repr(a))                # <__main__.Plain object at 0x...> -> default __repr__

    # 4. Change a default by overriding it
    class Point:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def __repr__(self):
            return f"Point({self.x}, {self.y})"

        def __eq__(self, other):
            return self.x == other.x and self.y == other.y

        def __hash__(self):
            return hash((self.x, self.y))

    print(Point(1, 2))                      # Point(1, 2)
    print(Point(1, 2) == Point(1, 2))       # True
    print(len({Point(1, 2), Point(1, 2)}))  # 

if __name__ == "__main__":
    main()
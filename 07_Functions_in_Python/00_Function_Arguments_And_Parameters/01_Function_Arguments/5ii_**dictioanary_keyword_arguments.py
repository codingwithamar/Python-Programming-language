# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 5_dictioanary_keyword_arguments.py
# Path    : Python-Programming-Language/07_Functions_in_Python/00_Function_Arguments/5_dictioanary_keyword_arguments.py
# Subject : Enter Subject
# Description : **dictionary - Unpacking as a keyword arguments
# =============================================================================

def main():
#%% Basic Examples
    def add(a, b, c):
        return a + b + c

    data = {'a': 5, 'b': 10, 'c': 15}
    print(add(**data))                           # 30  -> same as add(a=5, b=10, c=15)

    print(add(**{'c': 15, 'a': 5, 'b': 10}))     # 30  -> the order of keys does not matter

#%% Advanced Examples
    from types import MappingProxyType

    # 1. Use a settings dictionary as the arguments
    def connect(host, port=8080, secure=False):
        return f"{host}:{port} secure={secure}"

    config = {"host": "example.com", "port": 9000}
    print(connect(**config))                     # example.com:9000 secure=False

    # 2. Combine several dictionaries (defaults first, overrides after)
    defaults = {"port": 9000}
    overrides = {"secure": True}
    print(connect("example.com", **defaults, **overrides))
    # example.com:9000 secure=True

    # 3. Any mapping works, not only dict
    read_only = MappingProxyType({"a": 1, "b": 2, "c": 3})
    def add(a, b, c):
        return a + b + c
    print(add(**read_only))                      # 6

    # 4. Fill a text template
    person = {"name": "Amar", "age": 25}
    print("{name} is {age} years old".format(**person))    # Amar is 25 years old

    # 5. Errors
    try:
        connect(**{"host": "a.com", "colour": "red"})        # key is not a parameter
    except TypeError as error:
        print(error)       # connect() got an unexpected keyword argument 'colour'

    try:
        connect(**{"port": 1})                               # required "host" is missing
    except TypeError as error:
        print(error)       # connect() missing 1 required positional argument: 'host'

    try:
        connect("a.com", **{"port": 1}, **{"port": 2})       # same key twice
    except TypeError as error:
        print(error)       # connect() got multiple values for keyword argument 'port'

    try:
        connect(**{"host": "a.com", 5: "x"})                 # a key that is not a string
    except TypeError:
        print("TypeError: keywords must be strings")

    # 6. The function gets its own copy of the pairs
    settings = {"debug": True}

    def change(**kwargs):
        kwargs["debug"] = False
        return kwargs

    print(change(**settings))                    # {'debug': False}
    print(settings)                              # {'debug': True} -> unchanged

    # 7. The same ** merges dictionaries when used in a dictionary literal (not a call)
    a = {"x": 1, "y": 2}
    b = {"y": 99, "z": 3}
    print({**a, **b})                            # {'x': 1, 'y': 99, 'z': 3}   (later value wins)

if __name__ == "__main__":
    main()
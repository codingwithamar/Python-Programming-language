# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 18_dict_coleection_function.py
# Path    : Python-Programming-Language/07_Functions_in_Python/02_Function_Categories/01_Built_in_functions/02_Object_Type_Handling_builtIn_functions/3_Collection_Functions/18_dict_coleection_function.py
# Subject : Collection Built-In Functions
# Description : dict() - Creates a dictionary, or converts suitable data into one.
# =============================================================================

def main():
    d1 = dict()                           # {}
    d2 = dict(name="Amar", age=25)          # {'name': 'Amar', 'age': 25}
    d3 = dict([("a", 1), ("b", 2)])          # {'a': 1, 'b': 2} -> from list of pairs

    # From two parallel lists using zip()
    keys = ["name", "age", "city"]
    values = ["Amar", 25, "Pune"]
    d4 = dict(zip(keys, values))
    print(d4)  # {'name': 'Amar', 'age': 25, 'city': 'Pune'}

    # dict.fromkeys() -> creating a dict with the same default value for every key
    settings = dict.fromkeys(["debug", "verbose", "cache"], False)
    print(settings)  # {'debug': False, 'verbose': False, 'cache': False}

    # Merging dictionaries (Python 3.9+)
    defaults = {"host": "localhost", "port": 8080}
    overrides = {"port": 9090}
    merged = defaults | overrides  # merge operator
    print(merged)  #{'host': 'localhost', 'port': 9090}

if __name__ == "__main__":
    main()
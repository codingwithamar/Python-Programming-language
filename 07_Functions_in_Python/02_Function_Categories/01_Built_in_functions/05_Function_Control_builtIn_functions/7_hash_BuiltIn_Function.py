# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 7_hash_BuiltIn_Function.py
# Path    : Python-Programming-Language/07_Functions_in_Python/02_Function_Categories/01_Built_in_functions/05_Object_Control_builtIn_functions/1_Function_Related_Utilities/7_hash_BuiltIn_Function.py
# Subject : Built-in functions in python
# Description : hasattr() - eturns an integer hash value for an object. Dictionaries and sets 
#                       use hash values to find items very fast.
# =============================================================================

def main():
    print(hash(42))                              # 42
    print(hash(1) == hash(1.0) == hash(True))    # True
    print(hash((1, 2)) == hash((1, 2)))          # True

    try:
        hash([1, 2])
    except TypeError as error:
        print(error)    # unhashable type: 'list'

    # Tuples and frozensets as dictionary keys
    visited = {(0, 0): "start", (0, 1): "step 1"}
    print(visited[(0, 0)])                       # start

    a = frozenset(["read", "write"])
    b = frozenset(["write", "read"])
    print(hash(a) == hash(b))                    # True
    print({a: "editor"}[b])                      # editor

    # A custom class made hashable
    class Point:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def __eq__(self, other):
            return self.x == other.x and self.y == other.y

        def __hash__(self):
            return hash((self.x, self.y))

    print(len({Point(1, 2), Point(1, 2)}))       
    # 1 -> the set sees them as the same item

if __name__ == "__main__":
    main()
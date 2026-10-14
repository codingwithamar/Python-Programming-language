# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 7_zip_BuiltIN_Function.py
# Path    : Python-Programming-Language/07_Functions_in_Python/02_Function_Categories/01_Built_in_functions/03_Data_Iteration_Processing_builtIn_functions/3_Combining_and_Transforming/7_zip_BuiltIN_Function.py
# Subject : Built-in functions in python
# Description : zip() - Combines items from two or more iterables, position by position, into tuples.
# =============================================================================

def main():
    names = ["Amar", "Sara", "Ravi"]
    ages = [25, 22, 30]

    for name, age in zip(names, ages):
        print(name, age)

    print(list(zip(names, ages)))
    # [('Amar', 25), ('Sara', 22), ('Ravi', 30)]

    # 1. zip stops at the SHORTEST iterable
    print(list(zip([1, 2, 3], ["a", "b"])))      # [(1, 'a'), (2, 'b')]

    # 2. strict=True (Python 3.10+) raises ValueError if lengths differ
    # list(zip([1, 2, 3], ["a", "b"], strict=True))   -> ValueError

    # 3. Keep all items using zip_longest
    from itertools import zip_longest
    print(list(zip_longest([1, 2, 3], ["a", "b"], fillvalue="-")))
    # [(1, 'a'), (2, 'b'), (3, '-')]

    # 4. Build a dictionary from two lists
    keys = ["host", "port"]
    values = ["localhost", 8080]
    print(dict(zip(keys, values)))       # {'host': 'localhost', 'port': 8080}

    # 5. Unzip: separate pairs back into two groups
    pairs = [(1, "a"), (2, "b"), (3, "c")]
    numbers, letters = zip(*pairs)
    print(numbers, letters)      # (1, 2, 3) ('a', 'b', 'c')

    # 6. Compare neighbors using an offset
    data = [3, 8, 15, 20]
    print([b - a for a, b in zip(data, data[1:])])      # [5, 7, 5]

if __name__ == "__main__":
    main()
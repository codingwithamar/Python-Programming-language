# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 14_list_Collection.py
# Path    : Python-Programming-Language/07_Functions_in_Python/02_Function_Categories/01_Built_in_functions/02_Object_Type_Handling_builtIn_functions/3_Collection_Functions/14_list_Collection.py
# Subject : Collection Built in Functions
# Description : list() - Creates a list, or converts another iterable into a list.
# =============================================================================

def main():
    l1 = list()             # []
    l2 = list("abc")        # ['a', 'b', 'c']
    l3 = list((1, 2, 3))    # [1, 2, 3] -> from a tuple

    # Converting other iterables
    l4 = list(range(5))                   # [0, 1, 2, 3, 4]
    l5 = list({"a": 1, "b": 2}.keys())    # ['a', 'b']
    l6 = list({3, 1, 2})                   # from a set -> order not guaranteed

    # Common use: making a copy of a list (shallow copy)
    original = [1, 2, 3]
    copy_list = list(original)
    copy_list.append(4)
    print(original, copy_list)     # [1, 2, 3] [1, 2, 3, 4] -> original unaffected


if __name__ == "__main__":
    main()
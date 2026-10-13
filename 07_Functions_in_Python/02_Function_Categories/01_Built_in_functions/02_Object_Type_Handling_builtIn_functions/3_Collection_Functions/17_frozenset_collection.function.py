# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 17_frozenset_collection.function.py
# Path    : Python-Programming-Language/07_Functions_in_Python/02_Function_Categories/01_Built_in_functions/02_Object_Type_Handling_builtIn_functions/3_Collection_Functions/17_frozenset_collection.function.py
# Subject : Collection Built-In Functions
# Description : frozenset() - Creates an immutable version of a set.
# =============================================================================

def main():
    fs = frozenset([1, 2, 3, 2, 1])
    print(fs)          # frozenset({1, 2, 3})
    # fs.add(4)        # AttributeError -> frozenset has no add()

    # Using frozenset as a dictionary key (only possible because it is hashable)
    permissions_cache = {
        frozenset(["read", "write"]): "editor",
        frozenset(["read"]): "viewer"
    }

    user_permissions = frozenset(["write", "read"])
    print(permissions_cache[user_permissions])
    # editor -> order inside frozenset doesn't matter

if __name__ == "__main__":
    main()
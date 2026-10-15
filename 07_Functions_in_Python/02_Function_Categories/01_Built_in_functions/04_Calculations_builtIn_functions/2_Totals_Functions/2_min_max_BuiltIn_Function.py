# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 2_min_BuiltIn_Function.py
# Path    : Python-Programming-Language/07_Functions_in_Python/02_Function_Categories/01_Built_in_functions/04_Calculations_builtIn_functions/2_Totals_Functions/2_min_BuiltIn_Function.py
# Subject : Built-in functions in python
# Description : min( ), max( ) - Return the smallest and the largest item.
# =============================================================================

def main():
    print("Syntax :\nmin(iterable, *, key=None, default=...)\nmin(a, b, c, ..., key=None)")

    print(min([4, 8, 1, 9]))      # 1
    print(max([4, 8, 1, 9]))      # 9
    print(min(5, 2, 8))           # 2 -> you can pass values directly
    print(max("apple", "banana")) # banana -> strings compare alphabetically

    # 1. key= decides what is compared
    words = ["pear", "fig", "banana", "kiwi"]
    print(max(words, key=len))      # banana
    print(min(words, key=len))      # fig

    # 2. Key with a dictionary: the name with the highest score
    scores = {"a": 3, "b": 9, "c": 5}
    print(max(scores, key=scores.get))     # b

    # 3. default= avoids an error on an empty iterable
    print(max([], default=0))       # 0
    # max([])    -> ValueError

    # 4. Ties: the FIRST item wins
    print(max(["ab", "cd", "ef"], key=len))     # ab

    # 5. Real automation use: find the newest log file
    from pathlib import Path
    newest = max(
        Path(".").glob("*.log"),
        key=lambda p: p.stat().st_mtime,
        default=None,
    )
    print(newest)       # the newest .log file, or None if there are none

    # 6. Mixed types cannot be compared
    # max([1, "a"])      -> TypeError

if __name__ == "__main__":
    main()
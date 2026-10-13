# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 4_next_BuiltIN_Function.py
# Path    : Python-Programming-Language/07_Functions_in_Python/02_Function_Categories/01_Built_in_functions/03_Data_Iteration_Processing_builtIn_functions/2_Iterator_BuiltIN_Functions/4_next_BuiltIN_Function.py
# Subject : Built-in functions in python
# Description : next() - Gets the next item from an iterator.
# =============================================================================

def main():
# Syntax - next(iterator, default) 
    it = iter(["a", "b"])
    print(next(it))             # a
    print(next(it))             # b
    print(next(it, "empty"))    # empty -> default is returned instead of an error

#%%Example 1 : Find the First Match

    files = ["a.txt", "b.csv", "c.csv", "d.json"]

    first_csv = next((f for f in files if f.endswith(".csv")), None)
    print(first_csv)       # b.csv

    none_found = next((f for f in files if f.endswith(".xml")), None)
    print(none_found)      # None
    # This stops at the first match. It does not build a whole list, so it is faster than [f for f in files if ...][0].

#%% Example 2 : Skip the header row of a file
    with open("data.csv") as f:
        header = next(f)       # reads the first line only
        for line in f:         # continues from the second line
            print(line.strip())

if __name__ == "__main__":
    main()
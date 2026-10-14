# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 10_all_and_any_BuiltIN_Functions.py
# Path    : Python-Programming-Language/07_Functions_in_Python/02_Function_Categories/01_Built_in_functions/03_Data_Iteration_Processing_builtIn_functions/4_Testing_Ordering_Slicing/10_all_and_any_BuiltIN_Functions.py
# Subject : Import functions in python
# Description : all(iterable) returns True if every item is true.
#               any(iterable) returns True if at least one item is true.
# =============================================================================

def main():
    print(all([1, 2, 3]))        # True
    print(all([1, 0, 3]))        # False -> 0 is false
    print(any([0, 0, 5]))        # True
    print(any([0, "", None]))    # False
#%%
    import os

    # Check that ALL required files exist before starting a job
    required = ["config.json", "data.csv", "template.txt"]
    if all(os.path.exists(p) for p in required):
        print("Ready to run")
    else:
        print("Missing files")

    # Check if ANY file is too old
    ages_in_days = [2, 5, 40, 1]
    print(any(age > 30 for age in ages_in_days))     # True

    # Short-circuit: stops at the first deciding item
    def check(x):
        print("checking", x)
        return x > 0

    print(any(check(x) for x in [5, -1, 3]))    # prints "checking 5" then True; the rest are not checked

    # IMPORTANT empty-iterable rules
    print(all([]))     # True  -> nothing is false
    print(any([]))     # False -> nothing is true

if __name__ == "__main__":
    main()
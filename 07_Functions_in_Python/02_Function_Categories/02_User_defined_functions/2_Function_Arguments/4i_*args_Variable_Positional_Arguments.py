# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 4_i_args_Variable_Positional_Arguments.py
# Path    : Python-Programming-Language/07_Functions_in_Python/00_Function_Arguments/4_i_args_Variable_Positional_Arguments.py
# Subject : Function arguments in python
# Description : Variables length Arguments (Packing) i) *args : Variables Positional Arguments (Packing)
# =============================================================================

def main():
#%% Basic Concept
    def add_all(*numbers):
        return sum(numbers)

    # numbers = map(int, input("Enter the numbers: ").split())      # can take values using lambda function

    numbers = input("Enter the numbers : ").split()

    numbers = [int(num) for num in numbers]

    print(add_all(*numbers))

#%% Basic Examples
    def add_all(*numbers):
        print(numbers)             # (1, 2, 3)
        print(type(numbers))       # <class 'tuple'>
        return sum(numbers)

    print(add_all(1, 2, 3))        # 6
    print(add_all(10, 20))         # 30
    print(add_all())               # 0  -> no arguments gives an empty tuple ()

# %% Advanced Examples
    def report(title, *items, separator=", "):
        return f"{title}: {separator.join(map(str, items))}"

    print(report("Files", "a.txt", "b.txt", "c.txt"))
    # Files: a.txt, b.txt, c.txt

    print(report("Numbers", 1, 2, 3, separator=" | "))
    # Numbers: 1 | 2 | 3

    # Important: parameters after *args can only be given by keyword
    # report("Files", "a.txt", ", ")     # the ", " becomes part of items, not the separator

if __name__ == "__main__":
    main()
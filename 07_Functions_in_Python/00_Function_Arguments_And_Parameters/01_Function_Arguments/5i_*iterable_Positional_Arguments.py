# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 5_.py
# Path    : Python-Programming-Language/07_Functions_in_Python/00_Function_Arguments/5_.py
# Subject : Function arguments in python
# Description : *iterable - Unpacking as a positional arguments
# =============================================================================

def main():
#%% Basic Example
    def add(a, b, c):
        return a + b + c

    nums = [1, 2, 3]
    print(add(*nums))              # 6  -> same as add(1, 2, 3)

    point = (4, 5, 6)
    print(add(*point))             # 15 -> a tuple works too

#%% Advanced Examples
    import os
    from datetime import date

    # 1. Any iterable works
    def show(a, b, c):
        return f"{a}-{b}-{c}"

    print(show(*"xyz"))                          # x-y-z
    print(show(*range(3)))                       # 0-1-2
    print(show(*(n * n for n in range(3))))      # 0-1-4

    # 2. Several unpackings plus normal arguments in one call (Python 3.5+)
    def connect(host, port, timeout, retries):
        return (host, port, timeout, retries)

    print(connect("a.com", *[80, 30], *[3]))     # ('a.com', 80, 30, 3)
    print(connect(*["a.com", 80], 30, 3))        # ('a.com', 80, 30, 3)

    # 3. Built-in functions that are used with *
    items = ["apple", "banana", "mango"]
    print(*items)                                # apple banana mango
    print(*items, sep=", ")                      # apple, banana, mango
    print(max(*[3, 9, 4]))                       # 9
    print(os.path.join(*["data", "reports", "a.csv"]))   # data/reports/a.csv (Linux/Mac)
    print(date(*(2026, 11, 2)))                  # 2026-11-02

    # 4. Unzip (transpose) with zip(*...)
    pairs = [(1, "a"), (2, "b"), (3, "c")]
    numbers, letters = zip(*pairs)
    print(numbers, letters)                      # (1, 2, 3) ('a', 'b', 'c')

    # 5. Feed a function that has *args
    def total(*values):
        return sum(values)

    print(total(*[1, 2, 3], 4))                  # 10

    # 6. A generator is used up by unpacking
    gen = (n for n in range(3))
    print(show(*gen))                            # 0-1-2
    print(list(gen))                             # []  -> already consumed

    # 7. Count mismatch gives TypeError
    try:
        add(*[1, 2])
    except TypeError as error:
        print(error)       # add() missing 1 required positional argument: 'c'

    try:
        add(*[1, 2, 3, 4])
    except TypeError as error:
        print(error)       # add() takes 3 positional arguments but 4 were given

if __name__ == "__main__":
    main()
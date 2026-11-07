# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 03_Recursion.py
# Path    : Python-Programming-Language/07_Functions_in_Python/02_Function_Categories/02_User_defined_functions/4_Function_as_a_Tools/03_Recursion.py
# Subject : User Defined Function
# Description : Recursion
# =============================================================================

def main():
#%% Basic Concept
    # Factorial Using Loop
    n = 5
    factorial = 1

    for i in range(1, n + 1):
        factorial *= i

    print(factorial)        # Output: 120

    # Factorial Using Recursion
    def factorial(n):
        if n == 0 or n == 1:
            return 1

        return n * factorial(n - 1)


    print(factorial(5))     # Output: 120

    # Fcatorial Using math.factorial()

    import math

    print(math.factorial(5))

    # Output: 120

#%% Basic Example
    def factorial(n):
        if n == 0 or n == 1:           # base case
            return 1
        return n * factorial(n - 1)    # recursive case

    print(factorial(5))                # 120

    def countdown(n):
        if n == 0:                     # base case
            print("Go!")
            return
        print(n)
        countdown(n - 1)               # smaller problem

    countdown(3)                       # 3 2 1 Go!

#%% Advanced Examples
    import sys
    import json
    from functools import lru_cache

    # 1. Count files in a nested folder structure
    def count_files(folder):
        count = 0
        for name, content in folder.items():
            if isinstance(content, dict):
                count += count_files(content)      # go inside the sub folder
            else:
                count += 1                         # it is a file
        return count

    structure = {
        "report.csv": None,
        "data": {
            "a.json": None,
            "old": {"log.txt": None, "image.png": None},
        },
    }
    print(count_files(structure))                  # 4

    # 2. Flatten nested lists
    def flatten(items):
        result = []
        for item in items:
            if isinstance(item, list):
                result.extend(flatten(item))
            else:
                result.append(item)
        return result

    print(flatten([1, [2, [3, 4]], 5, [[6]]]))     # [1, 2, 3, 4, 5, 6]

    # 3. Walk a real folder tree
    from pathlib import Path

    def list_python_files(folder):
        for item in Path(folder).iterdir():
            if item.is_dir():
                yield from list_python_files(item)     # recursion inside a generator
            elif item.suffix == ".py":
                yield item
    # for f in list_python_files("."): print(f)

    # 4. Find a key in nested JSON data
    def find_key(data, target):
        if isinstance(data, dict):
            for key, value in data.items():
                if key == target:
                    return value
                found = find_key(value, target)
                if found is not None:
                    return found
        elif isinstance(data, list):
            for item in data:
                found = find_key(item, target)
                if found is not None:
                    return found
        return None

    doc = json.loads('{"a": {"b": [{"c": 42}]}}')
    print(find_key(doc, "c"))                      # 42

    # 5. Divide and conquer: binary search
    def binary_search(items, target, low=0, high=None):
        if high is None:
            high = len(items) - 1
        if low > high:                             # base case: not found
            return -1
        mid = (low + high) // 2
        if items[mid] == target:                   # base case: found
            return mid
        if items[mid] < target:
            return binary_search(items, target, mid + 1, high)
        return binary_search(items, target, low, mid - 1)

    print(binary_search([1, 3, 5, 7, 9, 11], 7))   # 3

    # 6. Merge sort (divide and conquer)
    def merge_sort(items):
        if len(items) <= 1:                        # base case
            return items
        mid = len(items) // 2
        left = merge_sort(items[:mid])
        right = merge_sort(items[mid:])
        merged = []
        while left and right:
            merged.append(left.pop(0) if left[0] <= right[0] else right.pop(0))
        return merged + left + right

    print(merge_sort([5, 2, 9, 1, 7]))             # [1, 2, 5, 7, 9]

    # 7. Power set / permutations are natural recursion; here is a simple sum
    def total(numbers):
        if not numbers:                            # base case
            return 0
        return numbers[0] + total(numbers[1:])

    print(total([1, 2, 3, 4]))                     # 10

    # 8. The recursion limit
    print(sys.getrecursionlimit())                 # 1000 (default)

    def forever(n):
        return forever(n + 1)                      # no base case

    try:
        forever(0)
    except RecursionError as error:
        print("RecursionError:", error)            # maximum recursion depth exceeded

    # 9. Slow recursion made fast with caching
    def slow_fib(n):
        return n if n < 2 else slow_fib(n - 1) + slow_fib(n - 2)   # repeats the same work

    @lru_cache(maxsize=None)
    def fast_fib(n):
        return n if n < 2 else fast_fib(n - 1) + fast_fib(n - 2)

    print(fast_fib(50))                            # 12586269025 (instant)
    print(fast_fib.cache_info())

    # 10. The same idea with a loop (no limit problem)
    def fib_loop(n):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a

    print(fib_loop(50))                            # 12586269025

    # 11. Convert deep recursion into a loop with a stack
    def count_files_loop(folder):
        stack = [folder]
        count = 0
        while stack:
            current = stack.pop()
            for content in current.values():
                if isinstance(content, dict):
                    stack.append(content)
                else:
                    count += 1
        return count

    print(count_files_loop(structure))             # 4

    # 12. Mutual recursion (two functions calling each other)
    def is_even(n):
        return True if n == 0 else is_odd(n - 1)

    def is_odd(n):
        return False if n == 0 else is_even(n - 1)

    print(is_even(10), is_odd(7))                  # True True

if __name__ == "__main__":
    main()
# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 11_sorted_BuiltIN_Function.py
# Path    : Python-Programming-Language/07_Functions_in_Python/02_Function_Categories/01_Built_in_functions/03_Data_Iteration_Processing_builtIn_functions/4_Testing_Ordering_Slicing/11_sorted_BuiltIN_Function.py
# Subject : Built-in functions in python
# Description : sorted() - Returns a new sorted list from any iterable. The original is not changed.
# =============================================================================

def main():
    print("Syntax : sorted(iterable, key=None, reverse=False)")

    print(sorted([3, 1, 2]))                 # [1, 2, 3]
    print(sorted([3, 1, 2], reverse=True))   # [3, 2, 1]
    print(sorted("hello"))                   # ['e', 'h', 'l', 'l', 'o']
    print(sorted(["banana", "apple", "cherry"]))   # ['apple', 'banana', 'cherry']

    # 1. key= decides what to compare
    words = ["pear", "fig", "banana", "kiwi"]
    print(sorted(words, key=len))             # ['fig', 'pear', 'kiwi', 'banana']

    # 2. Case-insensitive sort
    names = ["bob", "Alice", "charlie"]
    print(sorted(names))                       # ['Alice', 'bob', 'charlie']
    print(sorted(names, key=str.lower))        # ['Alice', 'bob', 'charlie'] -> compared in lower case

    # 3. Sort by more than one rule: department A to Z, then salary high to low
    employees = [
        {"name": "Amar", "dept": "IT", "salary": 50},
        {"name": "Sara", "dept": "HR", "salary": 40},
        {"name": "Ravi", "dept": "IT", "salary": 70},
    ]
    result = sorted(employees, key=lambda e: (e["dept"], -e["salary"]))
    for e in result:
        print(e["dept"], e["salary"], e["name"])
    # HR 40 Sara
    # IT 70 Ravi
    # IT 50 Amar

    # 4. operator.itemgetter is a faster, cleaner key for dicts and tuples
    from operator import itemgetter
    print(sorted(employees, key=itemgetter("salary")))

    # 5. Sorting a dictionary by value
    scores = {"a": 3, "b": 1, "c": 2}
    print(sorted(scores.items(), key=lambda item: item[1]))   # [('b', 1), ('c', 2), ('a', 3)]

if __name__ == "__main__":
    main()
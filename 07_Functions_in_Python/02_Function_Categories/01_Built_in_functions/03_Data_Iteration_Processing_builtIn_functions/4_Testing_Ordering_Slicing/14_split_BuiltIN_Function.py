# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 14_split_BuiltIN_Function.py
# Path    : Python-Programming-Language/07_Functions_in_Python/02_Function_Categories/01_Built_in_functions/03_Data_Iteration_Processing_builtIn_functions/4_Testing_Ordering_Slicing/14_split_BuiltIN_Function.py
# Subject : Built-in functions in python
# Description : split() - split() breaks a string into a list of smaller strings, 
# cutting it at a separator you choose. If you don’t give a separator, it cuts at whitespace (spaces, tabs, new lines).
# =============================================================================

def main():
    text = "Python is easy to learn"
    words = text.split()
    print(words)   # ['Python', 'is', 'easy', 'to', 'learn']

    date = "2026-10-14"
    parts = date.split("-")
    print(parts)   # ['2026', '10', '14']

    # 1. Using maxsplit to split only the first few times
    line = "name=Amar=Pune"
    print(line.split("=", 1))   # ['name', 'Amar=Pune']
    # Useful for key=value pairs where the value itself may contain "="

    # 2. Parsing CSV-style data and unpacking into variables
    record = "Amar,21,Pune"
    name, age, city = record.split(",")
    print(name, age, city)   # Amar 21 Pune

    # Converting the numeric part right away
    age = int(record.split(",")[1])
    print(age + 1)   # 22

    # 3. Reading a file and splitting every line
    with open("students.csv") as f:
        for line in f:
            name, age, city = line.strip().split(",")
            print(f"{name} is {age} years old and lives in {city}")

    # 4. Converting a line of numbers typed by the user into a list of ints
    numbers = "10 20 30 40"
    nums = list(map(int, numbers.split()))
    print(nums)        # [10, 20, 30, 40]
    print(sum(nums))   # 100

    # split() vs split(" ")
    text = "a   b    c"
    print(text.split())      # ['a', 'b', 'c']                  -> extra spaces ignored
    print(text.split(" "))   # ['a', '', '', 'b', '', '', '', 'c']  -> empty strings appear

if __name__ == "__main__":
    main()
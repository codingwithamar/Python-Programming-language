# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 9_filter_BuiltIN_Function.py
# Path    : Python-Programming-Language/07_Functions_in_Python/02_Function_Categories/01_Built_in_functions/03_Data_Iteration_Processing_builtIn_functions/3_Combining_and_Transforming/9_filter_BuiltIN_Function.py
# Subject : Import functions in python
# Description : filter() - Keeps only the items for which a function returns a true value.
# =============================================================================

def main():
    print("Syntax : filter(function, iterable)")
    numbers = [1, 2, 3, 4, 5, 6]
    evens = list(filter(lambda x: x % 2 == 0, numbers))
    print(evens)         # [2, 4, 6]

    # 1. filter(None, ...) keeps only truthy items
    data = [0, 1, "", "text", None, [], [0], False]
    print(list(filter(None, data)))        # [1, 'text', [0]]

    # 2. Filter files by extension
    files = ["a.txt", "b.csv", "c.csv", "d.json"]
    csv_files = list(filter(lambda f: f.endswith(".csv"), files))
    print(csv_files)        # ['b.csv', 'c.csv']

    # 3. Use a named function for more complex rules
    def is_valid_email(text):
        return "@" in text and "." in text.split("@")[-1]

    emails = ["a@x.com", "bad-email", "b@y.org"]
    print(list(filter(is_valid_email, emails)))     # ['a@x.com', 'b@y.org']

    # 4. Same result with a list comprehension
    print([e for e in emails if is_valid_email(e)])

if __name__ == "__main__":
    main()
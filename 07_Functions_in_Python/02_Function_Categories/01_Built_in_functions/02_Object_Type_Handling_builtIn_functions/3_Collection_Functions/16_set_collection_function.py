# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 16_set_collection_function.py
# Path    : Python-Programming-Language/07_Functions_in_Python/02_Function_Categories/01_Built_in_functions/02_Object_Type_Handling_builtIn_functions/3_Collection_Functions/16_set_collection_function.py
# Subject : Collection Built-In Functions
# Description : set() - Creates a set, or converts an iterable into a set, removing duplicates.
# =============================================================================

def main():
    s1 = set()                       # empty set -> NOTE: {} is an empty dict, not a set
    s2 = set([1, 2, 2, 3])            # {1, 2, 3} -> duplicates removed
    s3 = set("hello")                  # {'h', 'e', 'l', 'o'} -> unique characters only

    # Removing duplicates while keeping it simple
    emails = ["a@x.com", "b@x.com", "a@x.com", "c@x.com"]
    unique_emails = set(emails)
    print(unique_emails)              # {'a@x.com', 'b@x.com', 'c@x.com'}

    # Finding duplicates
    from collections import Counter
    counts = Counter(emails)
    duplicates = [email for email, count in counts.items() if count > 1]
    print(duplicates)                  # ['a@x.com']
    
if __name__ == "__main__":
    main()
# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 04_len_function.py
# Path    : Python-Programming-Language/07_Functions_in_Python/02_Function_Ctaegories/01_Built_in_functions/04_len_function.py
# Subject : Built-in functions in python
# Description : len() : Returns the number of items in an object
# =============================================================================

def main():
# %% Example 1 : Basic
    #   Syntax : len(object)
    name = "Amar"
    print(len(name))   # 4

    nums = [10, 20, 30, 40]
    print(len(nums))   # 4

    student = {"name": "Amar", "age": 21}
    print(len(student))   # 2 (counts keys, not values)

# %% Example 2 : Check validation using len()

def check_password(password):
    if len(password) > 8:
        print("High length")
    elif len(password) < 8:
        print("too short")
    else:
        return "valid length"

print(check_password("Amar1234"))

if __name__ == "__main__":
    main()
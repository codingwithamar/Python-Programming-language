# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 07_membership_operator.py
# Path    : Python-Programming-Language/05_Operators_in_python/07_membership_operator.py
# Subject : Membership Operator
# Description : Check value present or not ( in, not in)
# =============================================================================

def main():
    fruits = ["apple", "banana", "mango"]
    print("apple" in fruits)      # True
    print("grape" not in fruits)  # True

    allowed_ext = {".csv", ".json", ".txt"}
    filename = "report.csv"
    ext = filename[filename.rfind("."):]
    if ext not in allowed_ext:
        raise ValueError(f"{ext!r} not supported")
    print(f"{filename!r} is valid")

if __name__ == "__main__":
    main()
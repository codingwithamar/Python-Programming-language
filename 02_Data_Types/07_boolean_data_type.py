# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 07_boolean_data_type.py
# Path    : 02_Data_Types\07_boolean_data_type.py
# Subject : Boolean Data Type
# Description : The bool data type represents truth values, mainly used in decision making and conditional statements. 
# =============================================================================

def heading(text):
    print("=" * 60)
    print(text)
    print("=" * 60)

def main():
    # ------------------------------------------------------------
    # 1. Real-world eligibility check
    # ------------------------------------------------------------
    heading("1. Real-world eligibility check")
    age = 20
    is_adult = age >= 18
    print(f"is_adult = {is_adult!r}, type = {type(is_adult)!r}")

    # ------------------------------------------------------------
    # 2. bool is a subtype of int
    # ------------------------------------------------------------
    heading("2. bool is a subtype of int")
    print(f"isinstance(True, int) = {isinstance(True, int)!r}")
    print(f"True + True = {True + True!r}")
    print(f"True == 1 -> {True == 1!r}, False == 0 -> {False == 0!r}")

    # ------------------------------------------------------------
    # 3. Counting True values with sum() (best trick example)
    # ------------------------------------------------------------
    heading("3. Counting True values with sum()")
    scores = [85, 40, 92, 55, 78]
    passing = [s >= 60 for s in scores]
    print(f"passing = {passing!r}")
    print(f"{sum(passing)} students passed")

    # ------------------------------------------------------------
    # 4. Truthiness table - bool() conversion
    # ------------------------------------------------------------
    heading("4. Truthiness table - bool() conversion")
    values = [0, 1, "", "hi", [], [1], None]
    for v in values:
        print(f"bool({v!r}) = {bool(v)!r}")

if __name__ == "__main__":
    main()
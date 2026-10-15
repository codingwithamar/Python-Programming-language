# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 1_sum_BuiltIn_Function.py
# Path    : Python-Programming-Language/07_Functions_in_Python/02_Function_Categories/01_Built_in_functions/04_Calculations_builtIn_functions/2_Totals_Functions/1_sum_BuiltIn_Function.py
# Subject : Built-in functions in python
# Description : sum( ) - Adds all items of an iterable.
# =============================================================================

def main():
    print(sum([1, 2, 3, 4]))         # 10
    print(sum([1, 2, 3], 10))        # 16 -> starts from 10
    print(sum(range(1, 101)))        # 5050

    # 1. Counting with sum (True counts as 1)
    scores = [45, 80, 92, 30, 67]
    passed = sum(score >= 50 for score in scores)
    print(passed)        # 3

    # 2. Average
    print(sum(scores) / len(scores))      # 62.8

    # 3. Total of dictionary values
    sales = {"jan": 100, "feb": 150, "mar": 120}
    print(sum(sales.values()))            # 370

    # 4. Float errors add up
    print(sum([0.1] * 10))                # 0.9999999999999999
    import math
    print(math.fsum([0.1] * 10))          # 1.0 -> fsum is more accurate

    # 5. Strings are not allowed
    # sum(["a", "b"])        -> TypeError
    print("".join(["a", "b"]))            # ab -> use join for strings

    # 6. Joining lists with sum works, but it is slow for large data
    print(sum([[1, 2], [3, 4]], []))      # [1, 2, 3, 4]
    # For big data, use itertools.chain instead

if __name__ == "__main__":
    main()

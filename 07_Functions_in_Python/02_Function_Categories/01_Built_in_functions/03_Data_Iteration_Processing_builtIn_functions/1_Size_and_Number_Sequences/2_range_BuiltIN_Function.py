# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 2_range_BuiltIN_Function.py
# Path    : Python-Programming-Language/07_Functions_in_Python/02_Function_Categories/01_Built_in_functions/03_Data_Iteration_Processing_builtIn_functions/1_Size_and_Number_Sequences/2_range_BuiltIN_Function.py
# Subject : Built-in functions in python
# Description : range() - Creates a lazy sequence of integers.
# =============================================================================

def main():
    # Syntax
    range(stop)
    range(start, stop)
    range(start, stop, step)

    print(list(range(5)))          # [0, 1, 2, 3, 4]
    print(list(range(2, 6)))       # [2, 3, 4, 5]
    print(list(range(0, 10, 2)))   # [0, 2, 4, 6, 8]

for i in range(3):
    print(i)                   # 0 1 2

# Counting down with a negative step
print(list(range(10, 0, -2)))      # [10, 8, 6, 4, 2]

# range is a real sequence: it supports len, indexing, slicing, and 'in'
r = range(0, 100, 5)
print(len(r))          # 20
print(r[3])            # 15
print(r[-1])           # 95
print(r[2:5])          # range(10, 25, 5)
print(50 in r)         # True

# Membership test is fast, even for huge ranges (nrangeo loop is run)
print(10**12 in range(0, 10**15, 2))     # True, answered instantly

# Memory is tiny, no matter how large the range is
big = range(10**9)
print(len(big))        # 1000000000

# Float values are not allowed
# range(0, 1, 0.1)     -> TypeError
# range(0, 10, 0)      -> ValueError: step cannot be zero

if __name__ == "__main__":
    main()
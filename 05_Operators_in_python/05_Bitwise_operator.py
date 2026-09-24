# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 05_Bitwise_operator.py
# Path    : Python-Programming-Language/05_Operators_in_python/05_Bitwise_operator.py
# Subject : Bitwise Operator
# Description : Operate binary bit(& | ^ ~ << >>)
# =============================================================================

def main():
    a = 6      # 110
    b = 3      # 011
    print(a & b)   # 2  (010) AND
    print(a | b)   # 7  (111) OR
    print(a ^ b)   # 5  (101) XOR
    print(a << 1)  # 12 (left shift → *2)
    print(a >> 1)  # 3  (right shift → /2)

    READ = 1    # 001
    WRITE = 2   # 010
    EXECUTE = 4 # 100

    permissions = READ | WRITE   # combine flags → 011 (3)
    can_write = bool(permissions & WRITE)
    print(f"{permissions=!r}, {can_write=!r}")

if __name__ == "__main__":
    main()
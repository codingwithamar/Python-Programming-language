# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 8_bin_9_oct_10_hex_BuiltIn_Functions.py
# Path    : Python-Programming-Language/07_Functions_in_Python/02_Function_Categories/01_Built_in_functions/04_Calculations_builtIn_functions/3_Numbers_and_Unicodes_Functions/8_bin_9_oct_10_hex_BuiltIn_Functions.py
# Subject : Built-in functions in python
# Description : 8. bin(), 9. oct(), 10. hex() - Convert an integer into a string in binary (base 2), 
# octal (base 8), or hexadecimal (base 16). The strings start with a prefix: 0b, 0o, 0x.
# =============================================================================

def main():
    print(bin(10))       # 0b1010
    print(oct(64))       # 0o100
    print(hex(255))      # 0xff
    print(bin(-5))       # -0b101

    # Back to integers
    print(int("1010", 2))     # 10
    print(int("ff", 16))      # 255
    print(int("0xff", 16))    # 255 -> prefix is allowed

    # 1. Remove the prefix, or use format codes for clean output
    print(bin(10)[2:])               # 1010
    print(format(10, "b"))           # 1010
    print(f"{5:08b}")                # 00000101 -> 8 digits, padded with zeros
    print(f"{255:X}")                # FF (upper case)

    # 2. Writing numbers directly in other bases
    print(0b1010, 0o17, 0xFF)        # 10 15 255

    # 3. File permissions (octal is natural here)
    import os, stat
    os.chmod("script.sh", 0o755)
    mode = os.stat("script.sh").st_mode
    print(oct(stat.S_IMODE(mode)))   # 0o755

    # 4. Bit flags
    READ, WRITE, EXECUTE = 0b100, 0b010, 0b001
    permission = READ | WRITE
    print(bool(permission & WRITE))      # True
    print(bool(permission & EXECUTE))    # False

    # 5. RGB color to a web color code
    r, g, b = 255, 128, 0
    print(f"#{r:02x}{g:02x}{b:02x}")     # #ff8000

    # 6. These functions accept integers only
    # hex(3.5)    -> TypeError


if __name__ == "__main__":
    main()
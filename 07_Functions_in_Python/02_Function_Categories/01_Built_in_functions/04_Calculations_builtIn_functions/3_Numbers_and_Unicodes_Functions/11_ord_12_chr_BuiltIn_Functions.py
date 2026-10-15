# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 11_ord_12_chr_BuiltIn_Functions.py
# Path    : Python-Programming-Language/07_Functions_in_Python/02_Function_Categories/01_Built_in_functions/04_Calculations_builtIn_functions/3_Numbers_and_Unicodes_Functions/11_ord_12_chr_BuiltIn_Functions.py
# Subject : Built-in functions in python
# Description : ord(char)- gives the Unicode number (code point) of one character.
#               chr(number) - gives the character for a Unicode number.
# =============================================================================

def main():
    print(ord("A"))      # 65
    print(ord("a"))      # 97
    print(chr(65))       # A
    print(chr(97))       # a
    print(ord("€"))      # 8364
    print(chr(8364))     # €

    # 1. Make a list of letters
    print([chr(c) for c in range(ord("a"), ord("e") + 1)])
    # ['a', 'b', 'c', 'd', 'e']

    # 2. Caesar cipher
    def shift(text, k):
        result = []
        for ch in text:
            if "a" <= ch <= "z":
                result.append(chr((ord(ch) - ord("a") + k) % 26 + ord("a")))
            else:
                result.append(ch)
        return "".join(result)

    print(shift("xyz", 3))       # abc

    # 3. Emoji and other characters outside normal letters
    print(chr(0x1F642))          # 🙂
    print(hex(ord("🙂")))        # 0x1f642

    # 4. Error cases
    # ord("ab")         -> TypeError: needs exactly one character
    # chr(-1)           -> ValueError
    # chr(1114112)      -> ValueError (the maximum is 0x10FFFF)

    # 5. Check if a character is a digit using numbers
    print(ord("0") <= ord("7") <= ord("9"))      # True

if __name__ == "__main__":
    main()
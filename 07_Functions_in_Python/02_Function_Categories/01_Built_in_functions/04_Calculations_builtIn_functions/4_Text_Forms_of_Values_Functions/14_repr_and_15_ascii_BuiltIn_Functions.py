# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 14_repr_and_15_ascii_BuiltIn_Functions.py
# Path    : Python-Programming-Language/07_Functions_in_Python/02_Function_Categories/01_Built_in_functions/04_Calculations_builtIn_functions/4_Text_Forms_of_Values_Functions/14_repr_and_15_ascii_BuiltIn_Functions.py
# Subject : Built-in functions in python
# Description : 14. repr() and 15. ascii() - repr(x) returns a string meant for developers. It should be clear and, if possible, valid Python code. 
# ascii(x) is the same as repr(x), but every non-ASCII character is changed into an escape code (\xe9, \u20ac, \U0001f642).
# =============================================================================

def main():
    print(repr("hello"))        # 'hello' -> with quotes
    print(repr(42))             # 42
    print(repr(None))           # None
    print(repr("line1\nline2")) # 'line1\nline2' -> the \n is shown, not used

    print(ascii("héllo"))       # 'h\xe9llo'
    print(ascii("🙂"))          # '\U0001f642'

    import datetime

    # 1. str() is for users, repr() is for developers
    d = datetime.date(2026, 10, 14)
    print(str(d))        # 2026-10-14
    print(repr(d))       # datetime.date(2026, 10, 14)

    # 2. repr() can often be pasted back as code
    numbers = [1, 2, 3]
    print(eval(repr(numbers)) == numbers)       # True

    # 3. Items inside a list are shown with repr()
    print(["a", "b"])      # ['a', 'b'] -> quotes are visible
    print("a", "b")        # a b

    # 4. Your own class
    class Point:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def __repr__(self):
            return f"Point({self.x}, {self.y})"

    p = Point(1, 2)
    print(repr(p))          # Point(1, 2)
    print(p)                # Point(1, 2) -> print() uses __repr__ because __str__ is missing
    print([p, p])           # [Point(1, 2), Point(1, 2)]

    # Without __repr__, you get something unhelpful:
    class Plain:
        pass
    print(repr(Plain()))    # <__main__.Plain object at 0x...>

    # 5. Useful for logs: it shows hidden characters
    filename = "report.csv \n"
    print("File:", filename)         # hard to see the problem
    print("File:", repr(filename))   # File: 'report.csv \n' -> problem is visible


if __name__ == "__main__":
    main()
# ================================================================================
# Author  : codingwithamar@gmail.com
# File    : 02_text_data_types.py
# Path    : python_system_programming/02_Data_Types/
# Subject : Text Sequence Type — str (String) in Python
# Ref     : https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str
# =================================================================================

"""
str — Text Sequence Type
------------------------
- Textual data in Python is handled with str objects (strings).
- Strings are IMMUTABLE SEQUENCES of Unicode code points.
- Reference: docs.python.org/3/library/stdtypes.html#text-sequence-type-str
"""

# ─────────────────────────────────────────────
# SECTION 1 : Creating Strings — All Literal Forms
# ─────────────────────────────────────────────
print("=" * 60)
print(" SECTION 1 : String Creation — Literal Forms")
print("=" * 60)

s1 = 'single quotes'
s2 = "double quotes"
s3 = '''triple single — can span
multiple lines'''
s4 = """triple double — can also span
multiple lines"""

print(f"s1 = {s1!r}")
print(f"s2 = {s2!r}")
print(f"s3 = {s3!r}")
print(f"s4 = {s4!r}")
print(f"type(s1) = {type(s1)}")         # <class 'str'>

# str() Constructor — converting other types to string
print("\n-- str() Constructor --")
print(str(42))          # '42'
print(str(3.14))        # '3.14'
print(str(True))        # 'True'
print(str([1, 2, 3]))   # '[1, 2, 3]'

# Implicit string concatenation (whitespace between literals)
implicit = ("Hello " "World")
print(f"\nImplicit concat: {implicit!r}")   # 'Hello World'


# ─────────────────────────────────────────────
# SECTION 2 : Immutability
# ─────────────────────────────────────────────
print("\n" + "=" * 60)
print(" SECTION 2 : Immutability")
print("=" * 60)

name = "Amar"
# name[0] = "K"   ← TypeError: 'str' does not support item assignment

# Correct way → build a new string
name_modified = "K" + name[1:]
print(f"Original  : {name!r}")
print(f"Modified  : {name_modified!r}")   # 'Kmar'


# ─────────────────────────────────────────────
# SECTION 3 : Sequence Operations
# ─────────────────────────────────────────────
print("\n" + "=" * 60)
print(" SECTION 3 : Sequence Operations (indexing, slicing, etc.)")
print("=" * 60)

s = "Python"
#   P  y  t  h  o  n
#   0  1  2  3  4  5
#  -6 -5 -4 -3 -2 -1

# Indexing
print(f"\n-- Indexing --")
print(f"s        = {s!r}")
print(f"s[0]     = {s[0]!r}")       # 'P'
print(f"s[-1]    = {s[-1]!r}")      # 'n'

# No separate char type — s[0] is still str of length 1
print(f"type(s[0]) = {type(s[0])}")  # <class 'str'>

# Slicing
print(f"\n-- Slicing --")
print(f"s[0:3]   = {s[0:3]!r}")    # 'Pyt'
print(f"s[1:4]   = {s[1:4]!r}")    # 'yth'
print(f"s[::2]   = {s[::2]!r}")    # 'Pto'  (every 2nd char)
print(f"s[::-1]  = {s[::-1]!r}")   # 'nohtyP'  (reverse)

# Length
print(f"\n-- Length --")
print(f"len(s)   = {len(s)}")       # 6

# Membership
print(f"\n-- Membership (in / not in) --")
print(f"'y' in s        = {'y' in s}")       # True
print(f"'z' not in s    = {'z' not in s}")   # True

# Concatenation & Repetition
print(f"\n-- Concatenation & Repetition --")
print("Hello" + " " + "Amar")     # Hello Amar
print("PYTHON " * 3)               # PYTHON PYTHON PYTHON

# Iteration
print(f"\n-- Iteration --")
for ch in "Amar":
    print(ch, end=" ")
print()


# ─────────────────────────────────────────────
# SECTION 4 : Case Methods
# ─────────────────────────────────────────────
print("\n" + "=" * 60)
print(" SECTION 4 : Case Methods")
print("=" * 60)

s = "hello World"
print(f"Original    : {s!r}")
print(f"upper()     : {s.upper()!r}")       # 'HELLO WORLD'
print(f"lower()     : {s.lower()!r}")       # 'hello world'
print(f"title()     : {s.title()!r}")       # 'Hello World'
print(f"capitalize(): {s.capitalize()!r}")  # 'Hello world'
print(f"swapcase()  : {s.swapcase()!r}")    # 'HELLO wORLD'
print(f"casefold()  : {s.casefold()!r}")    # 'hello world' (Unicode-safe)


# ─────────────────────────────────────────────
# SECTION 5 : Search & Find Methods
# ─────────────────────────────────────────────
print("\n" + "=" * 60)
print(" SECTION 5 : Search Methods")
print("=" * 60)

s = "hello world hello"
print(f"String        : {s!r}")
print(f"find('hello') : {s.find('hello')}")      # 0   (first occurrence)
print(f"rfind('hello'): {s.rfind('hello')}")     # 12  (last occurrence)
print(f"index('world'): {s.index('world')}")     # 6   (raises ValueError if not found)
print(f"count('hello'): {s.count('hello')}")     # 2
print(f"startswith    : {s.startswith('hello')}") # True
print(f"endswith      : {s.endswith('hello')}")   # True


# ─────────────────────────────────────────────
# SECTION 6 : Replace
# ─────────────────────────────────────────────
print("\n" + "=" * 60)
print(" SECTION 6 : Replace")
print("=" * 60)

s = "I like cats and cats like me"
print(f"Original        : {s!r}")
print(f"replace all     : {s.replace('cats', 'dogs')!r}")
print(f"replace 1st only: {s.replace('cats', 'dogs', 1)!r}")


# ─────────────────────────────────────────────
# SECTION 7 : Strip / Clean
# ─────────────────────────────────────────────
print("\n" + "=" * 60)
print(" SECTION 7 : Strip / Clean")
print("=" * 60)

s = "   hello   "
print(f"strip()  : {s.strip()!r}")    # 'hello'
print(f"lstrip() : {s.lstrip()!r}")   # 'hello   '
print(f"rstrip() : {s.rstrip()!r}")   # '   hello'

s2 = "...hello..."
print(f"strip('.'): {s2.strip('.')!r}")  # 'hello'


# ─────────────────────────────────────────────
# SECTION 8 : Split & Join
# ─────────────────────────────────────────────
print("\n" + "=" * 60)
print(" SECTION 8 : Split & Join")
print("=" * 60)

s = "a,b,c,d"
parts = s.split(",")
print(f"split(',')  : {parts}")           # ['a', 'b', 'c', 'd']

joined = "-".join(parts)
print(f"join('-')   : {joined!r}")        # 'a-b-c-d'

line = "hello world python"
print(f"split()     : {line.split()}")    # ['hello', 'world', 'python']

multi = "line1\nline2\nline3"
print(f"splitlines(): {multi.splitlines()}")  # ['line1', 'line2', 'line3']


# ─────────────────────────────────────────────
# SECTION 9 : Alignment & Padding
# ─────────────────────────────────────────────
print("\n" + "=" * 60)
print(" SECTION 9 : Alignment & Padding")
print("=" * 60)

print(f"ljust(10) : {'hi'.ljust(10)!r}")     # 'hi        '
print(f"rjust(10) : {'hi'.rjust(10)!r}")     # '        hi'
print(f"center(10): {'hi'.center(10)!r}")    # '    hi    '
print(f"zfill(6)  : {'42'.zfill(6)!r}")      # '000042'


# ─────────────────────────────────────────────
# SECTION 10 : Type-Checking Methods
# ─────────────────────────────────────────────
print("\n" + "=" * 60)
print(" SECTION 10 : Type-Checking (is* methods)")
print("=" * 60)

print(f"'hello'.isalpha()       = {'hello'.isalpha()}")       # True
print(f"'123'.isdigit()         = {'123'.isdigit()}")         # True
print(f"'abc123'.isalnum()      = {'abc123'.isalnum()}")      # True
print(f"'hello'.islower()       = {'hello'.islower()}")       # True
print(f"'HELLO'.isupper()       = {'HELLO'.isupper()}")       # True
print(f"'   '.isspace()         = {'   '.isspace()}")         # True
print(f"'Hello World'.istitle() = {'Hello World'.istitle()}") # True
print(f"'123'.isdecimal()       = {'123'.isdecimal()}")       # True
print(f"'hello'.isidentifier()  = {'hello'.isidentifier()}")  # True
print(f"'hello'.isascii()       = {'hello'.isascii()}")       # True


# ─────────────────────────────────────────────
# SECTION 11 : Escape Sequences
# ─────────────────────────────────────────────
print("\n" + "=" * 60)
print(" SECTION 11 : Escape Sequences")
print("=" * 60)

print("Newline    : Hello\nWorld")
print("Tab        : Hello\tWorld")
print("Backslash  : C:\\Users\\Amar")
print("Quote      : It\'s raining")
print("Unicode    : \u0041 \u0048 \u0049")   # A H I

# Raw string — r prefix disables escape processing
path = r"C:\Users\amar\new_folder"
print(f"\nRaw string : {path!r}")   # backslash is literal


# ─────────────────────────────────────────────
# SECTION 12 : Unicode
# ─────────────────────────────────────────────
print("\n" + "=" * 60)
print(" SECTION 12 : Unicode")
print("=" * 60)

print(f"ord('A')   = {ord('A')}")       # 65
print(f"ord('ह')   = {ord('ह')}")      # 2361  (Hindi character)
print(f"chr(65)    = {chr(65)!r}")      # 'A'
print(f"chr(128512)= {chr(128512)}")    # 😀

s = "hello 😀 ह"
print(f"\nString   : {s}")
print(f"len()    : {len(s)}")           # 9  — each code point = 1

# Encoding / Decoding
print("\n-- Encoding & Decoding --")
s = "hello"
b = s.encode("utf-8")       # str → bytes
print(f"encode('utf-8')  : {b}")        # b'hello'
s2 = b.decode("utf-8")      # bytes → str
print(f"decode('utf-8')  : {s2!r}")     # 'hello'
print(f"type(b)          : {type(b)}")  # <class 'bytes'>
print(f"type(s2)         : {type(s2)}") # <class 'str'>


# ─────────────────────────────────────────────
# SECTION 13 : String Formatting — 3 Styles
# ─────────────────────────────────────────────
print("\n" + "=" * 60)
print(" SECTION 13 : String Formatting — 3 Styles")
print("=" * 60)

name = "Amar"
age  = 20
pi   = 3.14159

# Style 1 — f-strings (Python 3.6+, recommended)
print("\n[ Style 1 ] f-strings :")
print(f"Name  : {name}, Age : {age}")
print(f"2 + 2 = {2 + 2}")
print(f"Pi    = {pi:.2f}")          # 2 decimal places
print(f"Hex   = {255:#010x}")       # '0x000000ff'
print(f"Debug : {name = }")         # name = 'Amar'  (Python 3.8+)

# Style 2 — .format() method
print("\n[ Style 2 ] .format() :")
print("Hello, {}!".format(name))
print("{0} + {1} = {2}".format(2, 3, 5))
print("{name} is {age} years old.".format(name=name, age=age))

# Style 3 — % formatting (old C-style)
print("\n[ Style 3 ] % formatting (C-style) :")
print("Hello, %s!" % name)
print("Value: %d, Float: %.2f" % (42, pi))


# ─────────────────────────────────────────────
# SECTION 14 : Memory & String Interning
# ─────────────────────────────────────────────
print("\n" + "=" * 60)
print(" SECTION 14 : Memory & String Interning")
print("=" * 60)

import sys

a = "hello"
b = "hello"
print(f"a = {a!r}, id(a) = {id(a)}")
print(f"b = {b!r}, id(b) = {id(b)}")
print(f"a is b  → {a is b}")           # True  (interned — same object)
print(f"a == b  → {a == b}")           # True

print(f"\nsys.getsizeof('')      = {sys.getsizeof('')}")       # 49 bytes
print(f"sys.getsizeof('hello') = {sys.getsizeof('hello')}")   # 54 bytes


# ─────────────────────────────────────────────
# SECTION 15 : str vs bytes — Key Difference
# ─────────────────────────────────────────────
print("\n" + "=" * 60)
print(" SECTION 15 : str vs bytes")
print("=" * 60)

s = "hello"
b = b"hello"

print(f"str   : {s!r}  → type = {type(s)}")
print(f"bytes : {b!r}  → type = {type(b)}")
print(f"s[0]  = {s[0]!r}  (str of len 1)")
print(f"b[0]  = {b[0]}   (int — ASCII code)")
print(f"s == b → {s == b}")    # False — never equal
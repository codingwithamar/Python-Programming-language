# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 08_none_data_type.py
# Path    : 02_Data_Types\08_none_data_type.py
# Subject : Enter Subject
# Description : Description
# =============================================================================

def heading(text):
    print("=" * 60)
    print(text)
    print("=" * 60)

def main():
    # ------------------------------------------------------------
    # 1. None as a default sentinel value (real-world usage)
    # ------------------------------------------------------------
    heading("1. None as default sentinel value")

    def greet(name=None):
        if name is None:
            name = "Guest"
        return f"Hello, {name}!"

    print(greet())
    print(greet("Amar"))

    # ------------------------------------------------------------
    # 2. 'is None' vs '== None' - always use 'is'
    # ------------------------------------------------------------
    heading("2. 'is None' vs '== None'")
    x = None
    print(f"x is None  -> {x is None!r}")
    print(f"x == None  -> {x == None!r}")
    print(f"type(None) -> {type(None)!r}")

    # ------------------------------------------------------------
    # 3. NoneType is a singleton - only ONE instance ever exists
    # ------------------------------------------------------------
    heading("3. NoneType singleton behaviour")
    a = None
    b = None
    print(f"a is b       -> {a is b!r}")
    print(f"id(a) == id(b) -> {id(a) == id(b)!r}")

    # ------------------------------------------------------------
    # 4. None is falsy (truthiness)
    # ------------------------------------------------------------
    heading("4. None is falsy")
    print(f"bool(None) = {bool(None)!r}")
    if not None:
        print("None evaluates as falsy in conditions")

    # ------------------------------------------------------------
    # 5. None as a 'not found' / missing return value (best trick example)
    # ------------------------------------------------------------
    heading("5. None as 'missing value' marker (best example)")

    def find_item(items, target):
        for item in items:
            if item == target:
                return item
        return None

    result = find_item([1, 2, 3], 5)
    print(f"result = {result!r}, result is None -> {result is None!r}")

if __name__ == "__main__":
    main()
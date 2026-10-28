# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 2_eval_BuiltIn_Function.py
# Path    : Python-Programming-Language/07_Functions_in_Python/02_Function_Categories/01_Built_in_functions/06_Advanced_Dynamic_builtIn_functions/2_eval_BuiltIn_Function.py
# Subject : Advanced Built-in functions in python
# Description : eval()- takes a string that contains a Python expression, runs it, and returns the result.
# =============================================================================

def main():
#%% Concept Explanation
    x = input("Enter something : ")
    print(x * 2)
    """
    Enter something : 5         #55
    Enter something : "AMAR"    #"AMAR""AMAR"
    Enter something : 2.5       #2.52.5
    Enter something : arm9      #arm9arm9
    Enter something : $         #$$
    """

    y = int(input("Enter something : "))
    print(y * 2)
    """
        Enter something : 5         #10
        Enter something : "AMAR"    #AMARAMAR
        Enter something : 2.5       #ERROR
        Enter something : arm9      #ERROR
        Enter something : $         #ERROR
    """

# Now we use eval()
    z = eval(input("Enter something : "))
    print(z * 2)
    """
        Enter something : 5         #10
        Enter something : "AMAR"    #"AMAR"AMAR"
        Enter something : 2.5       #5.0
        Enter something : arm9      #ERROR
        Enter something : $         #ERROR
        """

#%% Advanced thinking

    # Arithmetic
    print(eval("2 + 3"))                 # 5
    print(eval("10 / 4"))                # 2.5

    # Using built-in functions inside the string
    print(eval("len('hello')"))          # 5
    print(eval("max(4, 9, 2)"))          # 9

    # Comparison gives a boolean
    print(eval("3 > 2"))                 # True

    # Strings that look like Python data become real data
    print(eval("[1, 2, 3]"))             # [1, 2, 3]
    print(type(eval("[1, 2, 3]")))       # <class 'list'>
    print(eval("{'a': 1}"))              # {'a': 1}

    # Using a variable from the current code
    x = 10
    print(eval("x * 2"))                 # 20

    # Giving your own variables through a dictionary
    print(eval("a + b", {"a": 5, "b": 7}))   # 12

#%% Advanced Example
    import ast

    # 1. A tiny calculator that limits what the expression can use
    def calculate(expression):
        allowed = {"abs": abs, "round": round, "min": min, "max": max}
        return eval(expression, {"__builtins__": {}}, allowed)

    print(calculate("max(3, 8) + abs(-2)"))     # 10
    # calculate("len('abc')")                   # NameError, because len is not allowed

    # 2. The SAFE way to turn text into Python data
    text = "{'name': 'Amar', 'scores': [85, 90]}"
    data = ast.literal_eval(text)
    print(data["scores"])                       # [85, 90]

    # literal_eval accepts only literals (numbers, strings, lists, dicts, tuples,
    # sets, booleans, None), so this fails instead of running anything:
    try:
        ast.literal_eval("__import__('os')")
    except ValueError:
        print("Blocked: not a plain literal")

    # 3. compile() once, eval() many times (faster in loops)
    code = compile("price * qty", "<string>", "eval")
    for price, qty in [(10, 2), (5, 4), (8, 3)]:
        print(eval(code, {"price": price, "qty": qty}))   # 20, 20, 24

if __name__ == "__main__":
    main()
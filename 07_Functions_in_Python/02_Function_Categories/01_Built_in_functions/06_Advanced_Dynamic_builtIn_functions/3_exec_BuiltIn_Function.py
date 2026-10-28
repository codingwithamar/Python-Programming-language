# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 3_exec_BuiltIn_Function.py
# Path    : Python-Programming-Language/07_Functions_in_Python/02_Function_Categories/01_Built_in_functions/06_Advanced_Dynamic_builtIn_functions/3_exec_BuiltIn_Function.py
# Subject : Advanced Built-in functions in python
# Description : exec() - executes Python statements from a string or code object.
# =============================================================================

def main():
#%% Basic Concept
    code1 = "print('Jai Ganesh...')"
    exec(code1)         #Jai Ganesh...

#    exec("x = 100")
#    print(x)           #ERROR

    code2 = exec("x = 100")
    print(code2)        #none

    code3 = """
x = 10
y = 20
total = x + y
print(total)
"""
    exec(code3)

    code = """
for number in range(1, 4):
    print(number)
"""
    exec(code)

#%% Advanced thinking

    # 1. Run a statement (an assignment)
#    exec("x = 5")
#    print(x)                      # Error

    ns = {}
    exec("x = 5", ns)
    print(ns["x"])                 # 5

    # 2. Run a print call
    exec("print('Hello')")        # Hello

    # 3. Run multiple lines, including a loop
    code = """
total = 0
for i in range(1, 4):
    total += i
print(total)
    """
    exec(code)                    # 6

    # 4. exec always returns None
    result = exec("2 + 3")
    print(result)                 # None

    # 5. Keep results in your own dictionary instead of the current scope
    ns = {}
    exec("a = 10\nb = 20\nc = a + b", ns)
    print(ns["c"])                # 30

#%% Advanced examples
    # 1. Define and use a function from a string
    namespace = {}
    source = """
def greet(name):
    return "Hello, " + name
message = greet("Amar")
    """
    exec(source, namespace)
    print(namespace["message"])              # Hello, Amar
    print(namespace["greet"]("Riya"))        # Hello, Riya

    # 2. Generate several functions from a table of settings
    operations = {"add": "+", "subtract": "-", "multiply": "*"}
    namespace = {}

    for name, symbol in operations.items():
        exec(f"def {name}(a, b):\n    return a {symbol} b", namespace)

    print(namespace["add"](6, 3))            # 9
    print(namespace["subtract"](6, 3))       # 3
    print(namespace["multiply"](6, 3))       # 18

    # 3. Use compile() once, exec() many times (faster in loops)
    code = compile("counter += step", "<string>", "exec")
    state = {"counter": 0, "step": 5}
    for _ in range(3):
        exec(code, state)
    print(state["counter"])                  # 15

    # 4. Run another script file's code in an isolated namespace
    with open("2_eval_BuiltIn_Function.py") as f:
        script_text = f.read()

    env = {"__name__": "__main__"}
    exec(compile(script_text, "2_eval_BuiltIn_Function.py", "exec"), env)
    # Variables defined in that file are now available in env

if __name__ == "__main__":
    main()
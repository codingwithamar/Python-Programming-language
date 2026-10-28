# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 1_compile_BuiltIn_Function.py
# Path    : Python-Programming-Language/07_Functions_in_Python/02_Function_Categories/01_Built_in_functions/06_Runtime_builtIn_functions/1_compile_BuiltIn_Function.py
# Subject : Advanced Built-in functions in python
# Description : compile() - turns source code (text) into a code object.
# =============================================================================

def main():
    # Mode "eval": one expression, gives back a value
    code1 = compile("2 + 3", "<string>", "eval")
    print(type(code1))        # <class 'code'>
    print(eval(code1))        # 5

    # Mode "exec": statements
    code2 = compile("x = 10\nprint(x * 2)", "<string>", "exec")
    exec(code2)               # 20

    # Mode "single": one statement, prints expression values like the shell
    code3 = compile("5 + 5", "<string>", "single")
    exec(code3)               # 10

#What to notice
# compile() itself prints nothing and runs nothing.
# The result is an object of type code.
# Running happens only when you pass it to eval() or exec().

#%% Advanced examples

    import ast

    # 1. Compile once, run many times
    rule = compile("price * qty > 1000", "<rule>", "eval")

    orders = [
        {"price": 500, "qty": 3},
        {"price": 100, "qty": 5},
        {"price": 900, "qty": 2},
    ]
    for order in orders:
        print(eval(rule, {}, order))      # True, False, True

    # 2. Check syntax WITHOUT running the code
    def is_valid_python(text):
        try:
            compile(text, "<check>", "exec")
            return True
        except SyntaxError as error:
            print("Syntax problem on line", error.lineno)
            return False

    print(is_valid_python("x = 5"))        # True
    print(is_valid_python("if x ="))       # Syntax problem on line 1, then False

    # 3. Look inside a code object
    code = compile("a + b", "<my_rule>", "eval")
    print(code.co_names)          # ('a', 'b') -> names the code uses
    print(code.co_filename)       # <my_rule>

    folded = compile("2 + 3", "<s>", "eval")
    print(folded.co_consts)       # (5,) -> Python calculated 2 + 3 while compiling

    # 4. Get a syntax tree instead of a code object
    tree = compile("a + b", "<s>", "eval", flags=ast.PyCF_ONLY_AST)
    print(type(tree))             # <class 'ast.Expression'>

    # 5. The optimize option removes assert statements
    source = "assert 1 == 2, 'math broke'"

    try:
        exec(compile(source, "<s>", "exec", optimize=0))
    except AssertionError as error:
        print("optimize=0 ->", error)         # optimize=0 -> math broke

    exec(compile(source, "<s>", "exec", optimize=1))
    print("optimize=1 -> assert was removed, nothing happened")

    # 6. Load and run a plugin file (real automation pattern)
    # with open("plugin.py") as f:
    #     code = compile(f.read(), "plugin.py", "exec")
    # env = {}
    # exec(code, env)
    # env["run"]()
    # The real file name makes error messages point to the right file.

if __name__ == "__main__":
    main()


# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 8_Global_and_Local_BuiltIn_Function.py
# Path    : Python-Programming-Language/07_Functions_in_Python/02_Function_Categories/01_Built_in_functions/05_Object_Control_builtIn_functions/1_Function_Related_Utilities/8_Global_and_Local_BuiltIn_Function.py
# Subject : Built-in functions in python
# Description : Description
# =============================================================================

x = 10

def main():


    def show():
        y = 5
        print("Locals:", locals())         #Locals: {'y': 5}
        print("Global x:", globals()["x"])  #Global x: 10

    show()
    print(globals() is locals())    # True
    # The last line prints True because at module level both functions give the same namespace.

#%%
    # 1. Create global variables dynamically
    def make_vars():
        for i in range(3):
            globals()[f"var_{i}"] = i * 10

    make_vars()
    print(var_0, var_1, var_2)      #0 10 20

    # 2. Use locals() to fill a template
    def greet():
        name = "Amar"
        course = "Python"
        return "Hello {name}, welcome to {course}".format(**locals())  #Hello Amar, welcome to Python

    print(greet())

    # 3. Changing locals() does NOT change a function variable
    def test():
        a = 1
        locals()["a"] = 99
        print("a is still:", a)     #a is still: 1

    test()


if __name__ == "__main__":
    main()
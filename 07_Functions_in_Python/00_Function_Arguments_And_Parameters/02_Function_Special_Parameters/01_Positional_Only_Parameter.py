# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 01_Positional_Only_Parameter.py
# Path    : Python-Programming-Language/07_Functions_in_Python/00_Function_Arguments_And_Parameters/02_Function_Parameters/01_Positional_Only_Parameter.py
# Subject : Function Special Parameters
# Description : 1) Positional-only Parameters (before /)
# =============================================================================

def main():
#%% Basic Concepts
    def add(a, b, /):
        return a + b

    print(add(10, 20))       # Valid
    print(add(a=10, b=20))   # TypeError
#________________________________________________________________________________________________________
    # Built-in functions that work this way
    print(len("hello"))     # 5
    # len(obj="hello")      # TypeError
    print(abs(-7))          # 7
    # abs(x=-7)             # TypeError
#________________________________________________________________________________________________________

#%% Basic Examples
    def square(x, /):
        return x * x

    print(square(5))        # 25

    try:
        print(square(x=5))  # name not allowed
    except TypeError as e:
        print(e)            # square() got some positional-only arguments passed as keyword arguments: 'x'

#%% Advanced Examples
    # Name clash fix: "data" is positional-only, so "data" can also be used as a keyword in **extra
    def log(data, /, **extra):
        print("Message:", data)
        print("Extra:", extra)

    log("Server started", data="ignored here", level="INFO")
    # Message: Server started
    # Extra: {'data': 'ignored here', 'level': 'INFO'}

#________________________________________________________________________________________________________
    # The parameter name can be renamed later without breaking any caller
    def distance(x1, y1, x2, y2, /):
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

    print(distance(0, 0, 3, 4))   # 5.0
    # Callers never use the names, so you can rename x1 to start_x safely.
#________________________________________________________________________________________________________

if __name__ == "__main__":
    main()
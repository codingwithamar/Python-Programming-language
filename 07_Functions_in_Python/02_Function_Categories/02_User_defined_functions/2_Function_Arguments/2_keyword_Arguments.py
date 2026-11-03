# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : keyword_Arguments.py
# Path    : Python-Programming-Language/07_Functions_in_Python/00_Function_Arguments/keyword_Arguments.py
# Subject : Function arguments in python
# Description : Keyword Arguments
# =============================================================================

def main():
#%% Basic Concept
    def introduce(name, age):
        print(f"{name} is {age} years old")

    introduce(name="Amar", age=25)
    introduce(age=25, name="Amar")       # same result, different order
    introduce("Amar", age=25)            # mix: positional first, then keyword

#%% Advanced Examples
    def create_server(host, port, use_ssl, timeout, retries):
        return (host, port, use_ssl, timeout, retries)

    # Hard to read:
    create_server("localhost", 8080, True, 30, 3)

    # Easy to read:
    create_server(host="localhost", port=8080, use_ssl=True, timeout=30, retries=3)

    # Errors
    try:
        introduce(name="Amar", name="Ravi")     # same keyword twice
    except SyntaxError:
        pass                                     # this is a SyntaxError when the file is compiled

    try:
        introduce("Amar", name="Ravi")           # "Amar" already filled name
    except TypeError as error:
        print(error)       # introduce() got multiple values for argument 'name'

    try:
        introduce("Amar", height=170)            # no parameter called height
    except TypeError as error:
        print(error)       # introduce() got an unexpected keyword argument 'height'

if __name__ == "__main__":
    main()
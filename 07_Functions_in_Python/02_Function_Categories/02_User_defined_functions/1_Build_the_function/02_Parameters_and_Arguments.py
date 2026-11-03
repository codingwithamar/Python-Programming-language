# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 02_Parameters_and_Arguments.py
# Path    : Python-Programming-Language/07_Functions_in_Python/Group1_Build_the_function/02_Parameters_and_Arguments.py
# Subject : User Define Function
# Description : Parameters and Arguments
# =============================================================================

def main():
#%% Basic Concepts
    def add(a, b):        # a and b are PARAMETERS
        return a + b

    add(5, 3)             # 5 and 3 are ARGUMENTS

    def create_user(name, age, country="India"):
        print(f"Name: {name}, Age: {age}, Country: {country}")

    create_user("Amar", 25)                   # positional, default country
    create_user("Sara", 30, "USA")            # positional, all three
    create_user(age=22, name="Priya")         # keyword, any order
    create_user("Ravi", age=28, country="UK") # mix: positional first, then keyword

#%% Advanced Examples
    def connect(host, port=8080, secure=False):
        return f"{host}:{port} secure={secure}"

    # Unpack a list into positional arguments
    args = ["localhost", 9000]
    print(connect(*args))                      # localhost:9000 secure=False

    # Unpack a dictionary into keyword arguments
    settings = {"host": "example.com", "secure": True}
    print(connect(**settings))                 # example.com:8080 secure=True

    # Wrong calls and their errors
    try:
        connect()                              # missing host
    except TypeError as error:
        print(error)    # connect() missing 1 required positional argument: 'host'

    try:
        connect("a", host="b")                 # same parameter given twice
    except TypeError as error:
        print(error)    # connect() got multiple values for argument 'host'

    try:
        connect("a", color="red")              # unknown keyword
    except TypeError as error:
        print(error)    # connect() got an unexpected keyword argument 'color'

if __name__ == "__main__":
    main()
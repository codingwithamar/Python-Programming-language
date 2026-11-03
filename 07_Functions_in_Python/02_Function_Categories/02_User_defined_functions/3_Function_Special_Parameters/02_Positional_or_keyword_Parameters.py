# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 03_Positional_or_keyword_Parameters.py
# Path    : Python-Programming-Language/07_Functions_in_Python/00_Function_Arguments_And_Parameters/02_Function_Parameters/03_Positional_or_keyword_Parameters.py
# Subject : Function Special Parameters
# Description : 3) Positional-or-keyword Parameters
# =============================================================================

def main():
#%% Basic Concept
    def student(name, age):
        print(name, age)

    student("Amar", 22)
    student(name="Amar", age=22)


    def example(a, /, b, *, c):
        print(a, b, c)

    example(10, 20, c=30)

#%% Basic Examples
    def introduce(name, city):
        print(name, "lives in", city)

    introduce("Amar", "Pune")                # by position
    introduce(name="Amar", city="Pune")      # by name
    introduce("Amar", city="Pune")           # mixed
    introduce(city="Pune", name="Amar")      # any order when using names
    # All four print: Amar lives in Pune

#%% Advanced Examples
    # Real-life function: the caller picks the style that reads best
    def create_file(name, extension="txt", folder="."):
        return f"{folder}/{name}.{extension}"

    print(create_file("notes"))                          # ./notes.txt
    print(create_file("notes", "md"))                    # ./notes.md
    print(create_file("notes", folder="docs"))           # docs/notes.txt
    print(create_file(folder="docs", name="a", extension="py"))   # docs/a.py

    # Mixing rule: positional arguments first, keyword arguments after
    def info(a, b, c):
        print(a, b, c)

    info(1, 2, c=3)        # valid
    # info(1, b=2, 3)      # SyntaxError: positional argument follows keyword argument

if __name__ == "__main__":
    main()
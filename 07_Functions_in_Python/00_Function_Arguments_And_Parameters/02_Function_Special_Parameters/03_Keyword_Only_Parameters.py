# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 02_Keyword_Only_Parameters.py
# Path    : Python-Programming-Language/07_Functions_in_Python/00_Function_Arguments_And_Parameters/02_Function_Parameters/02_Keyword_Only_Parameters.py
# Subject : EFunction Special Parameters
# Description : 2) Keyword-only Parameters (*)
# =============================================================================

def main():
#%% Basic Concept
    def student(name, *, age):
        print(name, age)

    student("Amar", age=22)  # Valid
    student("Amar", 22)      # TypeError

#%% Basic Examples
    def greet(name, *, greeting="Hello"):
        print(greeting, name)

    greet("Amar")                         # Hello Amar
    greet("Amar", greeting="Namaste")     # Namaste Amar

    try:
        greet("Amar", "Namaste")          # greeting by position, not allowed
    except TypeError as e:
        print(e)                          # greet() takes 1 positional argument but 2 were given

    # Built-in functions that work this way
    print("a", "b", sep="-")              # a-b   (sep is keyword-only)
    print(sorted([3, 1, 2], reverse=True))   # [3, 2, 1]  (reverse is keyword-only)

#%% Advanced Examples
    # Several flags: names make the call readable and prevent mix-ups
    def export_data(rows, *, header=True, delimiter=",", encoding="utf-8"):
        lines = []
        if header:
            lines.append("id,name")
        for row in rows:
            lines.append(delimiter.join(map(str, row)))
        return "\n".join(lines)

    data = [(1, "Amar"), (2, "Riya")]
    print(export_data(data))
    print(export_data(data, header=False, delimiter=";"))
    # export_data(data, False, ";")       # TypeError: flags must be named

if __name__ == "__main__":
    main()
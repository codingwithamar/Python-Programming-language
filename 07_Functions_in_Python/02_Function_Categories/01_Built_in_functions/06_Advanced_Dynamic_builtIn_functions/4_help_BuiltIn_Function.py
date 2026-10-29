# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 4_help_BuiltIn_Function.py
# Path    : Python-Programming-Language/07_Functions_in_Python/02_Function_Categories/01_Built_in_functions/06_Advanced_Dynamic_builtIn_functions/4_help_BuiltIn_Function.py
# Subject : Advanced Built-in functions in python
# Description : help()- shows the documentation of an object
# =============================================================================

def main():
    help(len)
    """OUTPUT :
    Help on built-in function len in module builtins:
    len(obj, /)
    Return the number of items in a container.
    """
    help(str.upper)      # help for a method
    help(list)           # full help for the list class
    help("keywords")     # all reserved words
    help("if")           # help for a keyword (use quotes)

    import math
    help(math)           # help for a whole module
    help(math.sqrt)      # help for one function in it

#%% Advanced Example

    import inspect
    import pydoc
    import contextlib
    import io

    # 1. help() shows YOUR docstrings
    def calculate_area(length, width):
        """Return the area of a rectangle.

        length: size of one side
        width: size of the other side
        """
        return length * width

    help(calculate_area)

    # 2. Classes: shows the class docstring and the docstring of every method
    class Account:
        """A simple bank account."""

        def deposit(self, amount):
            """Add money to the account."""

    help(Account)

    # 3. help() prints. To get the text inside your program, use these:
    print(calculate_area.__doc__)                 # raw docstring, with original spaces
    print(inspect.getdoc(calculate_area))         # cleaned docstring (indent removed)
    print(inspect.signature(calculate_area))      # (length, width)

    page = pydoc.render_doc(calculate_area, renderer=pydoc.plaintext)
    print(page)                                   # the full help page as a string

    # 4. Capture what help() prints
    buffer = io.StringIO()
    with contextlib.redirect_stdout(buffer):
        help(calculate_area)
    print(len(buffer.getvalue()) > 0)             # True

    # 5. help() on a value shows help for its class
    help(5)                                       # same as help(int)

    # 6. A string is treated as a NAME to look up, not as a value
    help("hello")      # No Python documentation found for 'hello'
    help(str)          # this is what you wanted for strings

    # 7. Interactive session
    # help()           -> shows the "help>" prompt
    #                     type: modules, keywords, topics, symbols, or any name
    #                     type: quit   to leave

if __name__ == "__main__":
    main()


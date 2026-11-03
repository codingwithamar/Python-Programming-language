# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 05_Docstring_and_TypeHint.py
# Path    : Python-Programming-Language/07_Functions_in_Python/Group1_Build_the_function/05_Docstring_and_TypeHint.py
# Subject : User Defined Functions
# Description : DOCSTRINGS
# =============================================================================

def main():
#%% Basic Concept
    def add(a: int, b: int) -> int:        # type hints: a and b are int, the result is int
        """Return the sum of a and b."""   # docstring: describes the function
        return a + b

#%% Basic Example
    def add(a, b):
        """Return the sum of a and b."""
        return a + b

    print(add.__doc__)       # Return the sum of a and b.
    help(add)

#%% Advanced Examples
    import inspect

    # 1. A multi-line docstring (Google style)
    def calculate_area(length, width):
        """Return the area of a rectangle.

        Args:
            length: size of one side, in meters.
            width: size of the other side, in meters.

        Returns:
            The area as a number.

        Raises:
            ValueError: if a side is negative.

        Example:
            >>> calculate_area(4, 5)
            20
        """
        if length < 0 or width < 0:
            raise ValueError("Sides must not be negative")
        return length * width

    # 2. Read the docstring in different ways
    print(calculate_area.__doc__)                  # raw text, with the original indentation
    print(inspect.getdoc(calculate_area))          # cleaned text (indentation removed)
    help(calculate_area)                           # formatted manual page

    # 3. The first statement only: a docstring written later is just a string
    def wrong():
        x = 1
        """This is NOT a docstring."""
        return x

    print(wrong.__doc__)                           # None

    # 4. A comment is not a docstring
    def commented():
        # This comment does not appear in help()
        return 1

    print(commented.__doc__)                       # None

    # 5. Docstrings can be tested with doctest
    import doctest

    def double(n):
        """Return n doubled.

        >>> double(4)
        8
        >>> double(0)
        0
        """
        return n * 2

    print(doctest.testmod())                       # TestResults(failed=0, attempted=2)

if __name__ == "__main__":
    main()

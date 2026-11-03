# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 03_return_Statement.py
# Path    : Python-Programming-Language/07_Functions_in_Python/Group1_Build_the_function/03_return_Statement.py
# Subject : User Defined Function
# Description : return Statement
# =============================================================================

def main():
    #%% Basic Concepts
    # Single value
    def square(x):
        return x * x

    result = square(5)
    print(result)                  # 25

    # No return gives None
    def say_hello():
        print("Hello")

    value = say_hello()            # prints Hello
    print(value)                   # None

    # Multiple values (really one tuple)
    def get_min_max(numbers):
        return min(numbers), max(numbers)

    result = get_min_max([4, 8, 1, 9, 3])
    print(result)                  # (1, 9)
    lowest, highest = result       # unpack
    print(lowest, highest)         # 1 9

#%% Advanced Examples
    # 1. Early return (guard clauses): flat and clear code
    def classify_age(age):
        if age < 0:
            return "Invalid age"
        if age < 18:
            return "Minor"
        return "Adult"

    print(classify_age(-5))        # Invalid age
    print(classify_age(25))        # Adult

    # 2. return inside a loop leaves the whole function
    def find_first_even(numbers):
        for n in numbers:
            if n % 2 == 0:
                return n           # leaves the function at once
        return None                # no even number found

    print(find_first_even([1, 3, 6, 8]))    # 6
    print(find_first_even([1, 3]))          # None

    # 3. Return a dictionary for several named results
    def analyze(numbers):
        return {
            "count": len(numbers),
            "total": sum(numbers),
            "average": sum(numbers) / len(numbers),
        }

    stats = analyze([10, 20, 30])
    print(stats["average"])        # 20.0

    # 4. Return a named tuple: tuple behavior plus readable names
    from collections import namedtuple

    Result = namedtuple("Result", ["lowest", "highest"])

    def min_max(numbers):
        return Result(min(numbers), max(numbers))

    r = min_max([4, 8, 1, 9])
    print(r.lowest, r.highest)     # 1 9
    print(r)                       # Result(lowest=1, highest=9)

    # 5. Return a function (closure)
    def make_multiplier(factor):
        def multiplier(x):
            return x * factor
        return multiplier

    double = make_multiplier(2)
    print(double(10))              # 20

    # 6. Return a boolean
    def is_even(n):
        return n % 2 == 0

    print(is_even(4), is_even(7))  # True False

    # 7. The classic bug: print is not return
    def add_wrong(a, b):
        print(a + b)               # shows the value, but returns None

    total = add_wrong(2, 3)        # prints 5
    print(total)                   # None
    # add_wrong(2, 3) + 10         # TypeError: unsupported operand type(s): 'NoneType' and 'int'

    # 8. One branch forgets to return
    def sign(n):
        if n > 0:
            return "positive"
        elif n < 0:
            return "negative"
        # n == 0 reaches the end, so None is returned

    print(sign(0))                 # None

    # 9. return with try/finally: finally still runs
    def read_value():
        try:
            return "from try"
        finally:
            print("cleanup runs before the function really returns")

    print(read_value())
    # cleanup runs before the function really returns
    # from try

    # 10. A generator uses yield, not return, to give many values (preview)
    def countdown(n):
        while n > 0:
            yield n
            n -= 1

    print(list(countdown(3)))      # [3, 2, 1]


if __name__ == "__main__":
    main()
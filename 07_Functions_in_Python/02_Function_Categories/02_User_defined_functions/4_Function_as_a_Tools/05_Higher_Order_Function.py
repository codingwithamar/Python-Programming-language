# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 05_Higher_Order_Function.py
# Path    : Python-Programming-Language/07_Functions_in_Python/02_Function_Categories/02_User_defined_functions/4_Function_as_a_Tools/05_Higher_Order_Function.py
# Subject : User Defined FUnction
# Description : Higher order Function
# =============================================================================

def main():
#%% Basic Examples
    from functools import reduce

    # 1. A function that TAKES a function
    def apply(func, value):
        return func(value)

    print(apply(len, "hello"))          # 5
    print(apply(str.upper, "hi"))       # HI

    # 2. A function that RETURNS a function
    def make_adder(n):
        def adder(x):
            return x + n
        return adder

    add5 = make_adder(5)
    print(add5(10))                     # 15

    # 3. The classic built-in trio and sorting
    nums = [1, 2, 3, 4, 5, 6]
    print(list(map(lambda x: x * x, nums)))             # [1, 4, 9, 16, 25, 36]
    print(list(filter(lambda x: x % 2 == 0, nums)))     # [2, 4, 6]
    print(reduce(lambda a, b: a + b, nums))             # 21
    print(sorted(["pear", "fig", "banana"], key=len))   # ['fig', 'pear', 'banana']

#%% Advanced Examples
#    1) map(function, *iterables)
#       Applies a function to every item. Returns a lazy iterator.

        # Basic use
    print(list(map(int, ["1", "2", "3"])))                       # [1, 2, 3]
    print(list(map(str.strip, ["  a ", " b"])))                  # ['a', 'b']

    # Several iterables: the function gets one item from each
    print(list(map(lambda a, b: a + b, [1, 2, 3], [10, 20, 30])))   # [11, 22, 33]
    print(list(map(pow, [2, 3, 4], [2, 2, 2])))                     # [4, 9, 16]

    # Stops at the shortest iterable
    print(list(map(lambda a, b: a + b, [1, 2, 3], [10, 20])))       # [11, 22]

    # Lazy and single use
    m = map(str.upper, ["a", "b"])
    print(m)                      # <map object at 0x...>  -> not the values
    print(list(m))                # ['A', 'B']
    print(list(m))                # []   -> already used up

    # Nothing runs until you consume it
    map(print, [1, 2])            # prints nothing
    list(map(print, [1, 2]))      # prints 1 and 2 (but a loop is clearer for side effects)

#    2) filter(function, iterable)
#       Keeps the items for which the function returns a true value.

    nums = [1, 2, 3, 4, 5, 6]
    print(list(filter(lambda x: x % 2 == 0, nums)))              # [2, 4, 6]
    print(list(filter(str.isdigit, ["12", "ab", "7"])))          # ['12', '7']

    # filter(None, ...) keeps only truthy items
    print(list(filter(None, [0, 1, "", "text", None, [], [0], False])))   # [1, 'text', [0]]

    # A function factory that makes a predicate
    def make_range_checker(low, high):
        def check(value):
            return low <= value <= high
        return check

    is_valid_age = make_range_checker(0, 120)
    print(list(filter(is_valid_age, [5, 150, 40, -1])))          # [5, 40]

    # The opposite: itertools.filterfalse
    from itertools import filterfalse
    print(list(filterfalse(lambda x: x % 2 == 0, nums)))         # [1, 3, 5]

#   3) sorted, min, max with key=
#       The key function runs once per item. Python sorts by the key values.

    words = ["pear", "fig", "banana", "kiwi"]
    print(sorted(words, key=len))                    # ['fig', 'pear', 'kiwi', 'banana']
    print(sorted(words, key=len, reverse=True))      # ['banana', 'pear', 'kiwi', 'fig']
    print(max(words, key=len), min(words, key=len))  # banana fig
    print(sorted(["bob", "Alice", "carl"], key=str.lower))   # ['Alice', 'bob', 'carl']

    # Sort by two rules: department A to Z, then salary high to low
    employees = [
        {"name": "Amar", "dept": "IT", "salary": 50},
        {"name": "Sara", "dept": "HR", "salary": 40},
        {"name": "Ravi", "dept": "IT", "salary": 70},
    ]
    ordered = sorted(employees, key=lambda e: (e["dept"], -e["salary"]))
    print([e["name"] for e in ordered])                          # ['Sara', 'Ravi', 'Amar']
    print(max(employees, key=lambda e: e["salary"])["name"])     # Ravi

    # Best key of a dictionary
    scores = {"a": 3, "b": 9, "c": 5}
    print(max(scores, key=scores.get))                           # b
    # Python's sort is stable: equal items keep their original order

#   4) functools.reduce(function, iterable[, initial])
#       Combines all items into one value, from left to right.

    from functools import reduce

    print(reduce(lambda a, b: a * b, [1, 2, 3, 4]))       # 24
    # Steps: ((1*2)*3)*4

    print(reduce(lambda a, b: a if a > b else b, [3, 9, 4]))     # 9 (maximum)
    print(reduce(lambda acc, lst: acc + lst, [[1, 2], [3], [4, 5]], []))   # [1, 2, 3, 4, 5]

    # An initial value also makes empty input safe
    print(reduce(lambda a, b: a + b, [], 0))              # 0
    try:
        reduce(lambda a, b: a + b, [])
    except TypeError as error:
        print(error)                # reduce() of empty iterable with no initial value


#   5) functools.partial(func, *args, **kwargs)
#   Returns a new function with some arguments already filled in.

    from functools import partial

    def power(base, exp):
        return base ** exp

    square = partial(power, exp=2)
    cube = partial(power, exp=3)
    print(square(5), cube(2))                         # 25 8

    # Useful with map and callbacks
    to_int_from_binary = partial(int, base=2)
    print(list(map(to_int_from_binary, ["101", "11"])))      # [5, 3]

    def log(level, message):
        print(f"[{level}] {message}")

    info = partial(log, "INFO")
    info("Job started")                                # [INFO] Job started
    print(info.func.__name__, info.args)               # log ('INFO',)

#   6) operator module: ready-made functions (faster than lambda)
#       itemgetter, attrgetter, and methodcaller are themselves higher-order functions: they return a function.

    import operator
    from operator import itemgetter, attrgetter, methodcaller
    from functools import reduce

    print(reduce(operator.mul, [1, 2, 3, 4]))                  # 24
    print(list(map(operator.add, [1, 2], [10, 20])))           # [11, 22]

    pairs = [("Amar", 25), ("Sara", 22), ("Ravi", 30)]
    print(sorted(pairs, key=itemgetter(1)))                    # [('Sara', 22), ('Amar', 25), ('Ravi', 30)]

    class User:
        def __init__(self, name, age):
            self.name, self.age = name, age

    users = [User("Amar", 25), User("Sara", 22)]
    print([u.name for u in sorted(users, key=attrgetter("age"))])      # ['Sara', 'Amar']

    print(list(map(methodcaller("upper"), ["a", "b"])))        # ['A', 'B']

#   7) itertools helpers that take functions

    from itertools import groupby, takewhile, dropwhile, starmap, accumulate
    import operator

    nums = [1, 2, 3, 4, 5, 1, 2]
    print(list(takewhile(lambda x: x < 4, nums)))        # [1, 2, 3]   (stops at the first failure)
    print(list(dropwhile(lambda x: x < 4, nums)))        # [4, 5, 1, 2]

    print(list(starmap(pow, [(2, 3), (3, 2)])))          # [8, 9]  (each tuple becomes arguments)
    print(list(accumulate([1, 2, 3, 4])))                # [1, 3, 6, 10]
    print(list(accumulate([1, 2, 3, 4], operator.mul)))  # [1, 2, 6, 24]

    # groupby needs the data sorted by the same key
    data = ["pear", "fig", "kiwi", "apple", "plum"]
    for length, group in groupby(sorted(data, key=len), key=len):
        print(length, list(group))
    # 3 ['fig']
    # 4 ['pear', 'kiwi', 'plum']
    # 5 ['apple']

#   8) iter(callable, sentinel): call a function until it returns a value
#   Read a big file in 4096-byte chunks until read() returns b""
#   with open("big.bin", "rb") as f:
#     for chunk in iter(lambda: f.read(4096), b""):
#         process(chunk)

    import random
    random.seed(1)
    print(list(iter(lambda: random.randint(1, 3), 3)))   # numbers until a 3 appears

#   9) Returning functions: factories and closures

    def make_multiplier(factor):
        def multiplier(x):
            return x * factor
        return multiplier

    double = make_multiplier(2)
    triple = make_multiplier(3)
    print(double(10), triple(10))            # 20 30

    def make_validator(min_length, must_have):
        def validate(text):
            return len(text) >= min_length and must_have in text
        return validate

    password_ok = make_validator(8, "@")
    print(password_ok("abc@12345"), password_ok("abc"))   # True False

#   10) Both at once: compose and currying

    def compose(*funcs):
        """Return one function that runs funcs from left to right."""
        def run(value):
            for func in funcs:
                value = func(value)
            return value
        return run

    clean = compose(str.strip, str.lower, str.title)
    print(clean("   hELLO wORLD  "))         # Hello World

    # Currying: one function that returns another
    def add(a):
        return lambda b: a + b

    print(add(2)(3))                         # 5

#   11) Decorators are higher-order functions
    import functools
    import time

    def timer(func):                          # takes a function, returns a function
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start = time.perf_counter()
            result = func(*args, **kwargs)
            print(f"{func.__name__} took {time.perf_counter() - start:.4f}s")
            return result
        return wrapper

    @timer
    def total(n):
        return sum(range(n))

    print(total(1_000_000))

# A decorator WITH arguments is a function that returns a decorator
    def retry(times=3):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                for attempt in range(1, times + 1):
                    try:
                        return func(*args, **kwargs)
                    except Exception as error:
                        print(f"Attempt {attempt} failed: {error}")
                        if attempt == times:
                            raise
            return wrapper
        return decorator

    calls = {"n": 0}

    @retry(times=3)
    def flaky():
        calls["n"] += 1
        if calls["n"] < 3:
            raise ConnectionError("busy")
        return "ok"

    print(flaky())
    # Attempt 1 failed: busy
    # Attempt 2 failed: busy
    # ok

#   12) lru_cache takes a function and returns a faster one
    from functools import lru_cache

    @lru_cache(maxsize=None)
    def fib(n):
        return n if n < 2 else fib(n - 1) + fib(n - 2)

    print(fib(50))              # 12586269025
    print(fib.cache_info())

#   13) Old style comparison functions: cmp_to_key
    from functools import cmp_to_key

    def compare_length_then_alpha(a, b):
        if len(a) != len(b):
            return len(a) - len(b)
        return (a > b) - (a < b)

    print(sorted(["bb", "a", "ab", "c"], key=cmp_to_key(compare_length_then_alpha)))
    # ['a', 'c', 'ab', 'bb']

#   14) A data pipeline with higher-order functions (automation style)
    orders = [
        {"item": "pen", "price": 10, "qty": 3},
        {"item": "book", "price": 200, "qty": 1},
        {"item": "bag", "price": 500, "qty": 0},
    ]

    valid = filter(lambda o: o["qty"] > 0, orders)
    totals = map(lambda o: o["price"] * o["qty"], valid)
    print(sum(totals))                                   # 230

    # The same job as a generator expression
    print(sum(o["price"] * o["qty"] for o in orders if o["qty"] > 0))   # 230

#   15) Your own higher-order functions
    # Run a function many times
    def repeat(func, times):
        def run(x):
            for _ in range(times):
                x = func(x)
            return x
        return run

    print(repeat(lambda x: x * 2, 3)(1))                 # 8

    # Run a job and let the caller decide what to do on success or failure
    def run_job(job, on_success, on_error):
        try:
            result = job()
        except Exception as error:
            return on_error(error)
        return on_success(result)

    print(run_job(lambda: 10 / 2, lambda r: f"OK {r}", lambda e: f"Failed: {e}"))   # OK 5.0
    print(run_job(lambda: 10 / 0, lambda r: f"OK {r}", lambda e: f"Failed: {e}"))   # Failed: division by zero

    # Apply a function to every value of a dictionary
    def map_values(func, data):
        return {key: func(value) for key, value in data.items()}

    print(map_values(len, {"a": "xx", "b": "yyy"}))      # {'a': 2, 'b': 3}

#   16) Higher-order functions in the standard library (Module 4 link)
    import sched
    import threading
    import time

    def job(name):
        print("Running", name)

    scheduler = sched.scheduler(time.time, time.sleep)
    scheduler.enter(0, 1, job, argument=("backup",))      # "action" is a callback
    scheduler.run()                                       # Running backup

    worker = threading.Thread(target=job, args=("report",))   # "target" is a callback
    worker.start()
    worker.join()                                         # Running report

if __name__ == "__main__":
    main()
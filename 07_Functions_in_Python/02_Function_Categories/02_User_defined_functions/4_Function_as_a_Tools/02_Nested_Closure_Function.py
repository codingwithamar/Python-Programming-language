# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 01_Nested_Function.py
# Path    : Python-Programming-Language/07_Functions_in_Python/02_Function_Categories/02_User_defined_functions/4_Function_as_a_Tools/01_Nested_Closure_Function.py
# Subject : User Defined Functions
# Description : Nested closure Function
# =============================================================================

def main():
#%% Basic Concept
    # Nested function: the inner function can read the outer variable
    def outer():
        print("This is Outer function")

        def inner():
            print("This is inner function")         # reads outer's variable

        inner()

    outer()                        

# OUTPUT :
# This is Outer function
# This is inner function

#%% Basic Exmaple
    # Closure: the inner function outlives the outer function
    def make_multiplier(factor):
        def multiplier(x):
            return x * factor      # "factor" is remembered
        return multiplier

    double = make_multiplier(2)  # Now Double is not normal variable it contain make_multiplier(2) Function
    triple = make_multiplier(3)  # Now Triple is not normal variable it contain make_multiplier(3) Function

    print(double(10))              # 20
    print(triple(10))              # 30

#%% Advanced Examples
    # 1. Look at what the closure remembers
    print(double.__closure__)                       # (<cell at 0x...: int object at 0x...>,)
    print(double.__closure__[0].cell_contents)      # 2
    print(double.__code__.co_freevars)              # ('factor',)

    # 2. A closure with changing state needs nonlocal
    def make_counter(start=0):
        count = start

        def increment(step=1):
            nonlocal count
            count += step
            return count

        return increment

    c1 = make_counter()
    c2 = make_counter(100)
    print(c1(), c1(), c1(5))      # 1 2 7
    print(c2())                   # 101   -> each closure has its own state

    # 3. Function factory for configuration
    def make_logger(prefix, level="INFO"):
        def log(message):
            return f"[{level}] {prefix}: {message}"
        return log

    backup_log = make_logger("BACKUP")
    error_log = make_logger("REPORT", level="ERROR")
    print(backup_log("started"))   # [INFO] BACKUP: started
    print(error_log("failed"))     # [ERROR] REPORT: failed

    # 4. Data hiding without a class
    def make_account(balance):
        def deposit(amount):
            nonlocal balance
            balance += amount
            return balance

        def get_balance():
            return balance

        return deposit, get_balance

    deposit, get_balance = make_account(100)
    deposit(50)
    print(get_balance())           # 150
    # "balance" cannot be reached from outside directly

    # 5. Memoization with a closure
    def make_cached(func):
        cache = {}

        def wrapper(n):
            if n not in cache:
                cache[n] = func(n)
            return cache[n]

        return wrapper

    slow_square = lambda n: n * n
    fast_square = make_cached(slow_square)
    print(fast_square(9), fast_square(9))      # 81 81 (second call comes from the cache)

    # 6. LATE BINDING TRAP: closures remember the VARIABLE, not its value at that moment
    funcs = [lambda: i for i in range(3)]
    print([f() for f in funcs])                # [2, 2, 2]   <- surprise

    # Fix 1: capture the current value with a default argument
    funcs = [lambda i=i: i for i in range(3)]
    print([f() for f in funcs])                # [0, 1, 2]

    # Fix 2: use a factory function
    def make_func(i):
        return lambda: i

    funcs = [make_func(i) for i in range(3)]
    print([f() for f in funcs])                # [0, 1, 2]

    # Fix 3: functools.partial
    from functools import partial
    funcs = [partial(lambda i: i, i) for i in range(3)]
    print([f() for f in funcs])                # [0, 1, 2]

    # 7. A closure sees later changes of the outer variable
    def outer():
        x = 1
        def inner():
            return x
        x = 2                      # changed AFTER inner was defined
        return inner

    print(outer()())               # 2   -> the closure reads the variable, not a copy

    # 8. Decorators are closures
    import functools

    def log_calls(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f"Calling {func.__name__}")
            return func(*args, **kwargs)
        return wrapper

    @log_calls
    def hello(name):
        return f"Hi {name}"

    print(hello("Amar"))           # Calling hello, then Hi Amar

    # 9. Closure vs class for state
    class Counter:
        def __init__(self):
            self.count = 0
        def __call__(self):
            self.count += 1
            return self.count

    c = Counter()
    print(c(), c())                # 1 2  -> same result, more setup


if __name__ == "__main__":
    main()
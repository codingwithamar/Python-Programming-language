# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 1_ii_Decorators_with_Parameters.py
# Path    : Python-Programming-Language/07_Functions_in_Python/02_Function_Categories/02_User_defined_functions/5_Function_Definitions_and_Expressions/1_Decorators/1_ii_Decorators_with_Parameters.py
# Subject : User Defined Functions
# Description : Decorators with Arguments
# =============================================================================

def main():
#%% Basic Examples
    import functools

    def repeat(times):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                result = None
                for _ in range(times):
                    result = func(*args, **kwargs)
                return result
            return wrapper
        return decorator

    @repeat(3)
    def hello(name):
        print(f"Hi {name}")

    hello("Amar")
    # Hi Amar
    # Hi Amar
    # Hi Amar

#%% Advanced Examples
    import functools
    import time

    # 1. Retry decorator (very common in automation)
    def retry(times=3, delay=1.0, exceptions=(Exception,)):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                for attempt in range(1, times + 1):
                    try:
                        return func(*args, **kwargs)
                    except exceptions as error:
                        print(f"Attempt {attempt} failed: {error}")
                        if attempt == times:
                            raise                      # give up on the last attempt
                        time.sleep(delay)
            return wrapper
        return decorator

    calls = {"n": 0}

    @retry(times=3, delay=0, exceptions=(ConnectionError,))
    def unstable_connect():
        calls["n"] += 1
        if calls["n"] < 3:
            raise ConnectionError("server busy")
        return "connected"

    print(unstable_connect())
    # Attempt 1 failed: server busy
    # Attempt 2 failed: server busy
    # connected

    # 2. Decorator that works both as @retry and as @retry(times=5)
    def retry2(func=None, *, times=3):
        def decorator(f):
            @functools.wraps(f)
            def wrapper(*args, **kwargs):
                for attempt in range(1, times + 1):
                    try:
                        return f(*args, **kwargs)
                    except Exception:
                        if attempt == times:
                            raise
            return wrapper

        if func is not None:           # used as @retry2 (no brackets)
            return decorator(func)
        return decorator               # used as @retry2(times=5)

    @retry2
    def a(): return "a"

    @retry2(times=5)
    def b(): return "b"

    print(a(), b())                    # a b

    # 3. Check the arguments of the decorator itself
    def limit(max_calls):
        if max_calls < 1:
            raise ValueError("max_calls must be at least 1")    # fails at decoration time
        def decorator(func):
            count = 0
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                nonlocal count
                if count >= max_calls:
                    raise RuntimeError(f"{func.__name__} can run only {max_calls} times")
                count += 1
                return func(*args, **kwargs)
            return wrapper
        return decorator

    @limit(2)
    def job():
        return "done"

    print(job(), job())                # done done
    # job()                            # RuntimeError: job can run only 2 times

    # 4. A decorator that takes a function as its argument
    def with_callback(callback):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                result = func(*args, **kwargs)
                callback(result)
                return result
            return wrapper
        return decorator

    @with_callback(lambda r: print("Result was", r))
    def square(x):
        return x * x

    square(6)                          # Result was 36

if __name__ == "__main__":
    main()
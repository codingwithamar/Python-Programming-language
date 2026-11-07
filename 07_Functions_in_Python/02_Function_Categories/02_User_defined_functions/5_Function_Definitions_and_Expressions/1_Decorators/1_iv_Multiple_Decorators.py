# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 1_iv_Multiple_Decorators.py
# Path    : Python-Programming-Language/07_Functions_in_Python/02_Function_Categories/02_User_defined_functions/5_Function_Definitions_and_Expressions/1_Decorators/1_iv_Multiple_Decorators.py
# Subject : User Defined Function
# Description : Decorators - Multiple Decorators
# =============================================================================

def main():
#%% Basic Concept
    '''
    @a
    @b
    @c
    def f(): ...

    # is the same as:
    f = a(b(c(f)))
    '''

#%% Basic Examples
    import functools

    def bold(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return "<b>" + func(*args, **kwargs) + "</b>"
        return wrapper

    def italic(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return "<i>" + func(*args, **kwargs) + "</i>"
        return wrapper

    @bold
    @italic
    def text():
        return "hello"

    print(text())              # <b><i>hello</i></b>
    # text = bold(italic(text))

#%% Advanced Examples
    import functools

    def trace(name):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                print(f"enter {name}")
                result = func(*args, **kwargs)
                print(f"exit  {name}")
                return result
            return wrapper
        return decorator

    @trace("A")
    @trace("B")
    @trace("C")
    def task():
        print("task runs")

    task()
    # enter A
    # enter B
    # enter C
    # task runs
    # exit  C
    # exit  B
    # exit  A

    # 1. Order matters. Compare:
    def uppercase(func):
        @functools.wraps(func)
        def wrapper(*a, **k):
            return func(*a, **k).upper()
        return wrapper

    def exclaim(func):
        @functools.wraps(func)
        def wrapper(*a, **k):
            return func(*a, **k) + "!"
        return wrapper

    @uppercase
    @exclaim
    def hi1():
        return "hi"

    @exclaim
    @uppercase
    def hi2():
        return "hi"

    print(hi1())               # HI!  -> exclaim runs first (inner), then uppercase
    print(hi2())               # HI!  -> same visible text here, but the steps differ

    # 2. A realistic stack: log the outside, retry inside, time the original
    # @log_calls
    # @retry(times=3)
    # @timer
    # def download(url): ...

    # 3. With @property, @classmethod, @staticmethod: put them on the OUTSIDE (top)
    class Demo:
        @staticmethod
        @functools.lru_cache(maxsize=None)
        def square(n):
            return n * n

    print(Demo.square(5))      # 25

    # 4. Stacking with wraps: __wrapped__ points one level down
    print(task.__wrapped__.__name__)    # task

if __name__ == "__main__":
    main()
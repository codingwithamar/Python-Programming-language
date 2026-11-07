# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 1_viii_Class_Base_Decorators.py
# Path    : Python-Programming-Language/07_Functions_in_Python/02_Function_Categories/02_User_defined_functions/5_Function_Definitions_and_Expressions/1_Decorators/1_viii_Class_Base_Decorators.py
# Subject : User Defined FUNCTIONS
# Description : Class Bse Decorators
# =============================================================================

def main():
#%% Basic Examples
    import functools

    class CountCalls:
        def __init__(self, func):
            functools.update_wrapper(self, func)     # like @wraps, for classes
            self.func = func
            self.calls = 0

        def __call__(self, *args, **kwargs):
            self.calls += 1
            return self.func(*args, **kwargs)

    @CountCalls
    def hello():
        return "hi"

    hello()
    hello()
    print(hello.calls)           # 2
    print(hello.__name__)        # hello

#%% Advanced Examples
    import functools

    # 1. A class decorator with arguments
    class Retry:
        def __init__(self, times=3):
            self.times = times

        def __call__(self, func):                    # receives the function
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                for attempt in range(1, self.times + 1):
                    try:
                        return func(*args, **kwargs)
                    except Exception:
                        if attempt == self.times:
                            raise
            return wrapper

    @Retry(times=2)
    def work():
        return "ok"

    print(work())                # ok

    # 2. Trap: a class-based decorator does NOT become a method automatically
    class CountCalls2:
        def __init__(self, func):
            self.func = func
        def __call__(self, *args, **kwargs):
            return self.func(*args, **kwargs)

    class Demo:
        @CountCalls2
        def hello(self):
            return "hi"

    # Demo().hello()    # TypeError: hello() missing 1 required positional argument: 'self'
    # The instance has no __get__, so "self" is not passed.
    # Fix: use a function wrapper, or add a __get__ method to the class.

if __name__ == "__main__":
    main()
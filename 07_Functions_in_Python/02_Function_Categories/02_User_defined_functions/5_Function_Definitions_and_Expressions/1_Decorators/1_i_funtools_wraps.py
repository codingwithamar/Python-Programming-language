# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 2_funtools_wraps.py
# Path    : Python-Programming-Language/07_Functions_in_Python/02_Function_Categories/02_User_defined_functions/5_Function_Definitions_and_Expressions/1_Decorators/2_funtools_wraps.py
# Subject : User Define Functions
# Description : Decorators using funtools.wrap
# =============================================================================

def main():
#%% Basic Examples
    import functools

    def timer(func):
        @functools.wraps(func)               # add this line above the wrapper
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper

    @timer
    def total(n):
        """Add numbers up to n."""
        return sum(range(n))

    print(total.__name__)      # total
    print(total.__doc__)       # Add numbers up to n.

#%% Advanced Examples
    import functools
    import inspect

    def log_calls(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f"Calling {func.__name__}")
            return func(*args, **kwargs)
        return wrapper

    @log_calls
    def connect(host: str, port: int = 8080) -> str:
        """Connect to a server."""
        return f"{host}:{port}"

    # 1. Metadata is kept
    print(connect.__name__)               # connect
    print(connect.__doc__)                # Connect to a server.
    print(connect.__annotations__)        # {'host': <class 'str'>, 'port': <class 'int'>, 'return': <class 'str'>}

    # 2. The original function is available through __wrapped__
    print(connect.__wrapped__)            # <function connect at 0x...>
    print(connect.__wrapped__("a.com"))   # a.com:8080   -> runs the original, with no logging

    # 3. help() and inspect.signature show the ORIGINAL signature
    print(inspect.signature(connect))     # (host: str, port: int = 8080) -> str

    # 4. Without wraps, the signature shows only (*args, **kwargs)
    def plain(func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper

    @plain
    def connect2(host: str, port: int = 8080) -> str:
        return f"{host}:{port}"

    print(inspect.signature(connect2))    # (*args, **kwargs)

    # 5. Remove the decorator for testing: use __wrapped__
    original = connect.__wrapped__

    # 6. What wraps copies
    print(functools.WRAPPER_ASSIGNMENTS)
    # ('__module__', '__name__', '__qualname__', '__doc__', '__annotations__')
    # (newer Python versions may add '__type_params__')
    print(functools.WRAPPER_UPDATES)      # ('__dict__',)


if __name__ == "__main__":
    main()
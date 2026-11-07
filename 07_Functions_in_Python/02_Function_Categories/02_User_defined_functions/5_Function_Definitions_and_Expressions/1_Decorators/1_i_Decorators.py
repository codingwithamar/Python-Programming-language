# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 1_Decorators.py
# Path    : Python-Programming-Language/07_Functions_in_Python/02_Function_Categories/02_User_defined_functions/5. Function_Definitions_and_Expressions/1_Decorators/1_Decorators.py
# Subject : User Defined Functions
# Description : Decorators
# =============================================================================

def main():
#%% Basic Concept
    # Same as a Without Decorator Syntax
    def say_hello():
        print("Hello!")

    say_hello = my_decorator(say_hello)    # this is what @my_decorator does
    say_hello()

    # With Decorator Syntax
    def decorator(func):
        def wrapper():
            print("Before Function Execution")
            func()
            print("After Function Execution")

        return wrapper


    @decorator
    def greet():
        print("Hello Python")

    greet()

#%% Basic Example
    def my_decorator(func):
        def wrapper():
            print("Before the function runs")
            func()
            print("After the function runs")
        return wrapper

    @my_decorator
    def say_hello():
        print("Hello!")

    say_hello()
    
    #OUTPUT : 
    # Before the function runs
    # Hello!
    # After the function runs

#   say_hello = my_decorator(say_hello)   # the name now points to the wrapped version

#1 Accept any arguments and return the result
    def log_calls(func):
        def wrapper(*args, **kwargs):                  # accept any arguments
            print(f"Calling {func.__name__} with {args} {kwargs}")
            result = func(*args, **kwargs)             # pass them on
            print(f"{func.__name__} returned {result}")
            return result                              # give back the result
        return wrapper

    @log_calls
    def add(a, b):
        return a + b

    print(add(2, 3))

    #OUTPUT :
    # Calling add with (2, 3) {}
    # add returned 5
    # 5

#2 When the Immediately decorator runs
    def show_time(func):
        print(f"Decorating {func.__name__}")      # runs once, at definition time
        return func                               # returning the same function is allowed

    @show_time
    def a():
        pass
    # prints immediately: Decorating a

    @show_time
    def b():
        pass
    # prints immediately: Decorating b

#3 Timer Decorator
    import time

    def timer(func):
        def wrapper(*args, **kwargs):
            start = time.perf_counter()
            result = func(*args, **kwargs)
            elapsed = time.perf_counter() - start
            print(f"{func.__name__} took {elapsed:.4f} seconds")
            return result
        return wrapper

    @timer
    def total(n):
        return sum(range(n))

    print(total(1_000_000))
    #OUTPUT : 
    # total took 0.0123 seconds   (time will differ)
    # 499999500000

if __name__ == "__main__":
    main()
# %%

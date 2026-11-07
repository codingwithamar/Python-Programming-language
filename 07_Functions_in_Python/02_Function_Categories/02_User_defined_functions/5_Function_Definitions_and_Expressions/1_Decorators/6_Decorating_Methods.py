# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 1_v_Decorating_Methods.py
# Path    : Python-Programming-Language/07_Functions_in_Python/02_Function_Categories/02_User_defined_functions/5_Function_Definitions_and_Expressions/1_Decorators/1_v_Decorating_Methods.py
# Subject : User derfined Functions
# Description : Decorating methods
# =============================================================================

def main():
#%% Basic Examples
    import functools

    def log_calls(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f"Calling {func.__name__}")
            return func(*args, **kwargs)
        return wrapper

    class Account:
        def __init__(self, balance):
            self.balance = balance

        @log_calls
        def deposit(self, amount):
            self.balance += amount
            return self.balance

    acc = Account(100)
    print(acc.deposit(50))
    # Calling deposit
    # 150

#%% Advanced Examples
    import functools

    # A decorator that uses the instance (self)
    def require_positive_balance(method):
        @functools.wraps(method)
        def wrapper(self, *args, **kwargs):
            if self.balance < 0:
                raise ValueError("Account is overdrawn")
            return method(self, *args, **kwargs)
        return wrapper

    class Account:
        def __init__(self, balance):
            self.balance = balance

        @require_positive_balance
        def withdraw(self, amount):
            self.balance -= amount
            return self.balance

    print(Account(100).withdraw(30))     # 70
    # Account(-5).withdraw(1)            # ValueError: Account is overdrawn

    # Decorating an existing method after the class is created
    def slow_method(self):
        return "result"

    Account.slow = log_calls(slow_method)
    print(Account(1).slow())
    # Calling slow_method
    # result

if __name__ == "__main__":
    main()
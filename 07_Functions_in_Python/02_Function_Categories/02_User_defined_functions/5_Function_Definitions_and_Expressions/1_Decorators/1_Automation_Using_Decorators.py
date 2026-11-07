# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 1_0_Automation_Using_Decorators.py
# Path    : Python-Programming-Language/07_Functions_in_Python/02_Function_Categories/02_User_defined_functions/5_Function_Definitions_and_Expressions/1_Decorators/1_0_Automation_Using_Decorators.py
# Subject : User Defined Functions
# Description : Automation Using Decorators
# =============================================================================

import functools
import time
import warnings

def main():
    # 1. Log calls and errors
    def log(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                print(f"[OK] {func.__name__}")
                return result
            except Exception as error:
                print(f"[FAIL] {func.__name__}: {error}")
                raise
        return wrapper

    # 2. Cache with expiry (time to live)
    def ttl_cache(seconds):
        def decorator(func):
            store = {}
            @functools.wraps(func)
            def wrapper(*args):
                now = time.monotonic()
                if args in store and now - store[args][1] < seconds:
                    return store[args][0]
                value = func(*args)
                store[args] = (value, now)
                return value
            return wrapper
        return decorator

    @ttl_cache(seconds=60)
    def get_rate(currency):
        print("calling the server...")
        return 83.5

    print(get_rate("USD"))               # calling the server... then 83.5
    print(get_rate("USD"))               # 83.5   (from the cache)

    # 3. Check arguments
    def positive_args(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for value in (*args, *kwargs.values()):
                if value <= 0:
                    raise ValueError(f"{value} must be positive")
            return func(*args, **kwargs)
        return wrapper

    @positive_args
    def area(width, height):
        return width * height

    print(area(2, 3))                    # 6
    # area(-1, 3)                        # ValueError: -1 must be positive

    # 4. Permission check
    def require_role(role):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(user, *args, **kwargs):
                if role not in user.get("roles", []):
                    raise PermissionError(f"{role} role required")
                return func(user, *args, **kwargs)
            return wrapper
        return decorator

    @require_role("admin")
    def delete_logs(user):
        return "logs deleted"

    print(delete_logs({"roles": ["admin"]}))     # logs deleted
    # delete_logs({"roles": ["guest"]})          # PermissionError: admin role required

    # 5. Run only once
    def once(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if not wrapper.called:
                wrapper.called = True
                wrapper.result = func(*args, **kwargs)
            return wrapper.result
        wrapper.called = False
        wrapper.result = None
        return wrapper

    @once
    def initialize():
        print("initializing...")
        return "ready"

    print(initialize())                  # initializing... then ready
    print(initialize())                  # ready   (not run again)

    # 6. Deprecated warning
    def deprecated(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            warnings.warn(f"{func.__name__} is deprecated", DeprecationWarning, stacklevel=2)
            return func(*args, **kwargs)
        return wrapper

    # 7. Register functions in a dictionary (dispatch table)
    COMMANDS = {}

    def command(name):
        def decorator(func):
            COMMANDS[name] = func
            return func                  # return the original, no wrapper needed
        return decorator

    @command("start")
    def start():
        return "Starting"

    @command("stop")
    def stop():
        return "Stopping"

    print(COMMANDS["start"](), COMMANDS["stop"]())     # Starting Stopping

    # 8. Use a decorator with the sched module (Module 4 link)
    import sched

    def scheduled(delay):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                scheduler = sched.scheduler(time.time, time.sleep)
                scheduler.enter(delay, 1, func, argument=args, kwargs=kwargs)
                scheduler.run()
            return wrapper
        return decorator

    @scheduled(0)
    def report(name):
        print("Report for", name)

    report("Amar")                       # Report for Amar

if __name__ == "__main__":
    main()
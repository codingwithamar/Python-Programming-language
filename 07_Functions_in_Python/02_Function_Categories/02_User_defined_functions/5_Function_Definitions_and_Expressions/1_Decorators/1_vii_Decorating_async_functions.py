# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 1_vii_Decorating_async_functions.py
# Path    : Python-Programming-Language/07_Functions_in_Python/02_Function_Categories/02_User_defined_functions/5_Function_Definitions_and_Expressions/1_Decorators/1_vii_Decorating_async_functions.py
# Subject : User Defined Functions
# Description : Decorating async functions
# =============================================================================

def main():
    import asyncio
    import functools
    import time

    def async_timer(func):
        @functools.wraps(func)
        async def wrapper(*args, **kwargs):
            start = time.perf_counter()
            result = await func(*args, **kwargs)          # await the coroutine
            print(f"{func.__name__} took {time.perf_counter() - start:.2f}s")
            return result
        return wrapper

    @async_timer
    async def fetch():
        await asyncio.sleep(0.2)
        return "data"

    print(asyncio.run(fetch()))
    # fetch took 0.20s
    # data

if __name__ == "__main__":
    main()


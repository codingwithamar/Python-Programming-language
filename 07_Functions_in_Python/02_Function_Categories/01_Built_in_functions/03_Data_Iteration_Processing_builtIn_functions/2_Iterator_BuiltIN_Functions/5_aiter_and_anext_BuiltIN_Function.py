# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 5_aiter_and_anext_BuiltIN_Function.py
# Path    : Python-Programming-Language/07_Functions_in_Python/02_Function_Categories/01_Built_in_functions/03_Data_Iteration_Processing_builtIn_functions/2_Iterator_BuiltIN_Functions/5_aiter_and_anext_BuiltIN_Function.py
# Subject : Built-in functions in python
# Description : aiter() and anext() - These are the asynchronous versions of iter() and next()
# =============================================================================

def main():
    import asyncio

    async def countdown(n):
        while n > 0:
            yield n
            n -= 1
            await asyncio.sleep(0.1)

    async def main():
        it = aiter(countdown(3))
        print(await anext(it))      # 3
        print(await anext(it))      # 2
        print(await anext(it))      # 1
        print(await anext(it, "done"))   # done -> default instead of an error

    asyncio.run(main())


if __name__ == "__main__":
    main()
# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 1_async_def_and_await_Basics.py
# Path    : Python-Programming-Language/07_Functions_in_Python/02_Function_Categories/02_User_defined_functions/5_Function_Definitions_and_Expressions/3_Coroutine_Function/1_async_def_and_await_Basics.py
# Subject : User Defined Functions
# Description : Coroutine Functions/async def and await Basics
# =============================================================================

def main():
#%% Basic Example
    import asyncio

    async def hello():
        print("start")
        await asyncio.sleep(1)          # pause for 1 second, without blocking the loop
        print("end")
        return "done"

    coro = hello()
    print(type(coro))                   # <class 'coroutine'>
    # nothing has been printed by hello() yet

    result = asyncio.run(coro)          # run the coroutine to the end
    # start
    # end
    print(result)                       # done

#%% Advanced Examples and common mistakes
    import asyncio  # Provides tools for asynchronous programming and event-loop management.
    import inspect  # Provides functions to inspect coroutine functions, objects, and their states.
    import keyword  # Provides functions to check Python keywords.
    import time     # Provides performance measurement using perf_counter().


    # ============================================================
    # 1. COROUTINE FUNCTION
    # ============================================================

    async def get_value():
        # async def defines a coroutine function.
        # Calling this function creates a coroutine object.
        # The function body does not execute until the coroutine is awaited or driven.
        return 42          # Returns 42 as the coroutine's result.


    # ============================================================
    # 2. ASYNC FUNCTION WITH AWAIT
    # ============================================================

    async def work(name, delay):
        # await suspends the current coroutine until the awaited operation completes.
        # asyncio.sleep() suspends the coroutine without blocking the event loop.
        await asyncio.sleep(delay)

        # Execution resumes after the specified delay.
        return f"{name} completed"


    # ============================================================
    # 3. SEQUENTIAL EXECUTION
    # ============================================================

    async def sequential():
        # Records the starting time for performance measurement.
        start = time.perf_counter()

        # Task A is awaited and completed before Task B starts.
        a = await work("Task A", 1)

        # Task B starts only after Task A completes.
        b = await work("Task B", 1)

        # Task C starts only after Task B completes.
        c = await work("Task C", 1)

        # Prints the results of all three tasks.
        print(a, b, c)

        # Displays the total execution time.
        # Since tasks execute sequentially, the total time is approximately 3 seconds.
        print(f"Sequential time: {time.perf_counter() - start:.1f}s")


    # ============================================================
    # 4. RETURN VALUES AND EXCEPTION HANDLING
    # ============================================================

    async def risky(n):
        # Checks whether the supplied value is negative.
        if n < 0:

            # Raises ValueError if the condition is True.
            raise ValueError("Negative value")

        # Returns the value multiplied by 2.
        return n * 2


    # ============================================================
    # 5. ASYNC GENERATOR
    # ============================================================

    async def async_generator():
        # async def combined with yield defines an asynchronous generator function.
        # Calling it creates an asynchronous generator object.
        yield 1               # Produces the first value.
        yield 2               # Produces the second value.
        yield 3               # Produces the third value.


    # ============================================================
    # 6. MAIN COROUTINE
    # ============================================================

    async def main():

        # --------------------------------------------------------
        # 1. Forgetting await
        # --------------------------------------------------------

        c = get_value()
        # Calling a coroutine function without await creates a coroutine object.
        # It does not execute the coroutine body.

        print("Coroutine object:", inspect.iscoroutine(c))
        # inspect.iscoroutine() returns True if c is a coroutine object.

        print("Correct value:", await c)
        # await starts and waits for the coroutine to complete.
        # The returned result is 42.

        # --------------------------------------------------------
        # 2. await usage
        # --------------------------------------------------------

        value = await get_value()
        # Calls get_value(), creates a coroutine object,
        # awaits it, and stores its returned value.

        print("Await result:", value)
        # Prints the result returned by the coroutine: 42.

        # --------------------------------------------------------
        # 3. Coroutine can be awaited only once
        # --------------------------------------------------------

        c = get_value()
        # Creates a new coroutine object.

        print("First await:", await c)
        # Awaits the coroutine and receives its result.
        # The coroutine has now completed.

        try:
            await c
            # Attempts to reuse the already-awaited coroutine.
            # A completed coroutine cannot be awaited again.

        except RuntimeError as error:
            # Catches the RuntimeError raised by attempting to reuse it.
            print("Second await:", error)

        # --------------------------------------------------------
        # 4. Sequential awaits
        # --------------------------------------------------------

        await sequential()
        # Executes the sequential() coroutine.
        # Each work() coroutine completes before the next one starts.

        # --------------------------------------------------------
        # 5. Inspect coroutine
        # --------------------------------------------------------

        print("Is coroutine function:",
            inspect.iscoroutinefunction(get_value))
        # Returns True because get_value is defined using async def.

        c = get_value()
        # Creates a new coroutine object without starting its execution.

        print("Is coroutine:", inspect.iscoroutine(c))
        # Checks whether c is a coroutine object.

        print("Is awaitable:", inspect.isawaitable(c))
        # Checks whether c can be used with the await expression.

        print("Coroutine state:", inspect.getcoroutinestate(c))
        # Returns CORO_CREATED because the coroutine has not started yet.

        c.close()
        # Closes the coroutine.
        # Closing an unstarted coroutine prevents it from being left unawaited.

        print("After close:",
            inspect.getcoroutinestate(c))
        # Returns CORO_CLOSED because the coroutine has been closed.

        print("Function type:", type(get_value))
        # Displays the type of the coroutine function itself.
        # It is a function object, not a coroutine object.

        # --------------------------------------------------------
        # 6. Coroutine driven by send()
        # --------------------------------------------------------

        c = get_value()
        # Creates another fresh coroutine object.

        try:
            c.send(None)
            # send(None) starts driving the coroutine.
            # Since get_value() contains no await expression,
            # it completes immediately.
            # Completion raises StopIteration.

        except StopIteration as stop:
            # The coroutine's return value is stored in stop.value.
            print("Send result:", stop.value)

        # --------------------------------------------------------
        # 7. Async generator
        # --------------------------------------------------------

        agen = async_generator()
        # Calling an asynchronous generator function creates
        # an asynchronous generator object.
        # Its body has not started executing yet.

        print("Async generator type:", type(agen))
        # Displays the type of the asynchronous generator object.

        async for item in agen:
            # async for iterates over an asynchronous iterable.
            # It retrieves values asynchronously until the generator is exhausted.
            print("Generator value:", item)

        # --------------------------------------------------------
        # 8. Return and exception handling
        # --------------------------------------------------------

        print("Risky result:", await risky(5))
        # Awaits risky(5).
        # Since 5 is not negative, the function returns 10.

        try:
            await risky(-1)
            # Awaits risky(-1).
            # Since -1 is negative, the function raises ValueError.

        except ValueError as error:
            # Catches the ValueError raised inside risky().
            print("Caught exception:", error)

        # --------------------------------------------------------
        # 9. async and await are keywords
        # --------------------------------------------------------

        print("async keyword:", keyword.iskeyword("async"))
        # Checks whether async is a reserved Python keyword.
        # Returns True in modern Python versions.

        print("await keyword:", keyword.iskeyword("await"))
        # Checks whether await is a reserved Python keyword.
        # Returns True in modern Python versions.


    # ============================================================
    # 7. RUN MAIN COROUTINE
    # ============================================================

    asyncio.run(main())
    # asyncio.run() creates and manages an event loop.
    # It executes the main() coroutine until completion.
    # It also handles event-loop shutdown.

if __name__ == "__main__":
    main()
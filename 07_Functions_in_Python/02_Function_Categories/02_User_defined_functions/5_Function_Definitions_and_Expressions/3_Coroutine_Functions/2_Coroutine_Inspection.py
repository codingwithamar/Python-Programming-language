# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 2_Coroutine_Inspection.py
# Path    : Python-Programming-Language/07_Functions_in_Python/02_Function_Categories/02_User_defined_functions/5_Function_Definitions_and_Expressions/3_Coroutine_Functions/2_Coroutine_Inspection.py
# Subject : Enter Subject
# Description : Description
# =============================================================================

def main():
#%% Basic Examples  
    import asyncio
    import inspect

    # Define a coroutine function.
    async def greet():

        return "Hello"

    # Calling the function creates a coroutine object.
    coro = greet()

    # Check whether greet is a coroutine function.
    print("Coroutine function:",
        inspect.iscoroutinefunction(greet))

    # Check whether coro is a coroutine object.
    print("Coroutine object:",
        inspect.iscoroutine(coro))

    # Check whether coro supports the await expression.
    print("Awaitable:",
        inspect.isawaitable(coro))

    # Close the coroutine because we have not awaited it.
    coro.close()

#%% Advanced Example
    import asyncio
    import inspect

    # Define a coroutine.
    async def worker(event):

        # Suspend until the event is set.
        await event.wait()

        return "Worker completed"

    async def main():
        # Create an Event to control when the coroutine resumes.
        event = asyncio.Event()

        # Create a coroutine object without starting it.
        coro = worker(event)

        # Check the state before execution.
        print("State 1:",
            inspect.getcoroutinestate(coro))

        # Schedule the coroutine as a Task.
        task = asyncio.create_task(coro)

        # Give the event loop an opportunity to start the task.
        await asyncio.sleep(0)

        # The coroutine is now waiting at event.wait().
        print("State 2:",
            inspect.getcoroutinestate(coro))

        # Set the event to release the waiting coroutine.
        event.set()

        # Wait for the task to finish and get its result.
        result = await task

        print("Result:", result)

        # Check the state after completion.
        print("State 3:",
            inspect.getcoroutinestate(coro))

    asyncio.run(main())

if __name__ == "__main__":
    main()
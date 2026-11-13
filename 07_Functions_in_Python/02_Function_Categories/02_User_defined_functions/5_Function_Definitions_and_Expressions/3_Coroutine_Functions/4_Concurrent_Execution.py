# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 4_Concurrent_Execution.py
# Path    : Python-Programming-Language/07_Functions_in_Python/02_Function_Categories/02_User_defined_functions/5_Function_Definitions_and_Expressions/3_Coroutine_Functions/4_Concurrent_Execution.py
# Subject : User Defined FUnctions
# Description : Coroutine Function / Concurrent Execution
# =============================================================================

def main():
#%% Basic Example
    import asyncio

    async def worker(name):     # Define an asynchronous task.
        print(name, "started")
        await asyncio.sleep(2)   # Simulate an asynchronous operation.
        print(name, "completed")

    async def main():   # Schedule all three coroutines for concurrent execution.
        await asyncio.gather(
            worker("Task A"),
            worker("Task B"),
            worker("Task C")
        )

        print("All tasks completed")    # This line executes after all three finish.

    asyncio.run(main()) # Execute the main coroutine.
    '''
    Code explanation:
    1. asyncio.gather() schedules the supplied coroutines.
    2. All three tasks can make progress concurrently.
    3. Each task suspends for two seconds.
    4. The event loop can run other tasks during that time.
    5. gather() waits until all three complete.
    '''

#%% Advanced Example
    import asyncio
    import time

    async def fetch_data(name, delay):  # Simulate fetching data from an API.
        print(f"{name}: Request started")
        await asyncio.sleep(delay)   # Simulate network waiting time.
        print(f"{name}: Response received")
        return f"{name} data"   # Return the response data.

    async def main():
        start = time.perf_counter()   # Record the starting time.

        # Run all API requests concurrently.
        results = await asyncio.gather(
            fetch_data("API 1", 3),
            fetch_data("API 2", 2),
            fetch_data("API 3", 1)
        )

        print("\nResults:")   # Display all returned results.

        for result in results:
            print(result)

        elapsed = time.perf_counter() - start   # Calculate total execution time.
        print(f"\nTotal time: {elapsed:.1f} seconds")

    asyncio.run(main())   # Execute the main coroutine.

if __name__ == "__main__":
    main()
# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 5_Task_Management.py
# Path    : Python-Programming-Language/07_Functions_in_Python/02_Function_Categories/02_User_defined_functions/5_Function_Definitions_and_Expressions/3_Coroutine_Functions/5_Task_Management.py
# Description : Coroutine Function / Task Management
# =============================================================================

def main():
#%% Basic Example
    import asyncio

    async def worker():     # Define a coroutine.
        print("Worker started")
        await asyncio.sleep(2)  # Suspend the coroutine for 2 seconds.
        print("Worker completed")
        return "Success"

    async def main():
        task = asyncio.create_task(worker())    # Create a Task from the worker coroutine.
        print("Task created")
        result = await task     # Wait for the task to complete.
        print("Task result:", result)   # Display the returned result.
        print("Task done:", task.done())    # Check whether the task has finished.

    asyncio.run(main())     # Execute the main coroutine.
    '''
    Code explanation:
    1. asyncio.create_task() schedules a coroutine as a Task.
    2. The task can execute when the event loop gets control.
    3. await task waits for the task to complete.
    4. task.done() checks whether it has finished.
    '''

#%% Advanced example – Task cancellation
    import asyncio

    async def worker():     # Define a coroutine that performs long-running work.
        try:
            print("Worker started")
            await asyncio.sleep(10) # Simulate a long-running operation.
            print("Worker completed")

        except asyncio.CancelledError:      # Handle the cancellation request.
            print("Worker was cancelled")
            raise   # Re-raise cancellation so the Task remains cancelled.

    async def main():
        task = asyncio.create_task(worker())    # Schedule the worker as a Task.
        await asyncio.sleep(2)  # Allow the worker to start and run for 2 seconds.
        print("Cancelling task...")
        task.cancel()   # Request cancellation of the Task.

        try:
            await task  # Wait for cancellation to be processed.

        except asyncio.CancelledError:   # Catch the cancellation propagated by the Task.
            print("Cancellation confirmed")

        print("Task done:", task.done())    # Check whether the task has finished.

        print("Task cancelled:", task.cancelled())  # Check whether the task was cancelled.

    asyncio.run(main())     # Execute the main coroutine.
    '''
    Code explanation:
    - create_task() schedules the worker.
    - task.cancel() requests cancellation.
    - CancelledError is raised inside the coroutine when cancellation is processed.
    - The coroutine can perform cleanup before re-raising the exception.
    - await task allows the caller to observe the cancellation.
    - task.cancelled() confirms whether the task was cancelled.
    '''

#%% Advanced example – TaskGroup
#asyncio.TaskGroup is available from Python 3.11 onwards. It provides structured task management.
    import asyncio

    async def worker(name, delay):  # Define a worker coroutine.
        print(name, "started")
        await asyncio.sleep(delay)  # Simulate asynchronous work.
        print(name, "completed")

    async def main():
        async with asyncio.TaskGroup() as group:    # Create a TaskGroup context.
            group.create_task(worker("Task A", 3))  # Create the first task.
            group.create_task(worker("Task B", 2))  # Create the second task.
            group.create_task(worker("Task C", 1))  # Create the third task.
        
        print("All tasks completed")# The program reaches here only after all tasks finish.

    asyncio.run(main())  # Execute the main coroutine.
    '''
    Code explanation:
    - TaskGroup() creates a group to manage related tasks.
    - group.create_task() schedules each coroutine.
    - All tasks make progress concurrently.
    - Exiting the async with block waits for all tasks.
    - If a task fails with an exception, the TaskGroup cancels remaining tasks and reports the failure using an exception group.
    '''

if __name__ == "__main__":
    main()
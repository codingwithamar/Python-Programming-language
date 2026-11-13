# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 6_Synchronization.py
# Path    : Python-Programming-Language/07_Functions_in_Python/02_Function_Categories/02_User_defined_functions/5_Function_Definitions_and_Expressions/3_Coroutine_Functions/6_Synchronization.py
# Path    : Python-Programming-Language/07_Functions_in_Python/02_Function_Categories/02_User_defined_functions/5_Function_Definitions_and_Expressions/3_Coroutine_Functions/5_Task_Management.py
# Description : Coroutine Function / Synchronization
'''
Primitive	                        Purpose
asyncio.Lock	    Allows one task at a time to access a protected section
asyncio.Event	    Notifies waiting tasks that an event has occurred
asyncio.Semaphore	Limits the number of tasks accessing a resource
asyncio.Condition	Allows tasks to wait until a condition becomes true
asyncio.Queue	    Transfers data between asynchronous tasks
'''
# =============================================================================

def main():
#%% Simple example – Lock
    import asyncio

    counter = 0 # Shared variable accessed by multiple coroutines.
    lock = asyncio.Lock()   # Create an asynchronous Lock.

    async def increment():  # Define a coroutine to increment the counter.
        global counter   # Tell Python that we want to modify the global counter.

        async with lock:   # Acquire the lock before accessing shared data.
            counter += 1    # Increase the counter by 1.
            print("Counter:", counter)  # Display the updated counter.

    async def main():
        # Run three increment operations concurrently.
        await asyncio.gather(
            increment(),
            increment(),
            increment()
        )

        print("Final counter:", counter)    # Display the final counter value.

    asyncio.run(main())  # Execute the main coroutine.
    '''
    Code explanation:
        1. asyncio.Lock() creates a lock.
        2. async with lock acquires the lock.
        3. Only one task at a time can enter the protected section.
        4. The counter is updated safely.
        5. The lock is automatically released when the block exits.
    '''

#%% Advanced example – Semaphore
# Imagine downloading 10 files, but you want only 3 downloads to run at the same time.
# We can use asyncio.Semaphore(3).
    import asyncio

    # Create a Semaphore that allows 3 tasks at a time.
    semaphore = asyncio.Semaphore(3)


    # Define an asynchronous download operation.
    async def download(file_number):

        # Acquire one semaphore slot.
        async with semaphore:

            print(f"Downloading file {file_number}")

            # Simulate downloading a file.
            await asyncio.sleep(2)

            print(f"Completed file {file_number}")


    async def main():

        # Create download coroutines for 10 files.
        tasks = [
            download(i)
            for i in range(1, 11)
        ]

        # Run all downloads concurrently.
        # The semaphore limits active downloads to 3.
        await asyncio.gather(*tasks)

        print("All downloads completed")


    # Execute the main coroutine.
    asyncio.run(main())
    '''
    Code explanation:
    - Semaphore(3) creates three available slots.
    - Each download must acquire one slot.
    - Only three tasks can hold the semaphore simultaneously.
    - Other tasks wait until a slot becomes available.
    - When a download completes, its slot is released.
    - Another waiting download can start.
    '''

#%% Advanced example – Event
# An Event is useful when one coroutine must wait until another coroutine sends a signal.
    import asyncio

    event = asyncio.Event() # Create an Event object.

    # Define a coroutine that waits for a signal.
    async def waiter():
        print("Waiting for signal...")
        await event.wait()  # Suspend until another coroutine sets the event.
        # Continue execution after receiving the signal.
        print("Signal received! Continuing work.")

    # Define a coroutine that sends the signal.
    async def signaler():
        await asyncio.sleep(2)  # Wait for 2 seconds before sending the signal.
        print("Sending signal...")
        event.set() # Set the event and notify waiting coroutines.

    async def main():
        # Run waiter and signaler concurrently.
        await asyncio.gather(
            waiter(),
            signaler()
        )
    # Execute the main coroutine.
    asyncio.run(main())
    '''
    Code explanation:
        1. asyncio.Event() creates an event object.
        2. event.wait() suspends the waiter.
        3. event.set() signals that the event has occurred.
        4. The waiting coroutine resumes.
        5. The Event remains set until event.clear() is called. 
    '''

#%% Advanced example – Async Queue (Producer and Consumer)
# An asynchronous Queue is useful when one task produces data and another task processes it.
    import asyncio

    queue = asyncio.Queue() # Create an asynchronous Queue.
    # Producer creates and adds items to the Queue.
    async def producer():
        for i in range(1, 6):
            await asyncio.sleep(1)  # Simulate producing an item.
            await queue.put(i)  # Add the item to the Queue.
            print("Produced:", i)
        await queue.put(None)   # Add None to indicate that production is finished.
    
    async def consumer():   # Consumer receives and processes items.
        while True:
            item = await queue.get()   # Wait until an item is available.

            try:
                if item is None:    # None indicates that there are no more items.
                    print("Consumer finished")
                    return
                
                print("Consumed:", item)    # Process the received item.
                await asyncio.sleep(0.5)    # Simulate processing time.

            finally:
                queue.task_done()   # Mark the retrieved item as processed.

    async def main():
        # Start producer and consumer as separate Tasks.
        async with asyncio.TaskGroup() as group:
            group.create_task(producer())
            group.create_task(consumer())
    
    asyncio.run(main()) # Execute the main coroutine.
    '''
    Code explanation:
        - asyncio.Queue() creates a queue for asynchronous communication.
        - queue.put() adds an item.
        - queue.get() waits until an item becomes available.
        - The producer creates items.
        - The consumer processes items.
        - queue.task_done() marks an item as processed.
        - None is used as a special signal to stop the consumer.
    '''

if __name__ == "__main__":
    main()
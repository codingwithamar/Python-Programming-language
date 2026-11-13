# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 3_Async_Generators.py
# Path    : Python-Programming-Language/07_Functions_in_Python/02_Function_Categories/02_User_defined_functions/5_Function_Definitions_and_Expressions/3_Coroutine_Functions/3_Async_Generators.py
# Subject : User Defined Function
# Description : Coroutine Function / 3 Async Generators
# =============================================================================

def main():
#%% Basic Example
    import asyncio

    async def numbers():    # Define an asynchronous generator function.
        yield 1 # Produce the first value.
        yield 2 # Produce the second value.
        yield 3 # Produce the third value.

    async def main():
        async for number in numbers():  # Iterate over the asynchronous generator.
            print(number)   # Print each generated value.

    asyncio.run(main())   # Execute the main coroutine.
    '''
    Code explanation:
    1. async def with yield defines an asynchronous generator.
    2. Calling numbers() creates an asynchronous generator object.
    3. async for retrieves values one by one.
    4. The generator finishes after producing all values.
    '''

#%% Advanced example – Async data streaming
    import asyncio

    async def download_data():  # Define an asynchronous generator.
        for i in range(1, 6):   # Generate five data items.
            print(f"Downloading item {i}")
            await asyncio.sleep(1)  # Simulate an asynchronous network operation.
            yield f"Data {i}"   # Produce the downloaded item.

    async def main():
        async for data in download_data():  # Start receiving data from the generator.
            print("Received:", data)    # Process each item immediately.

    asyncio.run(main())   # Execute the main coroutine.
    '''
    Code explanation:
    - download_data() generates data items one by one.
    - await asyncio.sleep(1) simulates waiting for a network response.
    - yield sends each item to the caller.
    - async for receives and processes each item immediately.
    - The program does not need to collect all items before processing them.
    '''

if __name__ == "__main__":
    main()
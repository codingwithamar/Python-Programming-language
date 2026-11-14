# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 0_Asynchronous_Generator_Function_Definitions.py
# Path    : Python-Programming-Language/07_Functions_in_Python/02_Function_Categories/02_User_defined_functions/5_Function_Definitions_and_Expressions/2_Generator_Function_Definitions/0_Asynchronous_Generator_Function_Definitions.py
# Subject : User Defined Function
# Description : Function Definitions / Asynchronous Generator Function Definitions
# =============================================================================
def main():
    async def generate_numbers():
        yield 10
        yield 20
        yield 30

    async def main():
        async for number in generate_numbers():
            print(number)

    import asyncio
    asyncio.run(main())

    '''
    Code Explanation
        1. async def generate_numbers() defines an asynchronous generator function.
        2. Each yield produces one value.
        3. async for retrieves values from the asynchronous generator.
        4. After the last value, iteration stops.
    '''

#%% 4. Advanced Example – Asynchronous Data Generation
#Suppose we want to fetch data from a server one record at a time.
    import asyncio

    async def fetch_data():
        for number in range(1, 4):
            print(f"Fetching data {number}")
            await asyncio.sleep(1)  # Simulate asynchronous I/O operation
            # Produce one value
            yield {
                "id": number,
                "name": f"User {number}"
            }

    async def main():
        async for data in fetch_data():
            print("Received:", data)

    asyncio.run(main())
    '''
    Code Explanation
        - await asyncio.sleep(1) simulates waiting for an asynchronous operation.
        - yield returns the generated record to the caller.
        - The generator pauses at yield.
        - The next async for iteration resumes the generator.
        - This continues until all records are generated.
    '''

if __name__ == "__main__":
    main()
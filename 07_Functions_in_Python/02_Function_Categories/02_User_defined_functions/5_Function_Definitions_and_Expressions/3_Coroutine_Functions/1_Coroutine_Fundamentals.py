# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 1_Coroutine_Fundamentals.py
# Path    : Python-Programming-Language/07_Functions_in_Python/02_Function_Categories/02_User_defined_functions/5_Function_Definitions_and_Expressions/3_Coroutine_Functions/1_Coroutine_Fundamentals.py
# Subject : User Defined Functions
# Description : Coroutine Generators/Coroutine Fundamentals (async def,greet(),asyncio.run(),await asyncio.sleep())
# =============================================================================

def main():
#%% Basic Example
    import asyncio

    # Define a coroutine function using async def.
    async def greet():

        print("Welcome")    #Welcome

        # Pause this coroutine for 2 seconds.
        # It does not block the entire event loop.
        await asyncio.sleep(2)

        # Execution resumes after 2 seconds.
        print("Jai Ganesh...")  #Jai Ganesh...

    # Create an event loop and execute the coroutine.
    asyncio.run(greet())

#%% Advanced Examples : Coroutine with arguments, return value and exception
    import asyncio

    # Define a coroutine that accepts two arguments.
    async def calculate(a, b):

        print("Calculation started")

        # Simulate an asynchronous operation.
        await asyncio.sleep(2)

        # Perform calculation after waiting.
        result = a + b

        print("Calculation completed")

        # Return the calculated value.
        return result

    # Main coroutine.
    async def main():
        try:
            # Execute calculate() and wait for its result.
            result = await calculate(10, 20)

            # Display the returned value.
            print("Result:", result)

        except Exception as error:

            # Handle an exception if one occurs.
            print("Error:", error)

    # Start the main coroutine.
    asyncio.run(main())

if __name__ == "__main__":
    main()
# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : lambda_Function_Expression.py
# Path    : Python-Programming-Language/07_Functions_in_Python/02_Function_Categories/02_User_defined_functions/5_Function_Definitions_and_Expressions/4_Lambda_Function_Expressions/lambda_Function_Expression.py
# Subject : User Defined Function
# Description : Lambda Function Expression with filter(),map(),reduce()
# =============================================================================

def main():
#%% Concept of Lambda
    # Single argument
    square = lambda x: x * x
    print(square(5))    # Output: 25

    # Multiple Arguments
    add = lambda a, b: a + b
    print(add(10, 20))  # Output: 30


    # Make Lambda Function
    square = lambda x: x * x
    print(square(5))

    # filter() – Values filtering
    numbers = [1, 2, 3, 4, 5, 6]
    result = filter(lambda x: x % 2 == 0, numbers)
    print(list(result))

    # filter() select those condition true values

    # map() – every value transform
    numbers = [1, 2, 3, 4, 5, 6]
    result = map(lambda x: x * x, numbers)
    print(list(result))

    # reduce() – combined all values and produce result
    from functools import reduce

    numbers = [1, 2, 3, 4, 5, 6]
    result = reduce(lambda x, y: x + y, numbers)
    print(result)

#%% Basic Example
    from functools import reduce

    numbers = [1, 2, 3, 4, 5, 6]

    result = reduce(
        lambda x, y: x + y,
        map(
            lambda x: x * x,
            filter(
                lambda x: x % 2 == 0,
                numbers
            )
        )
    )

    print(result)

if __name__ == "__main__":
    main()
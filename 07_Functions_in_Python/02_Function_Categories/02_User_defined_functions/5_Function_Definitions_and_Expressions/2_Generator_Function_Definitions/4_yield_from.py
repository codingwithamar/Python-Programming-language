# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 4_yield_from.py
# Path    : Python-Programming-Language/07_Functions_in_Python/02_Function_Categories/02_User_defined_functions/5_Function_Definitions_and_Expressions/2_Generator_Function_Definitions/4_yield_from.py
# Subject : User Defined Function
# Description : Function Definitions/Generator Function Definition/yield from
# =============================================================================

def main():
#%% Basic Example
    # from Particular format list
    def numbers():
        yield from [1, 3, 5, 6]

    for num in numbers():
        print(num)      #1 3 5 6

    print()

    # From Separated list
    def both():
        yield from [1, 2]
        yield from [3, 4]

    print(list(both()))   # [1, 2, 3, 4]

    print()

    # yield from with Another Generator
    def generator_one():
        yield 10
        yield 20

    def generator_two():
        yield from generator_one()
        yield 30
        yield 40

    for num in generator_two():
        print(num)      # 10 20 30 40


    print()

#%% Advanced Example
    def flatten(items):
        for item in items:
            if isinstance(item, list):
                yield from flatten(item)
            else:
                yield item
    
    print(list(flatten([1, [2, [3, 4]], 5])))   # [1, 2, 3, 4, 5]

    def read_lines(lines):
        for line in lines:
            yield line
        return len(lines)

    def wrapper(lines):
        total = yield from read_lines(lines)    # total gets the return value
        print("lines read:", total)

    list(wrapper(["x", "y"]))                   # prints: lines read: 2

if __name__ == "__main__":
    main()
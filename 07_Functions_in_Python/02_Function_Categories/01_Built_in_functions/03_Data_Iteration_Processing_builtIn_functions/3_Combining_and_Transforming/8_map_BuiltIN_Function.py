# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 8_map_BuiltIN_Function.py
# Path    : Python-Programming-Language/07_Functions_in_Python/02_Function_Categories/01_Built_in_functions/03_Data_Iteration_Processing_builtIn_functions/3_Combining_and_Transforming/8_map_BuiltIN_Function.py
# Subject : Built-in functions in python
# Description :map() - Applies a function to every item of an iterable.
# =============================================================================

def main():
#%% Example 1: Without Lambda (using def):
    def CheckEven(No):
        return (No % 2 == 0)

    Data = [13,12,8,10,11,20]
    print("Input Data is : ", Data)

    #FData = filter(CheckEven,Data) #Iterable <- filter(Iterable,Function)
    FData = list(filter(CheckEven,Data))
    print("Data after filter : ",FData)

    '''
    OUTPUT :
    Input Data is :  [13, 12, 8, 10, 11, 20]
    Data after filter :  [12, 8, 10, 20]
    '''

#%% Example 2: With Lambda
    CheckEven = lambda No : (No % 2 == 0)

    def main():
        Data = [13,12,8,10,11,20]
        print("Input Data is : ", Data)
        FData = list(filter(CheckEven,Data))
        print("Data after filter : ",FData)

    '''
    OUTPUT :
    Input Data is :  [13, 12, 8, 10, 11, 20]
    Data after filter :  [12, 8, 10, 20]
    '''









#%% Another some examples
    print("Synatax : map(function, iterable, *more_iterables)")
    numbers = ["1", "2", "3"]
    print(list(map(int, numbers)))              # [1, 2, 3]
    print(list(map(str.upper, ["a", "b"])))     # ['A', 'B']
    print(list(map(lambda x: x * x, [1, 2, 3])))  # [1, 4, 9]

    # 1. Two iterables: the function gets one item from each
    print(list(map(lambda a, b: a + b, [1, 2, 3], [10, 20, 30])))   # [11, 22, 33]

    # 2. map is lazy and single-use
    m = map(str.upper, ["a", "b"])
    print(m)            # <map object at 0x...>  -> not the values
    print(list(m))      # ['A', 'B']
    print(list(m))      # []  -> already used up

    # 3. Real use: clean a list of file names
    raw = ["  report.CSV ", "DATA.json  "]
    clean = list(map(lambda s: s.strip().lower(), raw))
    print(clean)        # ['report.csv', 'data.json']

    # 4. Same result with a list comprehension
    clean2 = [s.strip().lower() for s in raw]

if __name__ == "__main__":
    main()
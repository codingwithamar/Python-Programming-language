# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : reduce_functools_Function.py
# Path    : Python-Programming-Language/07_Functions_in_Python/02_Function_Categories/01_Built_in_functions/03_Data_Iteration_Processing_builtIn_functions/3_Combining_and_Transforming/reduce_functools_Function.py
# Subject : Functools Function
# Description : Basically filter(),map(),reduce() both three function use together
# =============================================================================

def main():
#%% Example 1: Without Lambda (using def):
    from functools import reduce

    def CheckEven(No):
        return (No % 2 == 0)

    def Increment(No):
        return No+1

    def Addition(No1, No2):
        return No1 + No2

    Data = [13,12,8,10,11,20]
    print("Input Data is : ", Data)
    FData = list(filter(CheckEven,Data))	   #12, 8, 10, 20
    MData = list(map(Increment,FData))      #13, 9, 11, 21
    RData = reduce(Addition, MData)         # 54
    print("Data after Reduce : ",RData)

#%% Example 2: With Lambda
    from functools import reduce

    CheckEven = lambda No : (No % 2 == 0)
    Increment = lambda No : No+1
    Addition = lambda No1, No2 : No1 + No2

    Data = [13,12,8,10,11,20]
    print("Input Data is : ", Data)
    FData = list(filter(CheckEven,Data))    #12, 8, 10, 20
    MData = list(map(Increment,FData))      #13, 9, 11, 21
    RData = reduce(Addition, MData)         # 54
    print("Data after Reduce : ",RData)

#%% Example 3 : 
    from functools import reduce

    def Add(iValue1,iValue2):
        return iValue1+iValue2

    Values = []
    while True:
        data = input("Enter your numbers : ")
        if data == "":
            break

        Values.append(int(data))

    Addition = reduce(Add,Values)
    print("Addition of all values : ",Addition)

if __name__ == "__main__":
    main()
from functools import reduce

def CheckEven(No):
    return (No % 2 == 0)

def Increment(No):
    return No+1

def Addition(No1, No2):
    return No1 + No2

def main():
    Data = [13,12,8,10,11,20]

    print("Input Data is : ", Data)

    FData = list(filter(CheckEven,Data))
    MData = list(map(Increment,FData))      #13, 9, 11, 21]
    RData = reduce(Addition, MData)         # 54

    print("Data after Reduce : ",RData)

if __name__ == "__main__":
    main()
    
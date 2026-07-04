from filter_map_reduce_library import filterX, mapX, reduceX

CheckEven = lambda No : (No % 2 == 0)

Increment = lambda No : No+1

Addition = lambda No1, No2 : No1 + No2

def main():
    Data = [13,12,8,10,11,20]

    print("Input Data is : ", Data)

    FData = list(filterX(CheckEven,Data))    #12, 8, 10, 20
    print("Data after filterX : ",FData)

    MData = list(mapX(Increment,FData))      #13, 9, 11, 21
    print("Data after mapX : ",MData)

    RData = reduceX(Addition, MData)         # 54
    print("Data after ReduceX : ",RData)

if __name__ == "__main__":
    main()
    
CheckEven = lambda No : (No % 2 == 0)

Increment = lambda No : No+1

def main():
    Data = [13,12,8,10,11,20]

    print("Input Data is : ", Data)

    FData = list(filter(CheckEven,Data))    #filter
    MData = list(map(Increment,FData))      #map

    print("Data after Map : ",MData)

if __name__ == "__main__":
    main()
    
# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : map() Function.py
# Path    : Python-Programming-Language\Function in Python\map() Function.py
# Subject : Function in Python
# Description : map() Function
# =============================================================================

def main():
    numbers = ["10", "20", "30"]    #Each elements is String

    num = map(int, numbers)
    print(numbers)             #['10', '20', '30']   -String

    numlist = list(map(int, numbers))
    print(numlist)             #[10, 20, 30]      - int

    names = ["python", "java", "c"]
    result = list(map(str.upper, names))
    print(result)               #['PYTHON', 'JAVA', 'C']    -string

    numbers = ["10", "20", "30"]
    result = []
    for i in numbers:
        result.append(int(i))
    print(result)

    # Read two integers
    a, b = map(int, input().split())

    # Read a list of integers
    numbers = list(map(int, input().split()))

    # Read comma-separated values
    items = input().split(",")
    
    # Convert names to uppercase
    upper_names = list(map(str.upper, input().split()))

if __name__ == "__main__":
    main()
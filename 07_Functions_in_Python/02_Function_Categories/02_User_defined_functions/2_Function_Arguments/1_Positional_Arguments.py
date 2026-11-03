# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : Positional_Arguments.py
# Path    : Python-Programming-Language/07_Functions_in_Python/00_Function_Arguments/Positional_Arguments.py
# Subject : Function arguments in python
# Description : Positional Arguments/Required argumnets
# =============================================================================

def main():
#%% Basic Concept
    def Batches1(name, fees):
        print("Batch name is", name)
        print("Fees are", fees)
    
    Batches1("Python", 28000)

#%% Basic Example
    def introduce(name, age):
        print(f"{name} is {age} years old")

    introduce("Amar", 25)       # Amar is 25 years old
    introduce(25, "Amar")       # 25 is Amar years old  -> wrong order, wrong meaning

#%% Advanced Examples
    def divide(numerator, denominator):
        return numerator / denominator

    print(divide(10, 2))        # 5.0
    print(divide(2, 10))        # 0.2  -> a different answer, because the order changed

    # Wrong number of arguments
    try:
        divide(10)
    except TypeError as error:
        print(error)    # divide() missing 1 required positional argument: 'denominator'

    try:
        divide(10, 2, 5)
    except TypeError as error:
        print(error)    # divide() takes 2 positional arguments but 3 were given

if __name__ == "__main__":
    main()


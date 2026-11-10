# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 1_Generator_Function_Concept.py
# Path    : Python-Programming-Language/07_Functions_in_Python/02_Function_Categories/02_User_defined_functions/5_Function_Definitions_and_Expressions/2_Generator_Function_Definitions/1_Generator_Function_Concept.py
# Subject : User Defined Function
# Description : Function Definitions/Generator Function Definition/Concept
# =============================================================================
import sys

def main():
#%% Why Use Generator Function
    # If we want print 10 numbers serially then we use Function using loop/range
    def whileCreator():
        #Using While Loop
        list = []
        i = 1
        while i<10:
            list.append(i)
            i += 1
        return list
    
    print(whileCreator())
    whileSize = sys.getsizeof(list)
    print("while list size is : ",whileSize,"Bytes")

    print("")
    #Using range Function
    RangeNumbers = list(range(1,10))
    print(RangeNumbers)
    rangeSize = sys.getsizeof(list)
    print("range list size is : ",rangeSize,"Bytes")

    '''
    OUTPUT : 

    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    while list size is :  416 Bytes

    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    range list size is :  416 Bytes
    '''

    print()
    # We see print all Numbers (List) at time in one called...
    # and if we want single number or perticular number serially when we called...
    # both functions not hold and remembered serial so python introduced Generator function - yield

    def yieldCreater():
        i = 1
        while i < 10:
            yield i     #it commit point, it hold the value serial
            i += 1
    print(yieldCreater())   
    #here Object Created - <generator object main.<locals>.yieldCreater at 0x752005cf2980>

    X = yieldCreater()
    print(next(X))  #1st print
    print(next(X))  #2nd print
    print(next(X))  #3rd print
    # We see it print serial by call, If we want print all list
    print(list(X))

    '''
    OUTPUT : 
    <generator object main.<locals>.yieldCreater at 0x793190746980>
    1
    2
    3
    [4, 5, 6, 7, 8, 9]
    '''

if __name__ == "__main__":
    main()

# %%

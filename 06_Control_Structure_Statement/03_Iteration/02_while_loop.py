# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 02_while_loop.py
# Path    : Python-Programming-Language/06_Control_Structure_Statement/03_Iteration/02_while_loop.py
# Subject : Control Structure Statements - Iteration/loops
# Description : while loop - Used when the number of iterations is not known before hand. 
# =============================================================================

def main():
    #________________________________________________________________________________
    #						               'Syntax'
    """
    while condition:
        code block (must be indented)
    """
    #Example 1 :
    count = 1                 # 1. starting value

    while count <= 5:         # 2. condition
        print(count)
        count += 1            # 3. update
    #________________________________________________________________________________

    #________________________________________________________________________________
    #						'Nested while Loop'
    i = 1
    j = 1
    while i<= 3:
        i = 1
        while j <= 3:
            print(i*j,end="\t")
            j += 1
        print()
        i += 1

        '''
        Output :
        1	2	3
        2	4	6
        3	6	9
        '''
    #________________________________________________________________________________
        print()
    #________________________________________________________________________________
    #						'else in while loop'
        i = 1

        while i <= 3:
            print(i)
            i += 1
        else:
            print("Completed")
    #________________________________________________________________________________
if __name__ == "__main__":
    main()
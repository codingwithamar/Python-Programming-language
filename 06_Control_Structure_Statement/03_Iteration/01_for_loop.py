# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 01_for_loop.py
# Path    : Python-Programming-Language/06_Control_Structure_Statement/03_Iteration/01_for_loop.py
# Subject : Control Structure Statements - Iteration
# Description : Iteration/Loops - for loop
# =============================================================================

def main():
#----------------------------------------------------------------------------------------------------
#										'for loop/iteration'
#----------------------------------------------------------------------------------------------------
#________________________________________________________________________________
#						            'Syntax'
    print("Syntax","-" * 30)
    print("""
    for variable in iterable:
    statement
    """)

#   for       → loop सुरू करतो
#   item      → प्रत्येक element temporary variable मध्ये घेतो
#   in        → iterable मधून value घेतो
#   [1,2,3]   → iterable
#   :         → loop body सुरू
#   print()   → प्रत्येक iteration मध्ये execute
#________________________________________________________________________________
#________________________________________________________________________________
#						'for loop/iterataion'

    #range
    print("\nRange","-" * 30)
    
    for i in range(5):  #start with 0
        print(i)        #0 1 2 3 4

    print()

    for i in range(2, 10, 2):   #range(start, stop, step)
        print(i)        #2 4 6 8

    print()

    for i in range(10, 0, -1):  #reverse loop
        print(i)        #10 9 8 7 6 5 4 3 2 1

    #List
    print("\nList","-" * 30)

    numbers = [10, 20, 30, 40]
    for x in numbers:
        print(x)        # 10 20 30 40

    #Tuple
    print("\nTuple","-" * 30)

    data = (10, 20, 30)
    for x in data:
        print(x)    # 10 20 30

    #String
    print("\nstring","-" * 30)

    name = "Python"
    for char in name:
        print(char)

    #OUTPUT :
    """ P
        y
        t
        h
        o
        n
    """
    
    #Set
    print("\nSet","-" * 30)
    
    numbers = {10, 20, 30}
    for x in numbers:
        print(x)

    #Dictionary    
    print("\nDictionary","-" * 30)

    student = {
        "name": "Amar",
        "age": 25,
        "marks": 81
    }

    '''if want only Values'''
    for value in student.values():      #values()
        print(value)

    print()

    '''if want only Keys'''
    for key in student.keys():          #keys()
        print(key)

    print()

    '''if want key and values'''
    for key, value in student.items():      #items()
        print(key, value)

    #enumerate() — index + value
    print("\nenumerate() — index + value","-" * 30)

    names = ["Amar", "Rahul", "Suresh"]
    for index,name in enumerate(names):
        print(index,name)

    #zip - one or more iterable
    print("\nZip","-" * 30)
    
    names = ["Amar"
            , "Rahul", "Suresh"]
    marks = [81, 75, 90]

    for name, mark in zip(names, marks):
        print(name, mark)
#________________________________________________________________________________

#________________________________________________________________________________
#						'Nested for loop'
    print("\nNested loop","-" * 50)

    for i in range(3):
        for j in range(3):
            print(i, j)
    '''
    flow :
    i = 0
        ├── j = 0
        ├── j = 1
        └── j = 2

    i = 1
        ├── j = 0
        ├── j = 1
        └── j = 2

    i = 2
        ├── j = 0
        ├── j = 1
        └── j = 2
    '''

    print()

    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    for row in matrix:
        for value in row:
            print(value)    #1 2 3 4 5 6 7 8 9
#________________________________________________________________________________
    
if __name__ == "__main__":
    main()
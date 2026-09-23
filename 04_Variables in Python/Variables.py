# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : Variables.py
# Path    : Python-Programming-Language/03_Variables in Python/Variables.py
# Subject : Varibales in Python
# Description : Complete concept of Varibles
# =============================================================================

def main():
    #----------------------------------------------------------------------------------------------------
    #										'Varibales in Python'
    #----------------------------------------------------------------------------------------------------
    #________________________________________________________________________________
    #						'Creation and updation'
    X = 10  #Create variable
    Y = 15  #No need to declaired Data type we can store any type of data in variables
    print(X + Y)  #25  #No need to declaration variables in python

    #Variable value can change  or overwrite it
    Z = 1.5
    X = X + Z

    print(X + Z)    # 25 + 1.5 = 26.5

    name = "Amar"
    age = 25
    salary = 50000.50
    #________________________________________________________________________________
    
    #________________________________________________________________________________
    #						'Variable Naming Conventions'
    #A Variable name containe only letters,numbers and Underscores. Variable is case sensitive
    #An Varibale name can start witha letter or underscore but not with letter and Space

    name = "Amar"           #Valid
    age = 25                #Valid
    Student_name = "Amar"   #Valid
    _private = 10           #Valid
    marks2 = 90             #Valid

    #    2marks = 90             # Invalid❌
    #    student-name = 10       # Invalid❌
    #    student name = 10       # Invalid❌
    #________________________________________________________________________________
    
    #________________________________________________________________________________
    #						'Chain Assignment in Variable'

    X = Y = Z = 10
    print(X + Y + Z)    #30    
    #________________________________________________________________________________
    
    #________________________________________________________________________________
    #						'Scope of Variables'
    
    var_x = 100       # Global

    def test():
        var_x = 200   # Local
        print(var_x)
        print(id(var_x))    #11373200

    test()          #200
    print(var_x)    #100

    print(id(var_x))    #11376400
    #________________________________________________________________________________
    
    #________________________________________________________________________________
    #						'Single object and multiple things'
    # ----------------------------------- is vs == --------------------------------- 
    # Multiple variable name can point to single object 
    x = [10, 20]
    y = x

    print(x == y)   # True
    print(x is y)   # True

    #--------------------Multiple assignment in one object---------------------------

    x = y = z = 100         #Valid
    x, y, z = 10, 20, 30    #Valid

    a = 10
    b = 20

    a, b = b, a     #Valid Swapping

    #------------------------------ Assignment ≠ Copy---------------------------------
    p = [1, 2, 3, 4, 5, 6, 7]
    q = p

    #here not created new copy q , both pointing same object
    p.append(30)
    print(q)        #[1, 2, 3, 4, 5, 6, 7, 30]

    # if we want copy of same variable then we use copy() function
    p = q.copy()
    p.append(40)
    
    print(p)    #[1, 2, 3, 4, 5, 6, 7, 30, 40]
    print(q)    #[1, 2, 3, 4, 5, 6, 7, 30]
    #________________________________________________________________________________
    
    #________________________________________________________________________________
    #						'type Anotation in python'
    age: int = 25           #valid
    name: str = "Amar"      #valid
    salary: float = 50000.0 #Valid
    #________________________________________________________________________________

    #________________________________________________________________________________
    #						'Varibales name conventions'
    #   1. Camel case convention :
    varibleNameConvention = 1

    #   2. Pascal case convention :
    VariableNameConvention = 2

    #   3. Snake case convention : 
    variable_name_convention = 3
    #________________________________________________________________________________
        

if __name__ == "__main__":
    main()


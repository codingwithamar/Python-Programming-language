# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 3_issubclass_builtIn_function.py
# Path    : Python-Programming-Language/07_Functions_in_Python/02_Function_Ctaegories/01_Built_in_functions/02_Object_Type_Handling_builtIn_functions/3_issubclass_builtIn_function.py
# Subject : Inspection Built-In Functions in Python
# Description : issubclass() : Checks if a class is a subclass of another class. Works on classes themselves, not instances.
# =============================================================================

def main():
#________________________________________________________________________________
#						'Defination and Syntax'
    print("Definition : Checks if a class is a subclass of another class. Works on classes themselves, not instances.")
    print("Syntax : issubclass(class, classinfo)")
#________________________________________________________________________________

    class Animal:       #Parent class
        pass

    class Dog(Animal):  #Child class
        pass

    print(issubclass(Dog, Animal))     # True
    print(issubclass(Animal, Dog))     # False -> relationship only works one direction
    print(issubclass(Dog, Dog))        # True -> a class is considered a subclass of itself

if __name__ == "__main__":
    main()
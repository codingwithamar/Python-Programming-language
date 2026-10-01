# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : Placeholder_Variable.py
# Path    : Python-Programming-Language/03_Variables in Python/Placeholder_Variable.py
# Subject : Placeholder Variables in Python
# Description : _  = "I received this value, but I don't need it."
# =============================================================================

def main():
#----------------------------------------------------------------------------------------------------
#										'Placeholder Variable'
#----------------------------------------------------------------------------------------------------
#________________________________________________________________________________
#						'Placeholder in Loops'
    #Normal variable vs placeholder variable
    for i in range(3):  #Normal Way
        print(i)        #0,1,2

    for _ in range(3):  #This value exists, but I don't need to use it.
        print("Hello")

        '''
        OUTPUT :
                Hello
                Hello
                Hello
        '''

        """In Above Example"""
        ''' i → value is needed
            _ → value is intentionally ignored
        '''
#________________________________________________________________________________

#________________________________________________________________________________
#						'In Unpacking'
    Data1 = ("Amar", 25, "Python")   #Packing

    name, _, language = Data1       #Unpacking
    print(name, _, language)        #If we dont know column name but data needed
#________________________________________________________________________________


if __name__ == "__main__":
    main()
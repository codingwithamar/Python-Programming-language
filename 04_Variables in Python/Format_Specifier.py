# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : Format_Specifier.py
# Path    : Python-Programming-Language/04_Variables in Python/Format_Specifier.py
# Subject : Format Specifier
# Description : a special part of a format string that tells Python how to 
#               represent a value in the output.
# =============================================================================

def main():
    #----------------------------------------------------------------------------------------------------
    #										'Format Specifier'
    #----------------------------------------------------------------------------------------------------
    
    name = "Amar"
    age = 25
    marks = 81.30

    print(f"Name: {name}")  #Amar
    print(f"Age: {age}")    #25

    price = 1234.5678

    print(f"{price:.2f}")   #1234.57
#_______________________________________________________________________________

    name = "Python"
    age = 25
    pi = 3.14159

    print("Name: %s" %name)    #Name: Python    #String
    print("Age: %d" %age)      #Age: 25         #integer
    print("PI: %.2f" %pi)      #PI: 3.14        #floating point
    print("Hex: %x" %age)      #Hex: 19         #hexadecimal-point
    print("Percent:100%%")     #Percent: 100%   #literal

#________________________________________________________________________________
#						'Decimal specifier'

    #   integer
    age = 25
    print("Age = %d" % age) # Age = 25
    #print("Age = %i", age)  # Age = 25 /NOT WORK YET PYTHON3

    #   OctaDecimal
    x = 10
    print("%o" % x)         # 12    /Decimal 10 , Octal 12

    #   HexaDecimal
    x = 255
    print("%x" % x)         #ff     /Lowecase
    print("%X" % 255)       #FF     /Uppercase
#________________________________________________________________________________

#________________________________________________________________________________
#						'Floating-point Specifiers'

    #   %.2f
    price = 231.24235
    print("Price = %.2f" %price)    #231.24

    #   %e
    x = 1234.567
    print("%.2e" % x)               #1.23e+03   /Scientific Notation lower case

    #   %E
    print("%.2E" % x)               #1.23E+03   Scientific Notation Upper case


    print("%g" % x)                 #123.456

    print("%G" % x)                 #123.456
#________________________________________________________________________________

#________________________________________________________________________________
#						'Character & String Specifier'

    print("%c" %65)                 #A          /Unicode code point 65 = A.    
    print("%s" % name)              #Python     /str()
    print("%r" % name)              #'Python'   /repre()
    print(ord('A'))                 #65         /Get Character > ASCII
    print(chr(65))                  #A          /Get ASCII > Character
#________________________________________________________________________________

#________________________________________________________________________________
#						'Multiple Specifier'
    print("Name: %s, Age: %d, Marks: %.1f" % (name, age, marks))
    # Name: Amar, Age: 25, Marks: 81.3
#________________________________________________________________________________

#________________________________________________________________________________
#						'Width,Padding & Alignment'
    print("%10d" % 25)      #          25       /Width
    print("%05d" % 25)      # 00025     /Zero Paddings
    print("% d" % 25)       
    print("%+d" % 26)
    print("%+d" % -27)
#________________________________________________________________________________


if __name__ == "__main__":
    main()

# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 1_Input_builtIn_function.py
# Path    : Python-Programming-Language/07_Functions_in_Python/02_Function_Ctaegories/01_Built_in_functions/01_Input_Output_builtIn_functions/1_Input_builtIn_function.py
# Subject : Built-In Input-Output Functions
# Description : input() - Reads a line of text typed by the user from the keyboard, Always returns a string, no matter what is typed.
# =============================================================================

def main():
    # %%________________________________________________________________________________
    #						    'Synatx & Defination'
    print("Defination -> Reads a line of text typed by the user from the keyboard, Always returns a string, no matter what is typed.")
    print("Syntax -> input(prompt='')")
    #________________________________________________________________________________
    print("_"*150)
# %%________________________________________________________________________________
#						        'Basic Code of input()'
    name = input("Enter Your Name : ")
    print("Hello",name)
#________________________________________________________________________________
    print("_"*150)
# %%________________________________________________________________________________
#						'Advanced Example of input()'
    # input() always returns a string -> must convert manually
    age_input = input("Enter your age : ")

    while True:
        if age_input.isdigit():
            age_in_int = int(age_input)     #Typecasting string to integer
            break
        else:
            print("That is not a valid number. Try again.")
            age_input = input("Enter your age : ")

    print("Next year you will be", age_in_int + 1, "Year completed")

    Birth_Year = 2026 - age_in_int

    print("Your Birth Year is", Birth_Year)
#________________________________________________________________________________

if __name__ == "__main__":
    main()
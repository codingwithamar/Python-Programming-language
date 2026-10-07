# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 1_Print_builtIn_function.py
# Path    : Python-Programming-Language/07_Functions_in_Python/02_Function_Ctaegories/01_Built_in_functions/01_Input_Output_builtIn_functions/1_Print_builtIn_function.py
# Subject : Built-In Input-Output Functions
# Description : print() : Outputs text or values to the screen (standard output).
# =============================================================================

def main():
    #________________________________________________________________________________
    #						'Syntax & Definition'
    print("Definition : Outputs text or values to the screen (standard output).")
    print('''Syntax 1 : print(*objects, sep=' ', end='\'n', file=sys.stdout, flush=False) OR''')
    print('Syntax 2 : <Text> OR')
    print("Syntax 3 : <Text> ,<VariableName>    ")
    #________________________________________________________________________________
    #________________________________________________________________________________
    #						'Basic Example of print()'
    print("Hello, AMAR")
    print("Amar", 25, "Pune")          # multiple values, space-separated by default
    #________________________________________________________________________________
    #________________________________________________________________________________
    #						'Anather way of use print()'
    # sep -> changes the separator between values
    print("2026", "10", "07", sep="-")              # 2026-10-07

    # end -> changes what is printed after, instead of a newline
    print("Loading", end="...")
    print("Done")                                     # Loading...Done
    #________________________________________________________________________________
    
if __name__ == "__main__":
    main()
# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 4_Breakpoint_builtIn_function.py
# Path    : Python-Programming-Language/07_Functions_in_Python/02_Function_Ctaegories/01_Built_in_functions/01_Input_Output_builtIn_functions/4_Breakpoint_builtIn_function.py
# Subject : Built-In function
# Description : breakpoint() : Program चालू असताना execution एखाद्या specific line वर थांबवून debugger मध्ये program ची current state तपासणे.
# =============================================================================

def main():
    #________________________________________________________________________________
    #						'Definition & Instruction'
    print("Definition : Starts Python's interactive debugger (pdb) at the exact line where it is called, " \
    "pausing the program so you can inspect variables step by step. Added in Python 3.7.")
    print("Syntax : breakpoint()")
    print("""
    Instructions :
    n	next line
    c	continue running until the next breakpoint or end
    p   variable_name	print a variable's current value
    q	quit the debugger
    l	show the code around the current line    
    h   help
    """)
    #________________________________________________________________________________
    
    def calculate_total(price, quantity):
        subtotal = price * quantity
        breakpoint()          # program pauses here
        tax = subtotal * 0.1
        print(tax)
        breakpoint()          # program pauses here
        total = subtotal + tax
        print(total)
        breakpoint()          # program pauses here
        return total

    calculate_total(100, 3)

if __name__ == "__main__":
    main()
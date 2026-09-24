# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : Sequence.py
# Path    : Python-Programming-Language/06_Control_Statement/01_Sequence/Sequence.py
# Subject : Control Structures in python - 1. Sequence
# Description : Sequence means code runs one line after another, in the exact order it 
# is written. This is the default behavior of every program. No special keyword is needed.
# =============================================================================

def main():
    #----------------------------------------------------------------------------------------------------
    #										'Sequence'
    #----------------------------------------------------------------------------------------------------
    #________________________________________________________________________________
    #						'Basic Example of Sequence'
    print("Step 1: Start")
    x = 5
    y = 10
    total = x + y
    print("Step 2: Total is", total)
    #________________________________________________________________________________
    print()
    #________________________________________________________________________________
    #						'Example of Sequnece using Function'
        
    def process_order(item, price, quantity):
        print("Step 1: Received order for", item)
        subtotal = price * quantity
        print("Step 2: Subtotal calculated:", subtotal)
        tax = subtotal * 0.1
        print("Step 3: Tax calculated:", tax)
        final_total = subtotal + tax
        print("Step 4: Final total is", final_total)
        return final_total

    process_order("Laptop", 50000, 1)
    #________________________________________________________________________________


if __name__ == "__main__":
    main()
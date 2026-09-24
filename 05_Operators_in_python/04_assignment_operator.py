# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 04_assignment_operator.py
# Path    : Python-Programming-Language/05_Operators_in_python/04_assignment_operator.py
# Subject : Assignment Operator
# Description : ssign a value to a variable.(= += -= *= /= //= %= **=)
# =============================================================================

def main():
    #----------------------------------------------------------------------------------------------------
    #										'Assignment Operators'
    #----------------------------------------------------------------------------------------------------
    #________________________________________________________________________________
    #						'Normal Assignemnt( = )'
    x = 10
    print(x)            # 10

    # Multiple assignment and unpacking
    a, b, c = 1, 2, 3
    print(a, b, c)      #1, 2, 3

    # Chained assignment
    x = y = z = 9
    print(x, y, z)   # 9 9 9

    # Swapping values without a temp variable
    a, b = 5, 10
    a, b = b, a
    print(a, b)   # 10 5
    #________________________________________________________________________________
    
    #________________________________________________________________________________
    #						'Add and Assign ( += )'
    x = 10
    x += 5     # x = x + 5
    print(x)   # 15

    # Works on strings (concatenation) and lists (extend in place)
    name = "Ama"
    name += "r"
    print(name)     # Amar

    nums = [1, 2, 3]
    nums += [4, 5]
    print(nums)     # [1, 2, 3, 4, 5]
    #________________________________________________________________________________
    
    #________________________________________________________________________________
    #						'Substract and assign( -= )'
    x = 10
    x -= 5
    print(x)        # 5

    ## Tracking inventory countdown in a loop
    stock = 100
    orders = [10, 30, 15, 20]
    for order in orders:
        stock -= order
    print(stock)        # 25
    #________________________________________________________________________________
    
    #________________________________________________________________________________
    #						'Multiply and Assign( *= )'
    x = 10
    x *= 5
    print(x)        # 50

    # String and list repetition
    line = "Amar "
    line *= 3
    print(line)     # Amar Amar Amar 

    pattern = [0, 1]
    pattern *= 4
    print(pattern)      # [0, 1, 0, 1, 0, 1, 0, 1]
    #________________________________________________________________________________
    
    #________________________________________________________________________________
    #						'Divide and Assign( /= )'
    x = 10
    x /= 5
    print(x)        # 2.0

    # Normalizing a list of values to a 0-1 scale
    scores = [20, 40, 60, 80, 100]
    max_score = max(scores)     # 100
    normalized = []
    for s in scores:
        s /= max_score
        normalized.append(s)
    print(normalized)       # [0.2, 0.4, 0.6, 0.8, 1.0]
    #________________________________________________________________________________
    
    #________________________________________________________________________________
    #						'Floor Divide and Assign( //= )'
    x = 10
    x //= 3
    print(x)   # 3

    # Converting seconds into minutes (discarding remainder)
    total_seconds = 500
    minutes = total_seconds
    minutes //= 60
    print(f"Total {minutes} minutes")      # Total 8 minutes
    #________________________________________________________________________________
    
    #________________________________________________________________________________
    #						'Modulo and Assign( %= )'
    x = 10
    x %= 3
    print(x)        # 1

    # Wrapping an index around a fixed-size list (circular buffer)
    size = 5
    index = 0
    for _ in range(12):
        index += 1
        index %= size
    print(index)        # 2

    # Checking even/odd inside a running total
    total = 17
    total %= 2
    print(total)   # 1  -> odd
    #________________________________________________________________________________
    
    #________________________________________________________________________________
    #						'Power and Assign( **= )'
    x = 2
    x **= 3
    print(x)   # 8

    # Compounding growth over time (like interest or population growth)
    value = 1000
    rate = 1.05
    years = 3
    for _ in range(years):
        value **= 1        # placeholder to show pattern; real compounding uses *=
    value = 1000
    value *= rate ** years
    print(round(value, 2))   # 1157.63
    #________________________________________________________________________________
    
    #________________________________________________________________________________
    #				    		'Keep Notes'
    """    @   → matrix multiplication
        @=  → matrix multiplication + assignment

        *   → multiplication / element-wise NumPy multiplication
        *=  → multiplication + assignment

        **  → exponentiation
        **= → exponentiation + assignment
    """
    #________________________________________________________________________________
    

if __name__ == "__main__":
    main() 

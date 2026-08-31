# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 04_set_data_types.py
# Path    : 02_Data_Types\04_set_data_types.py
# Subject : Set Data Type (Set and Frozenset)
# Description : 
# A set is an unordered collection used to store unique elements only, mainly for removing duplicates.
# • Elements are unordered (no fixed index position).
# • Sets are mutable (elements can be added or removed).
# • Duplicate values are not allowed (Stores unique elements only
# =============================================================================

#----------------------------------------------------------------------------------------------------
#					'Set Data Types'
#----------------------------------------------------------------------------------------------------

def heading(title):
        print("\n" + "=" * 70)
        print(f" {title}")
        print("=" * 70)

def main():
#----------------------------------------------------------------------------------------------------
#						'Set'
#----------------------------------------------------------------------------------------------------
        heading("Set")
        print("s = {10,20,30,40}")
        s = {10,20,20,30,40} 
        print("After removed duplication Set of S : ", s)    #40, 10, 20, 30 duplicate dropped
        print(type(s))
#________________________________________________________________________________
#				'Operations in Set'
        heading("Operations in Set")
        s.add(50)
        print("After add 50, Updated set is : ",s)    #{40, 10, 50, 20, 30}
        #s.remove(60)    #if value not found Generate Key Error
        s.discard(60)    #safe — no error if missing
        print("Length of code is : ",len(s))
#________________________________________________________________________________

#________________________________________________________________________________
#			        'Multiple Set Operations'

        heading("Multiple Set Operations")
        a = {1, 2, 3}
        b = {2, 3, 1, 4}
        print("A = ", a)
        print("B = ", b)

        print("Union(a | b) : ", a | b)             # Union : {1, 2, 3, 4}  #Way 1
        print("Union (a.union(b)): ", a.union(b))   # Union : {1, 2, 3, 4}  #Way 2

        print("Intersection (a & b): ", a & b )                                 # Intersection : {1, 2, 3}    #Way 1
        print("Intersection (a.intersection(b)) : ", a.intersection(b))         # Intersection : {1, 2, 3}    #Way 2
        print("Intersection (set(a) & set(b)): ", set(a) & set(b))              # Intersection : {1, 2, 3}    #Way 3
        print("Intersection (list(set([1, 2, 2, 3]))) : ", list(set([1, 2, 2, 3])))   # Intersection : {1, 2, 3}    #Way 4

        print("symmetric Difference (b - a): ", b - a)                       # Difference : {4}      #Way 1
        print("symmetric Difference (b.difference(a)) : ", b.difference(a))  # Difference : {4}      #Way 2
        print("symmetric Difference (a ^ b): ", a ^ b)                       # Difference : {4}      #Way 3
        print("symmetric Difference (b.symmetric_difference(a)): ", b.symmetric_difference(a))   # Difference : {4}      #Way 4

        heading("Subset / superset checks via boolean")
        print("a.issubset(b) : ",a.issubset(b))    # True  — all of a is in b
        print("b.issubset(b) : ",b.issubset(b))    # True  — all of b is in a
        print("a <= b", a <= b)     # same as issubset
        print("b.issuperset(a)",b.issuperset(a))  # True  — b contains all of a
        print("a.isdisjoint(b)",a.isdisjoint(b))  # False — they share elements
        print("b >= a", b >= a)     # same as issuperset
        print("2 in a",2 in a)      # 0(1) check lookup and return boolean
#________________________________________________________________________________

#________________________________________________________________________________
#				'Another Patterns in Set'

        print("-"*15, "Another Common patterns", "-"*15)
        heading("power(square)")
        #Way 1
        squares = {x**2 for x in range(6)}      
        print(squares)
        '''Description of code
        Step 1 : range(6) ha 0, 1, 2, 3, 4, 5 #This condition make this set 
        Step 2 : ** mean power(square)
        Step 3 : 
                0**2 = 0*0 = 0
                1**2 = 1*1 = 1
                2**2 = 2*2 = 4
                3**2 = 3*3 = 9
                4**2 = 4*4 = 16
                5**2 = 5*5 = 25
        '''
        # Way 2
        squares = set()
        for x in range(6):
                squares.add(x**2)
                print(squares)

        heading("Odd & Evens")
        values = {1, 2, 3, 4, 6, 7, 8, 10}
        print("Our values : ", values)
        evens = {x for x in values if x % 2 == 0}
        print("Even Values : ", evens)
        '''Description of Code
        Step 1 : x % 2 == 0        - This Condition check value Even or odd
                0 % 2 = 0  ✔
                1 % 2 = 1  ✘
                4 % 2 = 0  ✔
                9 % 2 = 1  ✘
                16 % 2 = 0 ✔
                25 % 2 = 1 ✘
        Step 2 : x for x in values - mean values madhil preatyek element x madhe ghya aani toch element x result madhe store kara 
        Step 3 : Inshort
        Read x from squares
                ↓
        Check x % 2 == 0
                ↓
        True?
                ↓
        Store x in set
        '''

        odd = {x for x in values if x % 2 != 0}
        print("Odd values : ", odd)

        heading("Clear()")
        values.clear()       #delete all element of set
        print("after used clear() : ", values)             #show set() for empty set
#________________________________________________________________________________

#----------------------------------------------------------------------------------------------------
#				        'Frozen Set'
#----------------------------------------------------------------------------------------------------

        heading("Creating a frozenset")
        nums = frozenset({10, 20, 30, 20})     # duplicate 20 dropped, just like set
        print(nums)
        print(type(nums))

        heading("Read operations work exactly like set")
        print(20 in nums)          # True — O(1) membership check
        print(len(nums))           # 3

        heading("Mutation is blocked")
        try:
                nums.add(40)
        except AttributeError as e:
                print("Error:", e)     # 'frozenset' object has no attribute 'add'

        heading("Set operations still work — they return a NEW frozenset")
        a = frozenset({1, 2, 3})
        b = frozenset({2, 3, 4})
        print("Union :", a | b)
        print("Intersection :", a & b)
        print("Difference :", a - b)

if __name__ == "__main__":
        main()




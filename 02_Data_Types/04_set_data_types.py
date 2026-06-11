# This code created by codingwithamar@gmail.com
# Path : python_system_programming/02_Data_Types/04_set_data_types.py
'''
Subject : Set Data Types
'''

print('''A set is an unordered collection used to store unique elements only, mainly for removing duplicates.
• Elements are unordered (no fixed index position).
• Sets are mutable (elements can be added or removed).
• Duplicate values are not allowed (Stores unique elements only)
''')

s = {10,20,20,30,40}
print("S = ", s)    #40, 10, 20, 30 duplicate dropped
print(type(s))

print("----------Operations in Set------------")
s.add(50)
print(s)    #{40, 10, 50, 20, 30}
#s.remove(60)    #if value not found Generate Key Error
s.discard(60)   #safe — no error if missing
print(len(s))

print("\n---------------Set Operation------------")
a = {1, 2, 3}
b = {2, 3, 1, 4}
print("A = ", a)
print("B = ", b)

print("Union : ", a | b)        # Union : {1, 2, 3, 4}  #Way 1
print("Union : ", a.union(b))   # Union : {1, 2, 3, 4}  #Way 2

print("Intersection : ", a & b )                    # Intersection : {1, 2, 3}    #Way 1
print("Intersection : ", a.intersection(b))         # Intersection : {1, 2, 3}    #Way 2
print("Intersection : ", set(a) & set(b))           # Intersection : {1, 2, 3}    #Way 3
print("Intersection : ", list(set([1, 2, 2, 3])))   # Intersection : {1, 2, 3}    #Way 4

print("Difference : ", b - a)                       # Difference : {4}      #Way 1
print("Difference : ", b.difference(a))             # Difference : {4}      #Way 2
print("Difference : ", a ^ b)                       # Difference : {4}      #Way 3
print("Difference : ", b.symmetric_difference(a))   # Difference : {4}      #Way 4

print("\n---------Subset / superset checks via boolean-------------")
print(a.issubset(b))    # True  — all of a is in b
print(b.issubset(b))    # True  — all of b is in a
print("<=", a <= b)     # same as issubset
print(b.issuperset(a))  # True  — b contains all of a
print(a.isdisjoint(b))  # False — they share elements
print(">=", b >= a)     # same as issuperset
print(2 in a)           # 0(1) check lookup and return boolean


print("\n----------Another Common patterns--------------")
print("---------power(square)-----------")
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


print("\n----------Odd & Evens--------------------")
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

print("\n----------Clear()-----------")
values.clear()       #delete all element of set
print("after used clear() : ", values)             #show set() for empty set
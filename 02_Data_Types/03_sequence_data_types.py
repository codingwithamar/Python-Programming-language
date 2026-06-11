# This code created by codingwithamar@gmail.com
# Path : python_system_programming/02_Data_Types/03_sequence_data_types.py
'''
Subject : Sequence Data Types(List Tuple range)
'''
print("Defination : Sequence Data Types are used to store multiple values in an ordered manner. Each element has a position called an index.\n")

print("----------1. List (list)-----------")
print("A list is an ordered collection used to store multiple values in a single variable, and it allows modification after creation.")
print('''Allows duplicate values
Uses square brackets []
Mutable (can be modified)''')
fruits = ["Apple", "Mango", "Banana", "Pineapple"]
print(fruits)
print(type(fruits))

print("\n----------1.1. Indexing in list sequence data types-----------")
name = ["A", "B", "C", "D"]
print(name[0])      #1st element
print(name[2])      #3rd Element
print(name[-1])     #last Element
print(name[-2])     #Second last element

print("\n----------1.2. Slicing in list sequence data types---------------")
print("Syntax : [start : stop : step]")
print("Default start = 0, Default End = n, Default Step = 1")
number = [10, 20, 30, 40, 50]
print(number[1:5])  #20, 30, 40, 50
print(number[1:6])  #20, 30, 40, 50     #NO Error Show
print(number[1:4])  #20, 30, 40
print(number[:3])   #10, 20, 30    
print(number[2:])   #30, 40, 50
print(number[::2])   #10, 30, 50
print(number[::-1])   #10, 30, 50       #Reversed list

print("\n----------1.3. Other Operations in list Sequence data Types---------------")
print(len(number))          # 5
30 in number          # True
print(number + [60, 70])    # concatenation
print(number * 2)           # repeat: [10,20,30,40,50,10,20,30,40,50]
print(min(number), max(number))  # 10, 50
print(number.index(30))     # 2   — position of value
print(number.count(20))     # 1   — how many times it appears
number[0] = 99              #0th number value changed
print(number)
number.append(70)   #add value in end of list
print(number)
number.insert(2, 80)    #Insert 80 in 2nd array list
print(number)
number.extend([90,100])     #add multiple elements at the last of list
print(number)
number.remove(99)       #Remove perticular list value
print(number)
number.pop()            #Remove last elements
print(number)           
number.sort()           #sorting lower to higher
print(number)
sorted(number)          #sorting lower to higher    
print(number)

print("\n-------------Looping------------------")
for i, item in enumerate(["a", "b", "c"]):
    print(i, item)                          # 0 a / 1 b / 2 c   #with index

for name, score in zip(["Amar", "Akshay"], [90, 85]):
    print(name, score)


print("\n----------2. Tuple(tuple)-----------")
print('''A tuple is similar to a list but is used when the data should not be changed after creation.
Allows duplicate values
Uses parentheses ( )
Immutable (cannot be modified) 
Used for fixed data ''')
colors = ("Red", "Sky Blue", "Baby Pink", "Navy blue", "Yellow")
print("Colors = ",colors)
print(type(colors))
#colors[1] = "Black"        #Error - Tuple not allows modification & updation

print("\n----------3. Range(range)-----------")
print('''The range data type represents a sequence of numbers and is commonly used in loops for iteration. 
Ordered sequence of numbers
Commonly used in loops
Memory efficient''')
print("Syntax - range(<starting_value>, <Ending_value>, <distance_value)")   #show n to n-1 values
numbers1 = range(1, 6, 2)     #   1   3   5
numbers2 = range(1, 6)        #   1   2   3   4   5
numbers3 = range(0, 6)        #   0   1   2   3   4   5
numbers4 = range(3)           #   0   1   2
print(list(numbers1))
print(list(numbers2))
print(list(numbers3))
print(list(numbers4))
print(type(numbers1))



# This code created by codingwithamar@gmail.com
# Path : python_system_programming/02_Data_Types/03_sequence_data_types.py
'''
Subject : Sequence Data Types(List Tuple range)
'''
print("Defination : Sequence Data Types are used to store multiple values in an ordered manner. Each element has a position called an index.\n")

print("----------1. List (list)-----------")
print("A list is an ordered and mutable (changeable) collection of items.")
print('''Allows duplicate values
Uses square brackets []''')
fruits = ["Apple", "Mango", "Banana", "Pineapple"]
print(fruits)
print(type(fruits))

print("\n----------2. Tuple(tuple)-----------")
print('''A tuple is an ordered and immutable (unchangeable) collection of items.
Allows duplicate values
Uses parentheses ( )''')
colors = ("Red", "Sky Blue", "Baby Pink", "Navy blue", "Yellow")
print("Colors = ",colors)
print(type(colors))

print("\n----------3. Range(range)-----------")
print('''A range generates a sequence of numbers.
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

print("\n----------4. Indexing in sequence types-----------")
name = ["A", "B", "C", "D"]
print(name[0])
print(name[2])

print("\n----------5. Slicing in Sequence Types---------------")
number = [10, 20, 30, 40, 50]
print(number[1:4])



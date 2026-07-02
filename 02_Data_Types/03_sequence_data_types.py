# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 03_sequence_data_types.py
# Path    : 02_Data_Types\03_sequence_data_types.py
# Subject : Sequnece Data Types
# Description : This is Master code of sequence data type
# =============================================================================

def heading(title):
    print("\n" + "=" * 70)
    print(f" {title}")
    print("=" * 70)

def main():
    heading("SEQUNECE DATA TYPE")
    print("Defination : Sequence Data Types are used to store multiple values in an ordered manner. Each element has a position called an index.\n")

    heading("TYPE 1 : LIST")
    print("Defination : A list is an ordered collection used to store multiple values in a single variable, and it allows modification after creation.")
    print("Allows duplicate values Uses square brackets [] Mutable (can be modified)")

    fruits = ["Apple", "Mango", "Banana", "Pineapple"]      #Creation
    print(fruits)                                           #Printing
    print(type(fruits))                                     #Check data Type


    heading("1.1 : Indexing in list sequence data types")
    name = ["A", "B", "C", "D"]
    print("1st element : ", name[0])      #1st element
    print("3rd Element : ", name[2])      #3rd Element
    print("last Element : ", name[-1])     #last Element
    print("Second last element : ", name[-2])     #Second last element

    heading("1.2 : Slicing in list sequence data type")
    print("Syntax : [start : stop : step]")
    print("Default start = 0, Default End = n, Default Step = 1")
    number = [10, 20, 30, 40, 50]
    print("list of Number : ", number)
    print("1 to 5 : ",number[1:5])      #20, 30, 40, 50
    print("1 to 5 : ",number[1:6])      #20, 30, 40, 50     #NO Error Show
    print("1 to 4 : ",number[1:4])      #20, 30, 40
    print("Start to 3 : ",number[:3])   #10, 20, 30    
    print("2 to end : ",number[2:])     #30, 40, 50
    print("start to end with 2 DIfference : ",number[::2])  #10, 30, 50
    print("Reverse list ",number[::-1])                     #10, 30, 50  #Reversed list

    heading("1.3 : Other Operations in list Sequence data Types")
    print("Lenght of Number : ", len(number))          # 5
    30 in number                # True
    print("after Concatenation : ", number + [60, 70])    # concatenation
    print("After repetation : ", number * 2)           # repeat: [10,20,30,40,50,10,20,30,40,50]
    print("Min and Max : ", min(number), max(number))  # 10, 50
    print("Fetch Value Position of List : ", number.index(30))     # 2   — position of value
    print("Count appear of Value : ", number.count(20))     # 1   — how many times it appears
    number[0] = 99              #0th number value changed
    print("Update 0th index Value : ", number)
    number.append(70)           #add value in end of list
    print("add value in end of list : ", number)
    number.insert(2, 80)        #Insert 80 in 2nd array list
    print("Insert 80 in 2nd array list : ", number)
    number.extend([90,100])     #add multiple elements at the last of list
    print("add multiple elements at the last of list : ", number)
    number.remove(99)           #Remove perticular list value
    print("Remove perticular list value : ", number)
    number.pop()                #Remove last elements
    print("Remove last elements : ", number)           
    number.sort()               #sorting lower to higher
    print("sorting lower to higher : ", number)
    sorted(number)              #sorting lower to higher    
    print("sorting lower to higher :", number)

    heading("1.4 : Looping in Sequence")
    for i, item in enumerate(["a", "b", "c"]):
        print(i, item)                                      # 0 a / 1 b / 2 c   #with index
    for name, score in zip(["Amar", "Akshay"], [90, 85]):
        print(name, score)                                  # Amar 90  Akshay 90    


    heading("TYPE 2 : TUPLE(tuple)")
    print('''A tuple is similar to a list but is used when the data should not be changed after creation.
    * Allows duplicate values
    * Uses parentheses ( )
    * Immutable (cannot be modified) 
    * Used for fixed data ''')
    colors = ("Red", "Sky Blue", "Baby Pink", "Navy blue", "Yellow")
    print("Our Tuple - Colors  : ", colors)
    print("Check Type of Tuple : ", type(colors))
    #colors[1] = "Black"        #Error - Tuple not allows modification & updation


    heading("TYPE 3 : RANGE")
    print('''Defination : The range data type represents a sequence of numbers and is commonly used in loops for iteration. 
    * Ordered sequence of numbers
    * Commonly used in loops
    * Memory efficient''')
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


if __name__ == "__main__":
    main()



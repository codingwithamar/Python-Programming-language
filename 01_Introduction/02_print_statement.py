
#This code created by codingwithamar@gmail.com
#path : python_system_programming/introduction/02_print_statement.py
#Subject : The print() function is used to display output in Python. 
#Common types include simple print, multiple-value print, separator print (sep), end print (end), 
#formatted print (f-string), format-method print, and escape-sequence print.


print("Way 1 :  Escape Sequence Print")  #Simple Way Print
print("Amar\nBhandare")
print("\n\n")

print("Way 2 : Print multiple values")  #objects → values to display
name = "Amar" "Bhandare"
age = 29
print(name,age)
print("\n\n")

print("Way 3 : Print with Separator (sep)") #sep → separator between values
print("09","06","2026\n\n",sep="-")

print("Way 4 : Print with End (end)")   #end → what to print at the end
print("hello", end="_")
print("World")
print("\n\n")

print("Way 5: Formatted String Print (f-string)")
name = "Piyush"
age  = "36"
print(f"Name : {name}, Age : {age}\n\n")    #"f" is compulsary for see variable values 

print("Way 6 : String Formatting using format()")
print("Name :{}\nAge :{}\n\n".format("Adarsh","28"))    #".format()" is the library function

print("Way 7 : Printing Variables and Expressions")
a = 10
b = 20
print("Sum = ",a+b)
print("\n\n")


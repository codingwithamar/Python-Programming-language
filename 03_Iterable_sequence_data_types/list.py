name = [11, 21, 51] 
Batches = ["PPA", "LB", "Python"] 

students = ["Amit", "Rahul", "Sneha"]

print(students[0])                      #Amit   #Access Perticular elements

students[1] = "Rohit"                   #Update
print("After replace Rahul to Rohit : ", students)   #['Amit', 'Rohit', 'Sneha']

students.append("Neha")                 #add new element
print("After Append new Elements : ",students)

print("After Insert New Elemets : ")    #At the insertion allowed only 2 Elements
students.insert(1, "Pooja")             #insert new element
print(students)

print("After Delete Elemets : ")        #list.remove() takes exactly one argument
students.remove("Amit")                 #Delete Element
print(students)
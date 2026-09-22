student = {
"Name":"Amit",
"Age":22,
"Marks":89
}

print(student)              #Complete Access
print(student["Name"])      #Perticular Access  #Amit

student["Age"] = 25         #Update
print("After Update : ", student)   #After Update :  {'Name': 'Amit', 'Age': 25, 'Marks': 89}

student["City"] = "Pune"    #Add
print("After Add New Elementds : ", student)    #After Add New Elementds :  {'Name': 'Amit', 'Age': 25, 'Marks': 89, 'City': 'Pune'}

del student["Marks"]        #Delete
print("After Delete Marks elements : ", student)    #After Delete Marks elements :  {'Name': 'Amit', 'Age': 25, 'City': 'Pune'}

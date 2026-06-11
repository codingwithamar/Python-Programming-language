# This code created by codingwithamar@gmail.com
# Path : python_system_programming/02_Data_Types/05_mapping_data_tyeps_dict.py
'''
Subject : Mapping Data Types (dict)
'''
print("Defination : dict stores data in key - value pairs, Keys must be unique and hashable (immutable).")
print('''Syntax :
dictionary_name = {
    "key1" : "value1",
    "key2" : "value2"
}''')
print("\n\n")
print("\n----------Creating in Dictionary---------------")
student = {
    "Name": "AMAR",
    "Age" : 29,
    "City" : "Pune"
}
print(student)

print("\n----------Accessing in Dictionary Values---------------")
print(student["Name"])
print(student.get("Age"))
print(student.keys())   #accessing all keys
print(student.values()) #accessing all values
print(student.items())  #accessing all keys and values

print("\n----------Add/Update in Dictionary Values---------------")
student["Email"] = "codingwithamar@gmail.com"
student["Age"] = 21
print(student)

print("\n----------Deletion in Dictionary Values---------------")
del student["Age"]
print(student)

print("\n----------Iteration in Dictionary Values---------------")
for key, value in student.items():
    print(f"{key}: {value}")





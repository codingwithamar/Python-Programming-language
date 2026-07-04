def Add(*no):
    ans = 0
    for i in no:
        ans = ans + i
    return ans

print(Add(10, 20, 30))
print(Add(10, 20, 30, 40, 50))


def total(*numbers):
    print(sum(numbers))

total(10, 20)
total(10, 20, 30)
total(10, 20, 30, 40)


def employee(id, name, department="IT", *skills, **details):
    print("ID:", id)
    print("Name:", name)
    print("Department:", department)
    print("Skills:", skills)
    print("Details:", details)

employee(
    101,
    "Amar",
    "Developer",
    "Python",
    "SQL",
    city="Pune",
    experience=3
)
# =============================================================================
# Author      : codingwithamar@gmail.com
# File        : 05_mapping_data_types_dict.py
# Path        : 02_Data_Types\05_mapping_data_types_dict.py
# Subject     : Mapping Data Types (dict)
# Description : dict stores data in key-value pairs.
#               Keys must be unique and hashable (immutable).
# =============================================================================

def heading(title):
    print("\n" + "=" * 70)
    print(f" {title}")
    print("=" * 70)


def main():

    print('''Syntax :
dictionary_name = {
    "key1": "value1",
    "key2": "value2"
}''')

    print("\n\n")

    # ============================================================
    heading("Creating Dictionary")

    student = {                     # Way 1
        "Name": "AMAR",
        "Age": 29,
        "City": "Pune"
    }
    print(student)

    student = dict(                 # Way 2
        Name="Amar",
        Age=30
    )
    print(student)

    # Other dictionary creation methods
    d1 = {'a': 1, 'b': 2}                    # Literal
    d2 = dict(a=1, b=2)                      # Constructor with keyword arguments
    d3 = dict([('a', 1), ('b', 2)])          # Iterable of key-value pairs
    d4 = {k: k**2 for k in range(5)}         # Dictionary comprehension
    d5 = dict.fromkeys(['x', 'y', 'z'], 0)   # All values initialized to 0

    print("\nd1 =", d1)
    print("d2 =", d2)
    print("d3 =", d3)
    print("d4 =", d4)
    print("d5 =", d5)

    # ============================================================
    heading("Accessing Dictionary Values")

    print(student["Name"])      # Access using key
    print(student.get("Age"))   # Safe access

    print(student.keys())       # All keys
    print(student.values())     # All values
    print(student.items())      # All key-value pairs

    # ============================================================
    heading("Add / Update Dictionary Values")

    student["Email"] = "codingwithamar@gmail.com"
    student["Age"] = 21
    print(student)
    student["Age"] = 31

    # ============================================================
    heading("Delete Dictionary Values")

    del student['Age']

    print(student)

    # ============================================================
    heading("Iterating Dictionary")

    for key, value in student.items():
        print(f"{key}: {value}")

    # ============================================================
    heading("Useful Dictionary Methods")

    d = {'a': 1, 'b': 2}

    print("get('c') :", d.get('c', 'default'))

    print("setdefault('c') :", d.setdefault('c', 'Absent'))
    print(d)

    print("popitem() :", d.popitem())
    print(d)


if __name__ == "__main__":
    main()
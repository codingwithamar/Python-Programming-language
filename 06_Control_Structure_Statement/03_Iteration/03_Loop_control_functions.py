# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 03_Loop_control_statement.py
# Path    : Python-Programming-Language/06_Control_Structure_Statement/03_Iteration/03_Loop_control_statement.py
# Subject : Control Structure Statements - Loop control functions
# Description : Used to change the normal execution flow of loops- 1.break, 2.continue 3.pass
# =============================================================================

def main():
#________________________________________________________________________________
#						    '1. break function'
    print("The break statement immediately terminates the loop.")
    #example 1 -
    for num in range(10):
        if num == 5:
            break
        print(num)

    print()

    #example 2 -
    users = ["amit", "sara", "admin", "ravi"]

    for user in users:
        if user == "admin":
            print("Admin account found:", user)
            break
    else:
        print("No admin account found.")

    print("Search finished.")
#________________________________________________________________________________
    print()
#________________________________________________________________________________
#						'2. continue function'
    print("Skips the current iteration round, goes to the next check")

    #Example 1 -
    for i in range(10):
        if i == 3:
            continue
        print(i)

    print()

    #Example 2 -
    total = []
    skip_record = []
    records = ["10", "abc", "20", "30", "def", "40"]

    for record in records:
        if not record.isdigit():
            print("Skipped invalid records : ",repr(record))
            skip_record.append(record)
            continue
        total.append(record)
    print("Total Valid numbers : ",total)
    print("Skip records : ", skip_record)
#________________________________________________________________________________

if __name__ == "__main__":
    main()
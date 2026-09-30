# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 03_Loop_control_statement.py
# Path    : Python-Programming-Language/06_Control_Structure_Statement/03_Iteration/03_Loop_control_statement.py
# Subject : Control Structure Statements - Loop control statements
# Description : Used to change the normal execution flow of loops- 1.break, 2.continue 3.pass
# =============================================================================

def main():
#________________________________________________________________________________
#						    '1. break statements'
    print("The break statement immediately terminates the loop.")
    #example 1 -
    for num in range(10):
        if num == 5:
            break
        print(num)

    print("-"*30)

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
    print("-"*50)
#________________________________________________________________________________
#						'2. continue statements'
    print("Skips the current iteration round, goes to the next check")

    #Example 1 -
    for i in range(10):
        if i == 3:
            continue
        print(i)

    print("-"*30)

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
    print("-"*50)
#________________________________________________________________________________
#						      'pass statement'
    print("""pass does absolutely nothing. It exists only because Python requires every block to have at least one line — it cannot be empty. pass is a placeholder to satisfy that rule.""")

    for num in range(5):
        pass          # loop runs but does nothing each time
#________________________________________________________________________________
    print('*'*50)
    print("break vs continue vs pass")
    #________________________________________________________________________________
    #						'break vs continue vs pass'
    for num in range(10):
        if num == 2:
            pass                 # does nothing, prints normally
        if num == 4:
            continue              # skips only this round
        if num == 5:
            break                 # stops the whole loop
        print(num)
    #________________________________________________________________________________
    
if __name__ == "__main__":
    main()
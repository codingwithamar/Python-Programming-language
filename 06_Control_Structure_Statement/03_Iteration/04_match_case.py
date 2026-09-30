# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 04_match_case.py
# Path    : Python-Programming-Language/06_Control_Structure_Statement/03_Iteration/04_match_case.py
# Subject : Match Case 
# Description : Structural pattern matching - match...case
# =============================================================================

def main():
    command = "start"

    match command:
        case "start":
            print("Starting")
        case "stop":
            print("Stopping")
        case _:
            print("Unknown command")

if __name__ == "__main__":
    main()
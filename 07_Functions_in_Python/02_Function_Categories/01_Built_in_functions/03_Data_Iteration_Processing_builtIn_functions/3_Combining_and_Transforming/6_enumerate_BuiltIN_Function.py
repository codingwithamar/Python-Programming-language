# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : enumerate_BuiltIN_Function.py
# Path    : Python-Programming-Language/07_Functions_in_Python/02_Function_Categories/01_Built_in_functions/03_Data_Iteration_Processing_builtIn_functions/3_Combining_and_Transforming/enumerate_BuiltIN_Function.py
# Subject : Import functions in python
# Description : enumerate() - Adds a counter to an iterable. It gives (index, item) pairs.
# =============================================================================

def main():
    print("Syntax : enumerate(iterable, start=0)")
    
    tasks = ["backup", "cleanup", "report"]

    for index, task in enumerate(tasks):
        print(index, task)
    # 0 backup
    # 1 cleanup
    # 2 report

    # Start counting from 1 (good for messages shown to people)
    for number, task in enumerate(tasks, start=1):
        print(f"Step {number}: {task}")

    # Find the line numbers of errors in a log
    log_lines = ["start", "ERROR disk", "ok", "ERROR network"]
    error_lines = [n for n, line in enumerate(log_lines, start=1) if "ERROR" in line]
    print(error_lines)      # [2, 4]

    # Convert to a dictionary
    print(dict(enumerate(["a", "b", "c"])))     # {0: 'a', 1: 'b', 2: 'c'}

if __name__ == "__main__":
    main()
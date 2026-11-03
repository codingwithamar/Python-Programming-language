# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 03_args_and_kwargs.py
# Path    : Python-Programming-Language/07_Functions_in_Python/02_Function_Categories/02_User_defined_functions/01_User_Define_Function_Basics/03_args_and_kwargs.py
# Subject : User Define Function
# Description : *args and *kwargs
# =============================================================================

def main():
#%% Basic Concepts
    def add_all(*numbers):
        print(type(numbers))        # <class 'tuple'>
        total = 0
        for n in numbers:
            total += n
        return total

    print(add_all(1, 2, 3))         # 6
    print(add_all(10, 20, 30, 40))  # 100
    print(add_all())                # 0

    def show_profile(**details):
        print(type(details))        # <class 'dict'>
        for key, value in details.items():
            print(f"{key}: {value}")

    show_profile(name="Amar", age=25, city="Pune")

#%% Advanced Examples
    # Combine everything. Required order of parameters:
    # normal, defaults, *args, keyword-only, **kwargs
    def log_task(task_name, priority=1, *steps, status, **metadata):
        print("Task:", task_name)
        print("Priority:", priority)
        print("Steps:", steps)
        print("Status:", status)          # keyword-only, because it comes after *steps
        print("Metadata:", metadata)

    log_task("Backup", 2, "connect", "copy", "verify", status="done", duration=12, user="amar")
    # Task: Backup
    # Priority: 2
    # Steps: ('connect', 'copy', 'verify')
    # Status: done
    # Metadata: {'duration': 12, 'user': 'amar'}

    # Pass everything through to another function (very common in wrappers)
    def my_print(*args, **kwargs):
        print("[LOG]", *args, **kwargs)

    my_print("a", "b", sep="-", end="!\n")        # [LOG] a-b!

if __name__ == "__main__":
    main()
# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 03_global_variable.py
# Path    : Python-Programming-Language/07_Functions_in_Python/01_Variable_scope/03_global_variable.py
# Subject : Variable scope in python
# Description : global scope variables
# =============================================================================

def main():
    # Example 1 : Accessible everywhere
    app_name = "AutomationTool"       # global variable

    def show_name():
        print("App name is:", app_name)   # can read the global variable

    show_name()
    print("App name is:", app_name)       # also works here
    
    #Output :
    #           App name is: AutomationTool
    #           App name is: AutomationTool

    # Example 2 :

    counter = 0                        # global variable

    def log_event(event):
        print("Event:", event)
        print("Current counter (read-only):", counter)

    log_event("Backup started")
    
if __name__ == "__main__":
    main()
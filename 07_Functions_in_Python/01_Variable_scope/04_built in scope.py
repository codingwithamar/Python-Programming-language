# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 04_built in scope.py
# Path    : Python-Programming-Language/07_Functions_in_Python/01_Variable_scope/04_built in scope.py
# Subject : Variable scope in python
# Description : built in function scope
# =============================================================================

# %% Example 1
x = 10

def check_scope():
    y = 20
    print("Local variables:", locals())     #Local variables: {'y': 20}

check_scope()
print("Global variables include 'x':", "x" in globals())    #Global variables include 'x': True

print()
print()
#NOTE:
# globals and locals is built-in functions.
#   locals()	A dictionary of all variables in the current local scope
#   globals()	A dictionary of all variables in the current global (module-level) scope
#________________________________________________________________________________
#					'Varible scope in built-in locals() function'
# %% Basic Example of locals():

def show_locals():
    x = 10
    y = "hello"
    print(locals())

show_locals()   #{'x': 10, 'y': 'hello'}

print()
# %%Advanced example of locals():
def calculate_order(price, quantity):
    tax_rate = 0.1
    subtotal = price * quantity
    tax = subtotal * tax_rate
    total = subtotal + tax

    print("Snapshot of local variables:")
    for name, value in locals().items():
        print(f"  {name} = {value}")

    return total

calculate_order(100, 3)

#OUTPUT :
#Snapshot of local variables:
#  price = 100
#  quantity = 3
#  tax_rate = 0.1
#  subtotal = 300
#  tax = 30.0
#  total = 330.0
#________________________________________________________________________________
print()
print()
#________________________________________________________________________________
#					'Varible scope in built-in globals() function'
# %%Basic Example of globals():
app_name = "AutomationTool"
version = "1.0"

print(globals()["app_name"])     # AutomationTool

print()
# %%Advanced Example of globals()
counter = 0
status = "idle"

def show_global_state():
    print("Current global state:")
    for name, value in globals().items():
        if not name.startswith("__"):          # skip Python's internal built-in names
            print(f"  {name} = {value}")

show_global_state()
#________________________________________________________________________________


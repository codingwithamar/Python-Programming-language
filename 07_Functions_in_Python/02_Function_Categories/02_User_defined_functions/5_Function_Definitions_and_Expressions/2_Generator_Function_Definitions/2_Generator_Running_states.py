
# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 2_Generator_Running_states.py
# Path    : Python-Programming-Language/07_Functions_in_Python/02_Function_Categories/02_User_defined_functions/5_Function_Definitions_and_Expressions/2_Generator_Function_Definitions/2_Generator_Running_states.py
# Subject : User Defined Function
# Description : Function Definitions/Generator Function Definition/Generator Running States
# =============================================================================

#%% Basic Example
def demo():
    print("start")
    yield 1
    print("middle")
    yield 2
    print("end")

g = demo()
print("created")
print(next(g))    # prints: start, then 1
print(next(g))    # prints: middle, then 2

print()
# %% Advanced Example
import inspect

g = demo()
print(inspect.getgeneratorstate(g))   # GEN_CREATED
next(g)                               # start
print(inspect.getgeneratorstate(g))   # GEN_SUSPENDED
list(g)                               # middle, end
print(inspect.getgeneratorstate(g))   # GEN_CLOSED

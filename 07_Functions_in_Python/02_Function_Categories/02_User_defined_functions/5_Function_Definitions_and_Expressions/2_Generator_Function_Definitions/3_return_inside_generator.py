# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 3_return_inside_generator.py
# Path    : Python-Programming-Language/07_Functions_in_Python/02_Function_Categories/02_User_defined_functions/5_Function_Definitions_and_Expressions/2_Generator_Function_Definitions/3_return_inside_generator.py
# Subject : User Defined Function
# Description : Function Definitions/Generator Function Definition/Return Inside Generator
# =============================================================================

def main():
#%%Basic Example
    def g():
        yield 1
        yield 2
        return "done"

    it = g()
    next(it); next(it)
    try:
        next(it)
    except StopIteration as e:
        print(e.value)    # done

#%% Advanced example (collect items and the return value)
    def read_lines(lines):
        count = 0
        for line in lines:
            count += 1
            yield line.strip()  
            #strip() ही Python मधील String Method आहे. ती string च्या सुरुवातीला आणि शेवटी असलेले whitespace (spaces, tabs, newlines) काढते.
        return count

    def collect(gen):
        items = []
        while True:
            try:
                items.append(next(gen))
            except StopIteration as e:
                return items, e.value

    print(collect(read_lines([" a ", " b "])))   # (['a', 'b'], 2)

if __name__ == "__main__":
    main()
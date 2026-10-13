# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 15_tuple_Collection.py
# Path    : Python-Programming-Language/07_Functions_in_Python/02_Function_Categories/01_Built_in_functions/02_Object_Type_Handling_builtIn_functions/3_Collection_Functions/15_tuple_Collection.py
# Subject : Collection Built-In Functions
# Description : tuple() - Creates a tuple, or converts an iterable into a tuple.
# =============================================================================

def main():
    t1 = tuple()           # ()
    t2 = tuple([1, 2, 3])  # (1, 2, 3)
    t3 = tuple("abc")      # ('a', 'b', 'c')

    def get_coordinates():
        return tuple([10, 20]) 
    # returning a tuple so caller cannot accidentally modify it

    coords = get_coordinates()
    print(coords)      # (10, 20)
    # coords[0] = 99   # TypeError -> tuples are immutable

    # Using a tuple as a dict key (only possible because tuples are hashable)
    locations = {
        (0, 0): "origin",
        (1, 1): "diagonal point"
    }
    print(locations[(0, 0)])     # origin

if __name__ == "__main__":
    main()
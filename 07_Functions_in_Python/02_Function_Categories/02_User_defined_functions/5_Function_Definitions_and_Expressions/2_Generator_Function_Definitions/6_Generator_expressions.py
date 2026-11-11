# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 6_Generator_expressions.py
# Path    : Python-Programming-Language/07_Functions_in_Python/02_Function_Categories/02_User_defined_functions/5_Function_Definitions_and_Expressions/2_Generator_Function_Definitions/6_Generator_expressions.py
# Subject : User Defined Function
# Description : Function Definitions/Generator Function Definition/Generator expressions
# =============================================================================

def main():
    #Genarator Function
    def numbers():
        for x in range(5):
            yield x * 2

    # Genarator Expression
    numbers = (x * 2 for x in range(5))

#%% Basic Examples
    list_numbers = [x * 2 for x in range(5)]
    print(list_numbers)  # [0, 2, 4, 6, 8]
    #It creates a list containing all the results.

    tuple_numbers = (x * 2 for x in range(5))
    print(tuple_numbers)    # <generator object <genexpr> at ...>
    #It creates a generator object, not a list.

    numbers = (x * 2 for x in range(5))
    print(next(numbers))    # 0
    print(next(numbers))    # 2
    print(next(numbers))    # 4
    #It creates a generator object, not a list.

    numbers = (x for x in range(10) if x % 2 == 0)
    print(list(numbers))    # You can use if to filter values.
    #You can use if to filter values.

    squares = (x ** 2 for x in range(1, 6))
    for value in squares:
        print(value)
    # Suppose we want to calculate the squares of numbers from 1 to 5.

#%% Real Examples 1
    def read_large_file(path):
        with open(path, encoding="utf-8") as f:
            for line in f:
                yield line.rstrip("\n")

    for line in read_large_file("rclone.log"):
        if "ERROR" in line:
            print(line)

#%% Real Example 2 : Batches
    def batched(iterable, size):
        batch = []
        for item in iterable:
            batch.append(item)
            if len(batch) == size:
                yield batch
                batch = []
        if batch:
            yield batch

    for b in batched(range(7), 3):
        print(b)      # [0, 1, 2]  [3, 4, 5]  [6]

#%% Real Example 3 : Page API Pattern
    def fetch_all(get_page):
        page = 1
        while True:
            data = get_page(page)     # your API call
            if not data:
                return
            yield from data
            page += 1

#%% Real Example 4 : Mini Schedular
    def task(name, steps):
        for i in range(1, steps + 1):
            print(name, "step", i)
            yield                      # give control back

    def run(tasks):
        while tasks:
            t = tasks.pop(0)
            try:
                next(t)
                tasks.append(t)        # not finished, go to the back of the line
            except StopIteration:
                pass

    run([task("A", 2), task("B", 3)])
    # A step 1, B step 1, A step 2, B step 2, B step 3

if __name__ == "__main__":
    main()
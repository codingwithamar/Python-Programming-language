# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 1_Generator_Function_Concept.py
# Path    : Python-Programming-Language/07_Functions_in_Python/02_Function_Categories/02_User_defined_functions/5_Function_Definitions_and_Expressions/2_Generator_Function_Definitions/1_Generator_Function_Concept.py
# Subject : User Defined Function
# Description : Function Definitions/ Generator Function(Synchronous) Definition/Concept
# =============================================================================
import sys

def main():
#%% Concept
    # If we want print 10 numbers serially then we use Function using loop/range
    def whileCreator():
        #Using While Loop
        list = []
        i = 1
        while i<10:
            list.append(i)
            i += 1
        return list
    
    print(whileCreator())
    whileSize = sys.getsizeof(list)
    print("while list size is : ",whileSize,"Bytes")

    print("")
    #Using range Function
    RangeNumbers = list(range(1,10))
    print(RangeNumbers)
    rangeSize = sys.getsizeof(list)
    print("range list size is : ",rangeSize,"Bytes")

    '''
    OUTPUT : 

    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    while list size is :  416 Bytes

    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    range list size is :  416 Bytes
    '''

    print()
    # We see print all Numbers (List) at time in one called...
    # and if we want single number or perticular number serially when we called...
    # both functions not hold and remembered serial so python introduced Generator function - yield

    def yieldCreater():
        i = 1
        while i < 10:
            yield i     #it commit point, it hold the value serial
            i += 1
    print(yieldCreater())   
    #here Object Created - <generator object main.<locals>.yieldCreater at 0x752005cf2980>

    X = yieldCreater()
    print(next(X))  #1st print
    print(next(X))  #2nd print
    print(next(X))  #3rd print
    # We see it print serial by call, If we want print all list
    print(list(X))

    '''
    OUTPUT : 
    <generator object main.<locals>.yieldCreater at 0x793190746980>
    1
    2
    3
    [4, 5, 6, 7, 8, 9]
    '''

#%% Basic Examples
    def countdown(n):
        while n > 0:
            yield n
            n -= 1

    # 1. Use it in a for loop (the usual way)
    for number in countdown(3):
        print(number)            # 3  2  1

    # 2. Use next() by hand
    g = countdown(2)
    print(type(g))               # <class 'generator'>
    print(next(g))               # 2
    print(next(g))               # 1
    # print(next(g))             # StopIteration -> the generator is finished

    # 3. Turn it into a list (this uses it up)
    print(list(countdown(4)))    # [4, 3, 2, 1]

#%% Advaneced Examples
    #1. The body runs only when you ask (execution trace)
    def demo():
        print("start")
        yield 1
        print("middle")
        yield 2
        print("end")

    g = demo()
    print("created")      # created        (the body has NOT started)
    print(next(g))        # start, then 1
    print(next(g))        # middle, then 2
    try:
        next(g)           # end, then StopIteration
    except StopIteration:
        print("finished")
    '''
    OUTPUT :
        created
        start
        1
        middle
        2
        end
        finished
    '''

    #2. Local variables are kept between values
    def running_total(numbers):
        total = 0
        for n in numbers:
            total += n            # "total" is remembered between yields
            yield total

    print(list(running_total([10, 20, 30])))     # [10, 30, 60]

    #3. Lazy values: big data without a big list
    def squares(n):
        for i in range(n):
            yield i * i

    print(sum(squares(1_000_000)))               # 333332833333500000 (no list of a million numbers)

    #4. An endless generator (safe because it is lazy)
    from itertools import islice

    def fib():
        a, b = 0, 1
        while True:
            yield a
            a, b = b, a + b

    print(list(islice(fib(), 10)))               # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    # list(fib())                                # NEVER: it would run forever

    #5. Read a big file one line at a time
    def read_lines(path):
        with open(path) as f:
            for line in f:
                yield line.rstrip("\n")
        # for line in read_lines("big_log.txt"):      # only one line in memory at a time
        #     if "ERROR" in line:
        #         print(line)

    #6. A generator is used up after one pass
    g = countdown(3)
    print(list(g))               # [3, 2, 1]
    print(list(g))               # []   -> already used up

    #7. Each call makes an independent generator
    a = countdown(3)
    b = countdown(3)
    print(next(a), next(a), next(b))     # 3 2 3   -> a and b have separate state

    #8. A generator is its own iterator
    g = countdown(3)
    print(iter(g) is g)                  # True
    print(hasattr(g, "__next__"))        # True
    print(hasattr(g, "__len__"))         # False -> a generator has no length
        # len(g)                             # TypeError
        # g[0]                               # TypeError: 'generator' object is not subscriptable

    #9. Any yield makes the whole function a generator
    def f():
        return           # ends at once
        yield            # never reached, but it still makes f a generator function

    print(type(f()))                     # <class 'generator'>
    print(list(f()))                     # []

    #10. The same thing written as an iterator class (more code)
    class Countdown:
        def __init__(self, start):
            self.current = start

        def __iter__(self):
            return self

        def __next__(self):
            if self.current <= 0:
                raise StopIteration
            value = self.current
            self.current -= 1
            return value

    print(list(Countdown(3)))            # [3, 2, 1]
        # The generator version is 4 lines. This class is 12 lines for the same result.

    #11 Generator or list?
    def get_squares_list(n):
        result = []
        for i in range(n):
            result.append(i * i)
        return result                    # builds everything first

    def get_squares_gen(n):
        for i in range(n):
            yield i * i                  # makes one value at a time

if __name__ == "__main__":
    main()


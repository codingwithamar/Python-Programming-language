# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 5_Two_Way_Generator.py
# Path    : Python-Programming-Language/07_Functions_in_Python/02_Function_Categories/02_User_defined_functions/5_Function_Definitions_and_Expressions/2_Generator_Function_Definitions/5_Two_Way_Generator.py
# Subject : User Defined Function
# Description : Function Definitions/Generator Function Definition/Two way genrator(send,throw,close)
# =============================================================================

def main():
#%% Two way generator - 
#0 Prime Generator
    def my_generator():
        x = yield "Ready"
        print("Received:", x)


    g = my_generator()

    next(g)        # Priming
    g.send(100)    # Sending value

    #g = my_generator()
    #g.send(100)   # TypeError
    '''
    g = my_generator() → Generator object तयार होतो; execution सुरू होत नाही.
    next(g) → Generator पहिल्या yield पर्यंत execute होतो.
    g.send(100) → Paused yield ला 100 मिळते.
    पहिल्यांदा next(g) किंवा g.send(None) वापरून generator prime करावा लागतो.
    '''

#1 Send()
    def my_generator():
        x = yield "Ready"
        print("Received:", x)

    g = my_generator()

    print(next(g))
    print(g.send(100))
    '''
    OUTPUT : 
    Ready
    Received: 100
    '''
#2 throw()
    def my_generator():
        try:
            yield "Ready"
        except ValueError:
            yield "Error received"

    g = my_generator()

    print(next(g))
    print(g.throw(ValueError))
    '''
    OUTPUT : 
    Ready
    Error received
    '''

#3 close()
    def my_generator():
        try:
            yield "Running"
        except GeneratorExit:
            print("Generator closed")

    g = my_generator()

    print(next(g))
    g.close()
    '''
    OUTPUT :
    Running
    Generator closed
    '''

#%% Two Way Generator - send(),throw() and close()
    def worker():
        try:
            while True:
                try:
                    job = yield
                    print("working on", job)
                except ValueError:
                    print("bad job skipped")
        finally:
            print("cleanup")

    w = worker()
    next(w)
    w.send("A")            # working on A
    w.throw(ValueError)    # bad job skipped
    w.send("B")            # working on B
    w.close()              # cleanup

if __name__ == "__main__":
    main()


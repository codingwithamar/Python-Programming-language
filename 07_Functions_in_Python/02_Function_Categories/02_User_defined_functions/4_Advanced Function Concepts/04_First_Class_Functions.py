# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 04_First_Class_Functions.py
# Path    : Python-Programming-Language/07_Functions_in_Python/02_Function_Categories/02_User_defined_functions/4_Function_as_a_Tools/04_First_Class_Functions.py
# Subject : User define Function
# Description : First Class Functions
# =============================================================================

def main():
#%% Basic Concepts
#   name = "Amar"
#   age = 25
# Like above object examples we can use function,
# Assign to variable, pass as argument, return a function, store a function in list,tuple,dictionary

    def greet():
        print("Hello Python")

    say = greet

    say()

    #OUTPUT : Hello Python
    """
    def greet(name): ...            greet  ───────►  [ function object ]
                                                            |
    say = greet                     say    ───────►  (same object)
    """

#%% Basic Examples
    # 1. Assign a function to a variable (no brackets)
    def greet(name):
        return f"Hello, {name}"

    say = greet
    print(say("Amar"))              # Hello, Amar
    print(say is greet)             # True  -> the same object
    print(type(greet))              # <class 'function'>
    print(greet.__name__)           # greet

    # 2. Store functions in a list
    operations = [str.upper, str.lower, str.title]
    for operation in operations:
        print(operation("hELLO"))   # HELLO, hello, Hello

    # 3. Store functions in a dictionary
    def add(a, b):
        return a + b

    def multiply(a, b):
        return a * b

    actions = {"add": add, "multiply": multiply}
    print(actions["add"](2, 3))         # 5
    print(actions["multiply"](2, 3))    # 6

    # 4. Pass a function as an argument (callback)
    def apply(func, value):
        return func(value)

    print(apply(len, "hello"))          # 5
    print(apply(str.upper, "hi"))       # HI

    # 5. Return a function from a function
    def make_greeter(greeting):
        def greeter(name):
            return f"{greeting}, {name}"
        return greeter

    hello = make_greeter("Hello")
    hi = make_greeter("Hi")
    print(hello("Amar"), "|", hi("Amar"))    # Hello, Amar | Hi, Amar

    print("-"*30)
#%% Advanced Examples
# 1) Dispatch table (replaces a long if/elif)
    import operator

    OPERATIONS = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv,
    }

    def calculate(a, symbol, b):
        func = OPERATIONS.get(symbol)
        if func is None:
            raise ValueError(f"Unknown operator: {symbol}")
        return func(a, b)

    print(calculate(6, "*", 7))      # 42
    print(calculate(9, "/", 3))      # 3.0

    # A command table with a default action
    def start(): return "Starting"
    def stop(): return "Stopping"
    def unknown(): return "Unknown command"

    commands = {"start": start, "stop": stop}
    for cmd in ["start", "stop", "restart"]:
        print(commands.get(cmd, unknown)())
    # Starting
    # Stopping
    # Unknown command

# 2) Callbacks
    def download(files, on_progress, on_done):
        for number, name in enumerate(files, start=1):
            on_progress(name, number, len(files))     # call the callback
        on_done(len(files))

    def show_progress(name, number, total):
        print(f"[{number}/{total}] {name}")

    def finished(count):
        print(f"Done: {count} files")

    download(["a.csv", "b.csv"], show_progress, finished)
    # [1/2] a.csv
    # [2/2] b.csv
    # Done: 2 files

# 3) Registry with a decorator (event handlers)
    handlers = {}

    def register(event):
        def decorator(func):
            handlers[event] = func        # store the function in the dictionary
            return func
        return decorator

    @register("created")
    def on_created(name):
        return f"{name} created"

    @register("deleted")
    def on_deleted(name):
        return f"{name} deleted"

    print(handlers["created"]("a.txt"))     # a.txt created
    print(sorted(handlers))                 # ['created', 'deleted']

# 4) The key= function in sorted, min, max
    words = ["pear", "fig", "banana"]
    print(sorted(words, key=len))           # ['fig', 'pear', 'banana']
    print(max(words, key=len))              # banana
    print(sorted(words, key=str.lower))     # ['banana', 'fig', 'pear']

    employees = [("Amar", 25), ("Sara", 22), ("Ravi", 30)]
    print(sorted(employees, key=lambda person: person[1]))
    # [('Sara', 22), ('Amar', 25), ('Ravi', 30)]

# 5) map and filter take functions
    print(list(map(int, ["1", "2", "3"])))              # [1, 2, 3]
    print(list(filter(str.isdigit, ["1", "a", "3"])))   # ['1', '3']

# 6) A function that takes and returns functions (compose)
    def compose(*funcs):
        def run(value):
            for func in funcs:
                value = func(value)
            return value
        return run

    clean = compose(str.strip, str.lower, str.title)
    print(clean("   hELLO wORLD  "))        # Hello World

# 7) Callbacks that need extra arguments (functools.partial)
    from functools import partial

    def log(level, message):
        print(f"[{level}] {message}")

    callbacks = [partial(log, "INFO"), partial(log, "ERROR")]
    for callback in callbacks:
        callback("event happened")
    # [INFO] event happened
    # [ERROR] event happened

# 8) Callbacks inside the standard library
    import sched
    import threading
    import time

    def job(name):
        print("Running", name)

    # sched: "action" is a callback. Pass job, not job()
    scheduler = sched.scheduler(time.time, time.sleep)
    scheduler.enter(0, 1, job, argument=("backup",))
    scheduler.run()                                       # Running backup

    # threading: "target" is a callback
    worker = threading.Thread(target=job, args=("report",))
    worker.start()
    worker.join()                                         # Running report

# 9) Strategy pattern (choose behavior by name)
    def no_discount(price): return price
    def student_discount(price): return price * 0.8
    def festival_discount(price): return price * 0.7

    DISCOUNTS = {
        "none": no_discount,
        "student": student_discount,
        "festival": festival_discount,
    }

    def final_price(price, kind="none"):
        return DISCOUNTS[kind](price)

        print(final_price(1000, "student"))      # 800.0
        print(final_price(1000, "festival"))     # 700.0

# 10) Callable objects and bound methods
    # An object with __call__ behaves like a function
    class Multiplier:
        def __init__(self, factor):
            self.factor = factor

        def __call__(self, x):
            return x * self.factor

    double = Multiplier(2)
    print(double(10))                # 20
    print(callable(double))          # True
    print(callable(Multiplier))      # True  -> classes are callable too
    print(callable(5))               # False

    # A method is also an object, bound to its instance
    class Greeter:
        def hello(self, name):
            return f"Hello {name}"

    g = Greeter()
    method = g.hello
    print(method("Amar"))                    # Hello Amar
    print(method.__self__ is g)              # True
    print(method.__func__ is Greeter.hello)  # True

# 11) Functions can have attributes
    def counter_func():
        counter_func.calls += 1

    counter_func.calls = 0
    counter_func()
    counter_func()
    print(counter_func.calls)               # 2
    print(vars(counter_func))               # {'calls': 2}

# 12) Functions are hashable (they can be dictionary keys)
    names = {len: "length", max: "maximum"}
    print(names[len])                       # length

    def f(): pass
    def g(): pass
    print(f == g)                           # False -> functions compare by identity

# 13) Traps
    # Trap 1: callbacks in a loop (late binding)
    callbacks = [lambda: i for i in range(3)]
    print([cb() for cb in callbacks])                  # [2, 2, 2]

    callbacks = [lambda i=i: i for i in range(3)]      # fix: capture the value
    print([cb() for cb in callbacks])                  # [0, 1, 2]

    # Trap 2: calling the function when you meant to pass it
    def run_twice(func):
        func()
        func()

    def hello():
        print("hi")

    run_twice(hello)                 # correct: prints hi twice
    # run_twice(hello())             # wrong: hello() runs once, gives None, then None() fails
    #                                # TypeError: 'NoneType' object is not callable

    # Trap 3: a missing key in a dispatch table
    # commands["restart"]()          # KeyError. Use .get(name, default) instead


if __name__ == "__main__":
    main()
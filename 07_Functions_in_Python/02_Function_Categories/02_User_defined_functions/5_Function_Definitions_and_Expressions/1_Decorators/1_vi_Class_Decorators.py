# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 1_vi_Class_Decorators.py
# Path    : Python-Programming-Language/07_Functions_in_Python/02_Function_Categories/02_User_defined_functions/5_Function_Definitions_and_Expressions/1_Decorators/1_vi_Class_Decorators.py
# Subject : User Defined Functions
# Description : Class Decorators
# =============================================================================

def main():
#%% Basic Examples
    def add_repr(cls):
        def __repr__(self):
            return f"{cls.__name__}({self.__dict__})"
        cls.__repr__ = __repr__
        return cls

    @add_repr
    class User:
        def __init__(self, name, age):
            self.name = name
            self.age = age

    print(User("Amar", 25))              # User({'name': 'Amar', 'age': 25})

#%% Advanced Decorators
    # 1. A registry of classes (plugins)
    PLUGINS = {}

    def register(cls):
        PLUGINS[cls.__name__.lower()] = cls
        return cls

    @register
    class Backup:
        def run(self): return "backup running"

    @register
    class Report:
        def run(self): return "report running"

    print(PLUGINS["report"]().run())     # report running
    print(sorted(PLUGINS))               # ['backup', 'report']

    # 2. dataclass is a class decorator from the standard library
    from dataclasses import dataclass

    @dataclass
    class Point:
        x: int
        y: int = 0

    print(Point(1, 2))                   # Point(x=1, y=2)
    print(Point(1) == Point(1, 0))       # True

    # 3. Add a method to every class that uses the decorator
    def add_greeting(cls):
        cls.greet = lambda self: f"Hello from {type(self).__name__}"
        return cls

    @add_greeting
    class Robot:
        pass

    print(Robot().greet())               # Hello from Robot

if __name__ == "__main__":
    main()
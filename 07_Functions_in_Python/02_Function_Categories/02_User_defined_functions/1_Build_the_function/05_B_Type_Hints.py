# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 05_B_Type_Hints.py
# Path    : Python-Programming-Language/07_Functions_in_Python/Group1_Build_the_function/05_B_Type_Hints.py
# Subject : User Defined Functions
# Description : Type Hints
# =============================================================================

def main():
#%% Basic Examples
    def add(a: int, b: int) -> int:
        return a + b

    def greet(name: str) -> str:
        return f"Hello, {name}"

    print(add(2, 3))                   # 5
    print(add.__annotations__)
    # {'a': <class 'int'>, 'b': <class 'int'>, 'return': <class 'int'>}

#%% Advanced Examples
    from typing import Optional, Union, Callable, Any

    # 1. Hints are NOT enforced
    print(add("a", "b"))               # ab  -> works, even though the hints say int

    # 2. Optional: a value or None
    def find_user(user_id: int) -> Optional[dict]:
        users = {1: {"name": "Amar"}}
        return users.get(user_id)       # dict, or None if not found

    # 3. Modern style (Python 3.9 and 3.10+)
    def first_item(items: list[int]) -> int | None:       # list[int] needs 3.9+, int | None needs 3.10+
        return items[0] if items else None

    # 4. Default values with hints
    def connect(host: str, port: int = 8080, secure: bool = False) -> str:
        return f"{host}:{port} secure={secure}"

    # 5. Collections
    def average(numbers: list[float]) -> float:
        return sum(numbers) / len(numbers)

    def count_words(words: list[str]) -> dict[str, int]:
        result: dict[str, int] = {}
        for w in words:
            result[w] = result.get(w, 0) + 1
        return result

    # 6. A function as an argument
    def apply(func: Callable[[int, int], int], x: int, y: int) -> int:
        return func(x, y)

    print(apply(lambda a, b: a + b, 2, 3))    # 5

    # 7. Functions that return nothing use None
    def log(message: str) -> None:
        print(message)

    # 8. *args and **kwargs hints
    def total(*numbers: int) -> int:
        return sum(numbers)

    def make_user(name: str, **extra: Any) -> dict[str, Any]:
        return {"name": name, **extra}

    # 9. Variable hints
    count: int = 0
    names: list[str] = []

    # 10. Read the hints at run time
    import inspect
    print(inspect.signature(connect))
    # (host: str, port: int = 8080, secure: bool = False) -> str

if __name__ == "__main__":
    main()
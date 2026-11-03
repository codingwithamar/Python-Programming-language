# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 4_ii_kwargs_Variable_Keyword_Arguments.py
# Path    : Python-Programming-Language/07_Functions_in_Python/00_Function_Arguments/4_ii_kwargs_Variable_Keyword_Arguments.py
# Subject : Function arguments in python
# Description : Variables length Arguments (Packing)- ii) **kwargs : Variable Keyword Arguments
# =============================================================================

def main():
#%% Basic Examples
    def show_profile(**details):
        print(type(details))              # <class 'dict'>
        for key, value in details.items():
            print(f"{key}: {value}")

    show_profile(name="Amar", age=25, city="Pune")

#%% Advanced Examples
    # Pass extra options straight through to another function
    def write_log(message, **print_options):
        print(f"[LOG] {message}", **print_options)

    write_log("Started")                        # [LOG] Started
    write_log("Done", end=" <<\n")              # [LOG] Done <<

    # Build an object from flexible data
    def make_user(name, **extra):
        user = {"name": name}
        user.update(extra)
        return user

    print(make_user("Amar", age=25, role="admin"))
    # {'name': 'Amar', 'age': 25, 'role': 'admin'}

if __name__ == "__main__":
    main()


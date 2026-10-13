# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 02_id_function.py
# Path    : Python-Programming-Language/07_Functions_in_Python/02_Function_Ctaegories/01_Built_in_functions/02_id_function.py
# Subject : Inspection Built-in-function in Python
# Description :  id() function : It used for get unique identity(Memory address)
# =============================================================================

def main():
#						        '2. id() function'
    print("\nExample 1")
# Example 1 : different variable and different value
    email_id_1 = 'codingwithamar@gmail.com'
    email_id_2 = 'akshaydorge1996@gmail.com'

    print(id(email_id_1))   #123530968719536
    print(id(email_id_2))   #123530968719616

    print(id(email_id_1) == id(email_id_2)) #false  (Not same)

    print("\nExample 2")
# Example 2 : Same Value but two different variables point him

    email_id_3 = 'bhandareamar404@gmail.com'
    email_id_4 = email_id_3

    print(email_id_3 == email_id_4)
# %% Example 3 : 
    print("\nExample 3")
    age = 21
    marks = 51
    number = 101

    # if we know the object then we can see their id/Memory address using -> id(object value) -> id(21)
    
    print("Age is :", age) 
    print("Type is : ", type(age)) 
    print("Address is : ", id(age)) 

    print("\nMarks is :", marks) 
    print("Type is : ", type(marks)) 
    print("Address is : ", id(marks)) 

    print("\nNo is :", number) 
    print("Type is : ", type(number)) 
    print("Address is : ", id(number)) 

    #update age = 21 to 30 and number = 101 to 151 now see the changes
    age = 51
    number = 151

    print("\nafter Updatation(age = 21 to 51 & number = 101 to 151") 
    print("age Address is : ", id(age))
    print("mark adddress is : ",id(marks))
    print("id and marks point same object : ",id(age) ==  id(marks))    # 51 value is available in marks varible so both memory address is same
    print("after update number object id is : ",id(number))   
    print("Here same value(object) not available so create new object")
    # Here we see After updation if object available in another then point to that location 
    # otherwise allocate new memory and here dynamically variable type can change


if __name__ == "__main__":
    main()
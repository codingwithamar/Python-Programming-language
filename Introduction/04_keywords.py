#This code created by codingwithamar@gmail.com
#path : python_system_programming/introduction/04_keywords.py
"""
Subject : Keywords in Python are reserved words with predefined meanings that form the syntax of the language. 
They cannot be used as identifiers, variable names, or function names. Python 3.x contains 35 keywords.
In this Code we try Program to Display Keywords
"""

print("Print A manual way")
print("False      await      else       import     pass\nNone       break      except     in         raise\nTrue       class      finally    is         return\nand        continue   for        lambda     try\nas         def        from       nonlocal   while\nassert     del        global     not        with\nasync      elif       if         or         yield\nmatch      case")

print("\nPrint A Logical way")
import keyword
print(keyword.kwlist)
print("Total Keyword : ", len(keyword.kwlist))
print("\n")

print("lets try Example of keywords")
x = 100
if x > 10:
    print("The value is Greater than 10\n")
else:
    print("The value is Smaller than 10\n")

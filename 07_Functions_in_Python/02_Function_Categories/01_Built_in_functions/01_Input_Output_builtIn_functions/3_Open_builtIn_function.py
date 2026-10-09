# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 3_Open_builtIn_function.py
# Path    : Python-Programming-Language/07_Functions_in_Python/02_Function_Ctaegories/01_Built_in_functions/01_Input_Output_builtIn_functions/3_Open_builtIn_function.py
# Subject : Built-In function
# Description : open() : Opens a file and returns a file object, used for reading or writing files.
# =============================================================================

def main():
    #________________________________________________________________________________
    #						'Syntax & Definition'
    print("Opens a file and returns a file object, used for reading or writing files.")
    print("open(file, mode='r', encoding=None)")
    print("""
    Mode	    Meaning
    "r"	        Read (default) — file must exist
    "w"	        Write — creates file, overwrites if it exists
    "a"	        Append — adds to the end of the file
    "x"	        Create — fails if file already exists
    "rb"/"wb"	Same as above, but in binary mode
    "r+"	    Read and write
    """)
    #________________________________________________________________________________
    print("_"*150)
    #%%________________________________________________________________________________
    #						'Basic Example & Use'
    #   Write a text inside a file
    with open("notes.txt","w") as f:
        f.write("This is the text file inside data")
    f.close()
    
    #   Read a file data
    with open("notes.txt","r") as f:
        fileData = f.read()
        print(fileData)
    f.close()

    with open("notes.txt","a") as f:
        f.write(" New entry write inside file")
    f.close()

    with open("notes.txt","r+") as f:
        file_content = f.read()
        print(file_content)     # cursor now at end of file
        f.write(" added this line")     # written at the end, since cursor was there
        f.seek(0)   # curser point reset
        new_content = f.read()
        print(new_content)
        f.close()

    try:
        with open("notes.txt","x") as f:
            f.write("this is new file")
            f.close()
    except FileExistsError:
        print("File is already exist so not overwrite content")

    # Copying an image file byte-for-byte
    try:
        with open("photo.jpg", "rb") as source:
            data = source.read()

        with open("photo_copy.jpg", "wb") as dest:
            dest.write(data)
            print("photo_copy.jpg created successfully")
    except FileNotFoundError:
        print("photo.jpg - File not found inside path")
    #________________________________________________________________________________
    
if __name__ == "__main__":
    main()
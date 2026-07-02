# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : 06_binary_data_types.py
# Path    : 02_Data_Types\06_binary_data_types.py
# Subject : Bytes and Bytearray
# Description : The bytes data type represents an immutable sequence of bytes, 
# mostly used to represent raw binary data
# =============================================================================
def heading(title):
    print("\n" + "=" * 70)
    print(f" {title}")
    print("=" * 70)
#=========================================================================================
def main():
#=========================================================================================
    heading("Creation Of Bytes")
    data = bytes([65,66,67])        #Way 1
    print(data)                     #b'ABC'

    data = b"Python"                #Way 2
    print(data)                     #b'Python'

    b = b'Sumaney'                    # literal
    ByteData1 = bytes([104,101,108,108,111])    # from list of ints (0-255)
    ByteData2 = bytes(5)                        # b'\x00\x00\x00\x00\x00' — zero-filled
    ByteData3 = bytes('hi', 'utf-8')            # from str + encoding

#=========================================================================================
    heading("Accessing Bytes")
    data = b"ABC"
    print(data[0])      #65
    #It returns Integer Not Character
    #pratyek integer 0-255 range madhla ASCII code point ahe (104='h', 101='e', 108='l', 108='l', 111='o'). 
    #Python te sagle integers ekatra ek immutable bytes object madhe convert karto, 
    #ani display kartana printable characters asतील tar b'hello' sarkhe show karto.
    print(b)            #b'Sumaney'
    print(ByteData1)    #b'hello'
    print(ByteData2)    #b'\x00\x00\x00\x00\x00'
    print(ByteData3)    #b'hi'

    print(ByteData1)              # b'hello'
    print(type(ByteData1))        # <class 'bytes'>
    print(list(ByteData1))        # [104, 101, 108, 108, 111]
    print(ByteData1.decode('utf-8'))  # hello

#=========================================================================================
    heading("Immutability - Cannot Modify Bytes")
    data = b"ABC"
    #data[0] = 90        #TypeError

#=========================================================================================
    heading("BYTEARRAY : Edit Binary Data")
    buffer = bytearray(b"Hello")
    print("Before Modified is : ", buffer)      #Before Modified is :  bytearray(b'Hello')
    buffer[0] = ord("Y")
    print("After Modified is : ", buffer)       #After Modified is :  bytearray(b'Yello')

#=========================================================================================
    heading("MEMORYVIEW")
    buffer1 = bytearray(b"Python")
    view = memoryview(buffer1)
    view[0] = ord("C")
    print(buffer1)                 #bytearray(b'Cython')
#=========================================================================================
if __name__ == "__main__":
    main()
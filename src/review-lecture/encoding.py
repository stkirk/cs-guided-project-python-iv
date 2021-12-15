# ASCII standard made a table that turned characters to numbers
char = 'a'
# ord gives ascii value
print(ord(char)) # 97
# chr converts ascii value to character
print(chr(97)) # a

string = 'abcd'
print(list(string.encode())) #--> ascii value in a list

# print using unicode values and hexidecimals
print(chr(0x41)) # A
print(chr(0x028D)) # weird M
print(chr(0x1F60E)) # emoji

# if the ascii value is in binary how does the computer distinguish it from the number?
# Given an ASCII encoded binary string...
# return the decoded text as a human readable string
# every 8 bits in a binary string represents one character in the ascii table

def binaryStrConverter(binary):
    # return out if binary is an empty string
    # if binary == "":
    #     return ""
    # create an array to append to
    binary_char_lst = []
    # loop through binary appending to the array in 8 character length segments, using step argument in range to create a sliding window to slice
    for i in range(0, len(binary), 8):
        # convert each 8 bit segment to a base 2 int, then use chr() to find the corresponding ascii character
        binary_char_lst.append(chr(int(binary[i:i + 8], 2)))
    # join the list and return
    return ''.join(binary_char_lst)


    # loop over the new list and convert each 8 bit index to its corresponding character using the ascii table
    # join the list back into a human readable string and return

print(binaryStrConverter("011011000110000101101101011000100110010001100001")) #--> "lambda"
print(binaryStrConverter("")) #--> "" 

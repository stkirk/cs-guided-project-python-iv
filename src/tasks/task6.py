# Given a decimal integer...
# transform it to binary and reverse the bits
# return the result as a decimal integer

# Example: 417==110100001--reverse-->100001011==267
def reverseBinaryInt(n):
    # transform n from integer to binary string and reverse it
    binary_str_reversed = bin(n)[::-1]
    # chop off last two chars, always 'b0'
    binary_str_reversed_no_b0 = binary_str_reversed[:len(binary_str_reversed) - 2]
    # convert back to decimal int, second arg signifies base 2
    return int(binary_str_reversed_no_b0, 2)


print(reverseBinaryInt(417)) #--> 267
print(reverseBinaryInt(267)) #--> 417
print(reverseBinaryInt(0)) #--> 0
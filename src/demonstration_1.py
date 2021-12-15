"""
Given a string, implement a function that returns the string with all lowercase
characters.

Example 1:

Input: "LambdaSchool"
Output: "lambdaschool"

Example 2:

Input: "austen"
Output: "austen"

Example 3:

Input: "LLAMA"
Output: "llama"

*Note: You must implement the function without using the built-in method on
string objects in Python. Think about how character encoding works and explore
if there is a mathematical approach that you can take.*
"""
# recreate the lower() class method
def to_lower_case(string):
    output_str = ""
    for letter in string:
        # if letter falls in uppercase range
        if ord(letter) > 64 and ord(letter) < 91:
            # letter is uppercase, convert it to lower case
            # upper and lowercase versions of letter separated by 32
            lower = ord(letter) + 32
            output_str += chr(lower)
        else:
            output_str += letter
    return output_str


print(to_lower_case("Lambda   -   School!!!"))
print(to_lower_case("austen"))
print(to_lower_case("LLAMA"))

def one_line_lower(string):
    return  "".join([chr(ord(letter) + 32) if ord(letter) > 64 and ord(letter) < 91 else letter for letter in string])

print(one_line_lower("Lambda   -   School!!!"))

def to_lower_case_josh(string):
    #convert the string to a list of ascii codes
    char_lst = [ord(char) for char in string]

    # loop through for each character in the string
    for (i, ascii_code) in enumerate(char_lst):
        # if ascii_code falls in uppercase range (ascii 65-90 inclusive)
        if ascii_code >= 65 and ascii_code <= 90:
            # upper and lowercase versions of ascii_code separated by 32
            # add 32 to  go from uppercase to lowercase
            char_lst[i] = ascii_code + 32
        # Otherwise, do nothing
    # convert the updated list of ascii codes back to a new string and return
    new_chars = [chr(ascii_code) for ascii_code in char_lst]
    return ''.join(new_chars)


print(to_lower_case_josh("Lambda   -   School!!!"))
print(to_lower_case_josh("austen"))
print(to_lower_case_josh("LLAMA"))

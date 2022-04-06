# 1. Split in Half:
# Given a string. Split it into two equal parts. Swap these parts and return the result.
# If the string has odd characters, the first part should be one character greater than the second part.
# Example: string = 'bbbbbcaaaaa'. Result = ‘aaaaabbbbbc’

def swap(str):
    length = len(str)
    if length % 2 != 0:
        str1 = str[:(length//2)+1]
        str2 = str[(length//2)+1:]
        return str2+str1
    else:
        str1 = str[:(length//2)]
        str2 = str[(length//2):]
        return str2+str1

print(swap('bbbbbcaaaaa'))
print(swap('bbbbdaaaa'))
print(swap('apc'))

# 2. Unique Characters in String:
# Given a string, determine if it consists of all unique characters.
# For example, the string 'abcde' has all unique characters and should return True.
# The string 'aabcde' contains duplicate characters and should return False.
# Hint: https://www.w3schools.com/python/python_sets.asp

def unique_characters(str):
    if str.isnumeric():
        return "Invalid Input"
    if str == "":
        return None
    else:
        for letter in str:
            if str.count(letter) != 1:
                return False
        return True


print(unique_characters('abcde'))
print(unique_characters('aabcde'))
print(unique_characters(""))
print(unique_characters('0987654321'))
# 1. Reverse a Statement:
# Build an algorithm that will print the given statement in reverse.
# Example: Initial string = Everything is hard before it is easy
# Reversed string = easy is it before hard is Everything
def reverse_word(s, start, end):
    while start < end:
        s[start], s[end] = s[end], s[start]
        start = start + 1
        end -= 1

s = "Everything is hard before it is easy"

s = list(s)
start = 0
while True:

    try:
        end = s.index(' ', start)
        reverse_word(s, start, end - 1)
        start = end + 1

    except ValueError:
        reverse_word(s, start, len(s) - 1)
        break
s.reverse()
s = "".join(s)
print(s)

# 2. Permutations:
# Write a solution that will print all permutations of a string.
# A permutation is an act of changing the arrangement of characters.
# Example: String = ABC, Return {ABC, ACB, BAC, BCA, CBA, CAB}

def toString(List):
    return ''.join(List)

def permute(a, l, r):
    if l == r:
        print(toString(a))
    else:
        for i in range(l, r + 1):
            a[l], a[i] = a[i], a[l]
            permute(a, l + 1, r)
            a[l], a[i] = a[i], a[l]


string = "ABC"
n = len(string)
a = list(string)
permute(a, 0, n - 1)

# 3. Count Characters:
# Create a program that will count vowels and consonants in a string.
# Example: String = “hello world”, Return {Vowels: 3, Consonants: 7}

str1 = input("Enter String helloworld:")
vowels = 0
consonants = 0

for i in str1:
    if (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'
            or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U'):
        vowels = vowels + 1
    else:
        consonants = consonants + 1

print("Total Number of Vowels in this String = ", vowels)
print("Total Number of Consonants in this String = ", consonants)
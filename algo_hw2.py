import math
#1: Compute the sum of digits in all numbers from 1 to n.
# When a user enters a number n, find the sum of digits in all numbers from 1 to n.
#Example: n = 5. Result = 1 + 2 + 3 + 4 + 5 = 15
def sum(n):
    s_result = (n * (n + 1)) / 2
    return s_result


number = int(input('Input a number: '))
print(sum(number))


#2: Find max number from 3 values, entered manually from a keyboard.
#Example: 124, 21, 32. Result = 124.
def find_max_num(n1, n2, n3):
    if n1 > n2 and n1 > n3:
        return n1
    if n2 > n1 and n2 > n3:
        return n2
    return n3


n1 = int(input('Input val1: '))
n2 = int(input('Input val2: '))
n3 = int(input('Input val3: '))

print(find_max_num(n1, n2, n3))


#3: Count odd and even numbers. Count odd and even digits of the whole number.
#Example: entered number is 34560, then 3 digits will be even (4, 6, and 0) and 2 odd digits (3 and 5).
def count_even_odd(n):
    even = 0
    odd = 0

    while n != 0:
        current_digit = n % 10
        if current_digit % 2:
            odd += 1
        else:
            even += 1
        n = n // 10

    return ["Evens: " + str(even), "Odds: " + str(odd)]


number = int(input('Enter a number: '))
print(count_even_odd(number))

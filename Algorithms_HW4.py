import math
# 1. Even First:
# Your input is an array of integers, and you have to reorder its entries so that the even entries appear first.
# You are required to solve it without allocating additional storage (operate with the input array).
# Example: [7, 3, 5, 6, 4, 10, 3, 2] Return [6, 4, 10, 2, 7, 3, 5, 3]
def even_odd(arr):
    even, odd = 0, len(arr) - 1
    while even < odd:
        if arr[even] % 2 == 0:
            even += 1
        else:
            arr[even], arr[odd] = arr[odd], arr[even]
            odd -= 1

    return arr


test_arr = [7, 3, 5, 6, 4, 10, 3, 2]
print(even_odd(test_arr))

# 2. Increment a Number:
# Write a program that takes as input an array of digits encoding a non-negative decimal integer D
# And updates the array to represent the integer D + 1.
# For example, if the input is [1, 2, 9] then you should update the array to [1, 3, 0].


def increment(a):
    n = len(a)

    a[n - 1] += 1
    carry = a[n - 1] / 10
    a[n - 1] = a[n - 1] % 10

    for i in range(n - 2, -1, -1):
        if (carry == 1):
            a[i] += 1
            carry = a[i] / 10
            a[i] = a[i] % 10

    if (carry == 1):
        a.insert(0, 1)

z = [1, 2, 9]

increment(z)

for i in range(0, len(z)):
    print(z[i], end=" ")
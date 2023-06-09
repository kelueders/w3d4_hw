# How many even digits?
# Given an array of integers, return how many of them contain an even number of digits.

# Example 1:
# Input: nums = [12,345,2,6,7896]
# Output: 2
# Explanation:
# 12 contains 2 digits (even number of digits).
# 345 contains 3 digits (odd number of digits).
# 2 contains 1 digit (odd number of digits).
# 6 contains 1 digit (odd number of digits).
# 7896 contains 4 digits (even number of digits).
# Therefore only 12 and 7896 contain an even number of digits.

# Example 2:
# Input: nums = [555,901,482,1771]
# Output: 1
# Explanation:
# Only 1771 contains an even number of digits


# for loop to access each integer in the arry
# find the length of each integer in the array
# do an if statement  num % 2 == 0 to determine if the length is even
# do a counter to determine how many in the array have even number of digits

def even_digits(arr):
    counter = 0
    for num in arr:
        str_num = str(num)
        if len(str_num) % 2 == 0:
            counter += 1
    return counter

print(even_digits([12,345,2,6,7896]))
print(even_digits([555,901,482,1771]))

print(float("inf"))




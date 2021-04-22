"""
Project Euler Problem 4
=======================

A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""


def is_palindrome(n):
    digits = str(n)
    num_digits = len(digits)
    for i in range(0, int(num_digits / 2)):
        if digits[i] != digits[num_digits - 1 - i]:
            return False
    return True


def largest_palindrome(n):
    largest_num = 0
    for i in range(pow(10, n), 0, -1):
        for j in range(pow(10, n)):
            num = i * j
            if is_palindrome(num):
                if num > largest_num:
                    largest_num = num
    return largest_num


print(largest_palindrome(3))

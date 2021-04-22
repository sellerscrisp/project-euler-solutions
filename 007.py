"""
Project Euler Problem 7
=======================

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
that the 6th prime is 13.

What is the 10001st prime number?
"""


import math


def is_prime(n):
    if n == 1:
        return False
    if n < 4:
        return True
    if n % 2 == 0:
        return False
    if n < 9:
        return True
    for d in range(3, math.floor(math.sqrt(n))+1):
        if n % d == 0:
            return False
    return True


counter = 1
solution = 1
while counter < 10001:
    solution += 2
    if is_prime(solution):
        counter += 1

print(solution)

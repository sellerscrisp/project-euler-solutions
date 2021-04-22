"""
Project Euler Problem 3
=======================

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""


import math


def main(n):
    factors = []

    for i in range(2, math.ceil(math.sqrt(n))):
        while n % i == 0:
            factors.append(i)
            n = n / i

    return factors[-1]


print(main(600851475143))

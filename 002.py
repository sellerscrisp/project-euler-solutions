"""
Project Euler Problem 2
=======================

Each new term in the Fibonacci sequence is generated by adding the
previous two terms. By starting with 1 and 2, the first 10 terms will be:

                  1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

Find the sum of all the even-valued terms in the sequence which do not
exceed four million.
"""


def main(n):
    term = [None] * n
    term[0] = 1
    term[1] = 2
    total = 2

    for i in range(2, n):
        term[i] = term[i - 1] + term[i - 2]
        if (term[i] % 2 == 0):
            total += term[i]

    if (term[n - 1] < 4000000):
        total = main(n + 1)
    return total


print(main(20))
"""
Project Euler Problem 1
=======================

If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

def factor(f, n):
    t = (n-1)/f
    return f * (t * (t+1))/2

def p1(n):
    return factor(3, n) + factor(5, n) - factor(15, n)

if __name__ == '__main__':
    print(p1(1000))

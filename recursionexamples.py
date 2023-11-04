# recursion code
def fact(n):
    start = 1
    if n == 0:
        return 1
    else:
        for i in range(1, n + 1):
            start *= i
        return start


def factorial(n):
    # We make sure that n is a positive integer or 0.
    if n >= 1:
        return n * fact(n - 1)
    else:
        return 1


print(factorial(20))


def fib(n):
    b = [1, 1]
    start = 0
    stuff = 1
    for i in range(n - 1):
        b.append(b[start] + b[stuff])
        start += 1
        stuff += 1
    return b[-1]


def fibb(n):
    if n >= 3:
        return fibb(n - 1) + fibb(n - 2)
    else:
        return 1


print(fibb(20))
fib(19)  # for 20 we use 19 since list indexing starts from zero.

# Dynamic programming
"""
It involves three steps --:
   1.recursion.
   2.store (memoize).
   3.Bottom-up approach if you don't like recursion.

"""


# fibocacci memoized solution
def fib(n, memo):
    if memo[n] is not None:
        return memo[[n]]
    if n < 3:
        result = 1
    else:
        result = fib(n - 1) + fib(n - 2)
    memo[n] = result
    return result

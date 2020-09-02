# 0 1 1 2 5 8 13 21
# Top-Down Dynamic Programming

cache = {}


def fib(n):
    if n <= 1:
        return n

    if n not in cache:
        cache[n] = fib(n-1) + fib(n-2)

    return cache[n]


for i in range(100):
    print(fib(i))


"""
Bonus:
    Bottom-Up Dynamic Programming
    Solves fib 0(1) space

"""

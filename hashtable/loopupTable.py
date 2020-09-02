# Lookup Table
# for repetitive expensive calculations

import math

"""Build a lookup table for inverse square root for numbers 1 - 1000"""
inv_sqrt_table = {}


def inv_sqrt(n):
    if n not in inv_sqrt_table:
        inv_sqrt_table[n] = 1/math.sqrt(n)
    return 1 / math.sqrt(n)


def build_lookup_table():
    for i in range(1, 1001):
        inv_sqrt_table[i] = inv_sqrt(i)


# build_lookup_table()

# print(inv_sqrt_table[10])
# print(inv_sqrt_table[37])
print(inv_sqrt(1000000000))

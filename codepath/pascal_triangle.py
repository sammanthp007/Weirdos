# The rth column of nth row of the Pascal's Triangle is
# (n!)/ (r! * (n-r)!. Note that the value of n starts from 0 and nth row has
# (n + 1) entries, i.e., 0 <= r <= n

# Complete the function pascalTriangle, that has one parameter - an integer k.
# The funtion should print first k rows of Pascal's Triangle, and the entries
# of a row must be printed separated by space.

# e.g
"""
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
1 5 10 5 1
1 6 15 20 15 6 1
...
"""


def factorial(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    return factorial(n - 1) * n


def pascalTriangle(k):
    for r in range(0, k):
        for c in range(0, r + 1):
            item_nume = factorial(r)
            item_deno = factorial(c) * factorial(r - c)
            item = int(item_nume / item_deno)
            print(item, end=" ")
        print()

pascalTriangle(7)

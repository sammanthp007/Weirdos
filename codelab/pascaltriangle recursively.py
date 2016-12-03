# The rth column of nth row of the pascal's Triangle is n! / (r! * (n - r))!).
# Note that the value of n starts from 0 and the nth row has (n + 1) entries
# i.e 0 <= r <= n

#Complete the function pascalTriangle that has one parameter-an integer k.
#The function should print first k rows of pascal's triangle, and the entries
#of a row must be pointed separated by space.
factorial_map = {0: 1, 1: 1}

def pascalTriangle(k):
    print_pascal_triangle(0, 0, k - 1)

def print_pascal_triangle(row, col, max_row):
    if max_row < row:
        return

    if col > row:
        print()
        print_pascal_triangle(row + 1, 0, max_row)
        return

    numo = factorial(row)
    deno = (factorial(col) * factorial(row - col))

    print (int(numo / deno), end = ' ')
    print_pascal_triangle(row, col + 1, max_row)

def factorial(num):
    if num in factorial_map:
        return factorial_map.get(num)

    nn = factorial(num - 1) * num

    factorial_map[num] = nn
    return nn

k = 8
pascalTriangle(k)

input_n = int(input().strip())

def factorial(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    return n * factorial(n - 1)

print (factorial(input_n))
# Write a program that finds the nth fibonacci number

def get_nth_fibonacci_number(n):
    fibo_number = {1:1, 2:1}
    if (n in fibo_number):
        return fibo_number.get(n)
    for i in range(3, n + 1):
        fibo_number[i] = fibo_number.get(i - 1) + fibo_number.get(i - 2)

    return fibo_number[n]

n = 6
print (get_nth_fibonacci_number(n))


# space optimize the above solution since we only need the most recent two
# to get to the next fibonacci number

def space_optimized_get_fibo_number(n):
    a = 1
    b = 1
    for num in range(3, n + 1):
        c = a + b
        a = b
        b = c
    return c

m = 6
print(space_optimized_get_fibo_number(m))

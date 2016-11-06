"""
Given a string, S, of length N that is indexed from 0 to N -1, print its even-indexed and odd-indexed characters as  2 space-separated strings on a single line (see the Sample below for more detail).
"""


num_test_cases = int(input())

for i in range(num_test_cases):
    odd = ''
    even = ''
    current = input()
    
    for j in range(len(current)):
        if j % 2 == 0:
            even += current[j]
            continue
        else:
            odd += current[j]
    
    print(even + ' ' + odd)
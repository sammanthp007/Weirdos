"""
Print a single base-10 integer denoting the maximum number of consecutive 1's in the binary representation of n
"""


#!/bin/python3

import sys


n = int(input().strip())


bin_num = str(bin(n))[2:]

def find_consequtive(string, char_pattern):
    p = char_pattern
    s = string
    max_repetition = 0
    count = 0
    for i in string:
        if i == p:
            count += 1
            if count > max_repetition:
                max_repetition = count
        else:
            count = 0
            
    return max_repetition

print(find_consequtive(bin_num, '1'))
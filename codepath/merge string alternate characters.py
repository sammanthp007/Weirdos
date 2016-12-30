#!/bin/python3

import sys
import os


# Complete the function below.


def  mergeStrings(a, b):
    len_a = len(a)
    len_b = len(b)
    a_ptr = 0
    b_ptr = 0
    merged_string = ""
    turn = 0
    while True:
        if a_ptr == len_a and b_ptr == len_b:
            return merged_string
        if a_ptr == len_a:
            merged_string = merged_string + b[b_ptr]
            b_ptr += 1
        elif b_ptr == len_b:
            merged_string = merged_string + a[a_ptr]
            a_ptr += 1
        else:
            if turn == 0:
                merged_string = merged_string + a[a_ptr]
                a_ptr += 1
                turn = 1
            elif turn == 1:
                merged_string = merged_string + b[b_ptr]
                b_ptr += 1
                turn = 0

f = open(os.environ['OUTPUT_PATH'], 'w')
    

_a = str(input())


_b = str(input())

res = mergeStrings(_a, _b);
f.write(res + "\n")

f.close()
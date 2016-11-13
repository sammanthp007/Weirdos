#!/bin/python

import sys


a,b,c,d,e = input().strip().split(' ')
a,b,c,d,e = [int(a),int(b),int(c),int(d),int(e)]

max_sum = float('-inf')
min_sum = float('inf')

lis = [a,b,c,d,e]

for i in lis:
    current_sum = sum(lis) - i
    if current_sum > max_sum:
        max_sum = current_sum
    if current_sum < min_sum:
        min_sum = current_sum
print (min_sum, max_sum)

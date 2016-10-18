#!/bin/python3

import sys


x1,v1,x2,v2 = input().strip().split(' ')
x1,v1,x2,v2 = [int(x1),int(v1),int(x2),int(v2)]

def willLand(x1, v1, x2, v2):
    if x1 > x2:
        small_pos = x2
        small_rate = v2
        large_pos = x1
        large_rate = v1
    elif x1 < x2:
        small_pos = x1
        small_rate = v1
        large_pos = x2
        large_rate = v2
    else:
        return "YES"
    
    if large_rate >= small_rate:
        return "NO"
    while small_pos <= large_pos:
        if small_pos == large_pos:
            return "YES"
        small_pos += small_rate
        large_pos += large_rate
    return "NO"

print (willLand(x1, v1, x2, v2))
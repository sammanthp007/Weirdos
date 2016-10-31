#!/bin/python3

import sys


N = int(input().strip())

def is_weird(n):
    if n % 2 != 0:
        return "Weird"
    elif 2 <= n <= 5:
        return "Not Weird"
    elif 6 <= n <= 20:
        return "Weird"
    else:
        return "Not Weird"
    
print (is_weird(N))

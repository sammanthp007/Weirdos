#!/bin/python3

import sys


n = int(input().strip())

for i in range(1, 11):
    print (("{:d} x {:d} = {:d}").format(n, i, n*i))
    

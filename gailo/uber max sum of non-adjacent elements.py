# Given an array of integers, find the maximum sum of non-adjacent elements

# Analysis
"""
[2,3,4,5,6,7]
= 5 + 7

Just the two largest number.
"""

# Approach 1:
# Sort the array and get the two highest adjacent numbers (Will not work)

# Analysis
"""
for the stock market problem:
    [2,4,2,5,6,4,7,7,4,6]
    create a array for changes
    then find the maximum subarray
"""






# Approach 2:
# Create a list of changes`

def get_max_sum_of_non_adjacent_elements(lis, start, end, max_sum):
    if start < end:
        return lis

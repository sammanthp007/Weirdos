# Given an array of stock prices, give the best price to buy stocks

# Approach:
"""
[2,5,7,2,3,5,3,2,6,3,8,4,3,2]

Approach 1: 
Create a pair of all values such that the buy date preceeds the sell 
date.
Find the pair that has the highest deference
"""

"""
Approcah 2:
Create a list of changes
Find the subarray with the max change
"""
def get_max_subarray(lis, start, last, gain):
    if last < start:
        return 0, 0, 0

    if last == start:
        if lis[start] > gain:
            gain = lis[start]
        return start, last, gain
    else:
        mid = (start + last) // 2
        max_from_left = get_max_subarray(lis, start, mid, gain)
        max_from_right = get_max_subarray(lis, mid, last, gain)
        max_from_between = get_max_sum(lis, start, last, gain)
        sol = (max_from_left, max_from_right, max_from_between)
        max_gain = max(sol)
        for i in sol:
            if i[2] == max_gain:
                if max_gain > gain:
                    gain = max_gain
                return i[0], i[1], gain

def get_max_sum(lis, start, last, gain):
    total_sum = 0
    while start <= last:
        total_sum += lis[start]
    return total_sum


def get_best_time_to_buy_stocks(lis):
    if len(lis) == 1:
        return lis
    changes = []

    for i in range(1, len(lis)):
        changes.append(lis[i] - lis[i - 1])
    gain = float("-inf")
    bday, sday, gain = get_max_subarray(changes, 0, len(changes) - 1, gain)
    return (bday, sday, gain)


lis = [2,3,4,1,3,5]
best_time = get_best_time_to_buy_stocks(lis)

print ("The best time to buy stock is", end = " ")
print ("buy on: ", best_time[0], end=" ")
print ("and sell on: ", best_time[1], end = " ")
print ("and get profit of: ", best_time[2])






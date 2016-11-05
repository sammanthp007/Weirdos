def find_max_crossing_subarray(A, low, mid, high):
    max_sum = 0
    highest_left = float('-inf')
    temp_sum = 0
    max_left = mid
    for i in range(mid, low - 1, -1):
        temp_sum += A[i]
        if temp_sum > highest_left:
            highest_left = temp_sum
            max_left = i

    max_right = mid + 1
    highest_right = float('-inf')
    temp_sum = 0
    for i in range(mid + 1, high + 1):
        temp_sum += A[i]
        if temp_sum > highest_right:
            highest_right = temp_sum
            max_right = i

    return (max_left, max_right, highest_left + highest_right)

def find_maximum_subarray(A):
    return find_maximum_recur(A, 0, len(A) - 1)

def find_maximum_recur(A, low, high):
    if high < low:
        return 0, 0, 0
    if low == high:
        return low, high, A[low]
    mid = (high + low) // 2
    lowest_left, highest_left, max_of_left = find_maximum_recur(A, low, mid)
    lowest_right, highest_right, max_of_right = find_maximum_recur(A, mid + 1, high)
    lowest_cross, highest_cross, max_of_cross = find_max_crossing_subarray(A, low, mid, high)
    if (max_of_left >= max_of_right and max_of_left >= max_of_cross):
        return lowest_left, highest_left, max_of_left
    elif  max_of_right >= max_of_left and max_of_right >= max_of_cross:
        return lowest_right, highest_right, max_of_right
    else:
        return lowest_cross, highest_cross, max_of_cross


A = [13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]
A = []
print(find_maximum_subarray(A))

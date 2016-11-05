def find_max_crossing_subarray(A, low, mid, high):
    max_sum = 0
    highest_left = float(-inf)
    temp_sum = 0
    for i in range(mid, low - 1, -1):
        temp_sum += A[i]
        if temp_sum > highest_left:
            highest_left = temp_sum
            max_left = i

    highest_right = float(-inf)
    temp_sum = 0
    for i in range(mid + 1, high + 1):
        temp_sum += A[i]
        if temp_sum > highest_right:
            highest_right = temp_sum
            max_right = i

    return (max_left, max_right, highest_left + highest_right)

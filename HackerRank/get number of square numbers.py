def  getMinimumUniqueSum(arr):
    final_arr = []
    for each_range in arr:
        list_range = each_range.split(" ")
        num_of_square_num = get_num_of_square(int(list_range[0]), int(list_range[1]))
        final_arr.append(num_of_square_num)
    return final_arr

def get_num_of_square(a, b):
    num_of_squares = 0
    square_root = 0
    num = a
    # get first square root
    while num <= b:
        if is_square(num):
            square_root = int(num ** 0.5)
            break
        num += 1
    if square_root != 0:
        while square_root ** 2 <= b:
            num_of_squares += 1
            square_root += 1
    return num_of_squares
    


def is_square(a):
    if a <= 0:
        return False
    return (int(a ** 0.5) ** 2 == a)

print (getMinimumUniqueSum(['1 20', '']))

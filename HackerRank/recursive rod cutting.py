def recursive_rod_cutting(rod_length, price_list):
    if rod_length == 0:
        return 0
    max_price = float('-inf')
    for i in range(rod_length):
        max_price = max(max_price, price_list[i] + recursive_rod_cutting(rod_length - i - 1, price_list))
    return max_price

price_lis = [1,5,8,9,10,17,17,20,24,30]
size = 5

print(recursive_rod_cutting(size, price_lis))

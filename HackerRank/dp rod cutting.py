def best_rod_price(price_list, rod_length):
    best_price_memo = {0:0}
    for i in range(1, rod_length + 1):
        max_val = float('-inf')
        for j in range(1, i + 1):
            max_val = max(max_val, price_list[j] + best_price_memo.get(i - j))
        best_price_memo[i] = max_val
    return best_price_memo.get(rod_length)

price_list = [0,1,5,8,9,10,17,17,20,24,30]
rod_length = 5

print(best_rod_price(price_list, rod_length))

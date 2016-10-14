def  lonelyInteger( arr):
    dicti = {}
    for num in arr:
        dicti[num] = dicti.get(num, 0) + 1
    for k, v in dicti.items():
        if v == 1:
            return k
    return None

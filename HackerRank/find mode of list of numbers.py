lis = [ 3, 5, 9, -1, -4, -3]
lis = []
lis = [1,1,1,1,1,1,1,1,1,1]
lis = [2]
lis = [-4, -3, -3, -3, -1, -1, 3, 5, 5, 9]



def get_mode(nxt, mode_val, mode_amt, dict):
    dic_of_freq = {}
    mode = None
    max_cout = 0
    # populate the dict with freq
    for each_item in lis:
        current_count = dic_of_freq.get(each_item, 0) + 1
        dic_of_freq[each_item] = current_count
        if current_count > max_count:
            mode = each_item 
    
    return mode
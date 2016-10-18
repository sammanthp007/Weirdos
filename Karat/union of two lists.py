
# Your previous Markdown content is preserved below:

# Suppose we are writing the backend for a search engine. The search fetches sorted lists of IDs (ints) representing the search results. Given two sorted lists of ints, return their union as a sorted list without duplicates.

# Inputs:
# list1 = [1, 3, 3, 5, 9] len = 5; l = 1
# list2 = [1, 2, 3, 4, 4, 6, 7] len = 7; m = 2

# last_output_list = 2

# output_list= [1, 2]

# Output:
# [1, 2, 3, 4, 5, 6, 7]

def get_union(lis1, lis2):
    l = 0
    m = 0
    output_list = []
    if (len(lis1) == 0 and len(list2) == 0):
        return []
    if (len(lis1) == 0):
        output = []
        add_remaining(lis2, output, m)
        return output
        
    if len(lis2) == 0:
        output = []
        add_remaining(lis1, output, l)
        return output
    
    while (l < len(lis1) and m < len(lis2)):
        if len(output_list) == 0:
            last_output_list = None
            print "came here"
        else:
            last_output_list = output_list[-1]
        print l, m
        min_val = min(lis1[l], lis2[m])
        if lis1[l] == min_val:
            if last_output_list != lis1[l]:
                output_list.append(lis1[l])
            l += 1
        else:
            if last_output_list != lis2[m]:
                output_list.append(lis2[m])
            m += 1
        last_output_list = output_list[-1]
        
        # if (lis1[l] < lis2[m] and lis1[l] != last_output_list):
        #     output_list.append(lis1[l])
        #     l += 1
        # elif (lis1[l] > lis2[m] and lis2[m] != last_output_list):
        #     output_list.append(list2[m])
        #     m += 1
        # elif (lis1[l] == lis2[m] and lis1[l] != last_output_list):
        #     output_list.append(lis2[m])
        #     m += 1
        #     l += 1

    add_remaining(lis1, output_list, l)
    add_remaining(lis2, output_list, m)
        
    return output_list
        
def add_remaining(lis1, output, i):
    while (i < len(lis1)):
        if len(output) == 0:
            last_num = None
        else:
            last_num = output[-1]
        if (lis1[i] != last_num):
            output.append(lis1[i])
        i += 1
            
            
list1 = []
list2 = []
        
    
print (get_union(list1, list2))

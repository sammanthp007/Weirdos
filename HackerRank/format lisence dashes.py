# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

# Test Cases:
# ('2dE', 4)
# ('se334sdsvdred', 3)
# ('d', 2)
# ('45f3fsaf-dfgdf-ggdf-----dftdfg4', 4)
# ('3-', 3)
# ('TESTCASE', 1)
# ('hh', 1)
# ('6', 1)


# Algorithm
# iterate from behind
# keep record of if the group is the first or not
# if first group then it is ok to have length less than the size of the group
# if dashes then remove
# keep record of the dash
# add dashes if length of the group is greater than the max_length



def solution(S, K):
    # write your code in Python 2.7
    formatted_lisence = ""
    current_group_size = 0
    for i in range(len(S) - 1, -1, -1):
        if S[i] == "-":
            continue
        if current_group_size == K:
            formatted_lisence = S[i].upper() + "-" + formatted_lisence
            current_group_size = 1
        else:
            formatted_lisence = S[i].upper() + formatted_lisence
            current_group_size += 1
    return formatted_lisence
        
#!/bin/python3

import sys
import os

# Complete the function below.

def  electionWinner(votes):
    if len(votes) == 0:
        return None
    vote_count = {}
    max_vote = 0
    for candidate in votes:
        candidate_vote = vote_count.get(candidate, 0)
        vote_count[candidate] = candidate_vote + 1
        if vote_count[candidate] > max_vote:
            max_vote = vote_count[candidate]
    
    winner = ""
    for c in vote_count:
        if vote_count[c] == max_vote:
            if winner < c:
                winner = c
    return winner
        
        
# f = open(os.environ['OUTPUT_PATH'], 'w')
lis = ["AA", "AA", "AA"]
print (electionWinner(lis))

# _votes_cnt = 0
# _votes_cnt = int(input())
# _votes_i=0
# _votes = []
# while _votes_i < _votes_cnt:
#     _votes_item = str(input())
#     _votes.append(_votes_item)
#     _votes_i+=1
    

# res = electionWinner(_votes);
# f.write(res + "\n")

# f.close()
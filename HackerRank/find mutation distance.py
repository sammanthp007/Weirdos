def  findMutationDistance(start, end, bank):
    bank_set = set(bank)
    mutation_count = 0
    
    if not end in bank_set:
        return -1
    
    length = len(start)
    
    for i in range(length):
        if start == end:
            return mutation_count
        
        set_of_valid_new_mutations = getAllNewMutations(start, end, bank_set)
        
        if len(set_of_valid_new_mutations) == 0:
            return -1
        else:
            new_mutation = set_of_valid_new_mutations[0]
            print (new_mutation)
            mutation_count += 1
            start = new_mutation
    return mutation_count

def getAllNewMutations(start, end, bank_set):
    all_valid_mutation = []
    print (start, end)
    length = range(len(start))
    for i in length:
        if start[i] == end[i]:
            continue
        new_mutation = start[:i] + end[i] + start[i + 1:]
        if new_mutation in bank_set:
            all_valid_mutation.append(new_mutation)
    print (all_valid_mutation)
            
    return list(set(all_valid_mutation))

bank = ['AAAAAAAA', 'AAAAAAAT', 'AAAAAATT', 'AAAAATTT']

start = 'AAAAAAAA'
end = 'AAAAAATT'

print(findMutationDistance(start, end, bank))

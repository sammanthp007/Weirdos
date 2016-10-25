"""
aaabaaacaaadaaafaaag… aaaxaaayaaaz, M=5
{‘a’: 6, ‘b’: 1}
“abracadabra”, M=3 → “acada” # 11
M = 3
p=0
q=4
Check = {a, b, r}
longest_d_substring= “abr”
“Aaaa” M = 1
“Abaaab” M=2
len(check)
{} len(M)

"""
def get_longest_distinct_substring(M, string):
    front = 0
    last = 0 + M
    longest_str = string[:last]
    check = {}
    for character in string[:last]:
        check[character] = check.get(character, 0) + 1
        current_substring = longest_str
        # make sure the length of check is M
        while (front < len(string) - 1 - M and last < len(string)):
            if (string[last] in check or len(check) < M):
                check[character] = check.get(character, 0) + 1
                # not distinct, so add to longest
                current_substring += string[last]
                if (len(current_substring) >= len(longest_str)):
                    longest_str = current_substring
                last += 1
            else:
                # remove the one poited by front
                check[string[front]] = check.get(string[front]) - 1
                front += 1
                last = front + M
                current_substring = string[front : last]
        return longest_str

a = get_longest_distinct_substring(3, "samman")
print (a)

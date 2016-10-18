# takes in a string s and an integer n and returns a list of n tuples of the most frequent words in s in the format (word, frequency)

def count_words(s, n):
    output_list = []
    list_of_words = s.split()
    if n < 1:
        return output_list

    dict_words = {}
    for word in list_of_words:
        dict_words[word] = dict_words.get(word, 0) + 1

    min_freq = 0
    for k, v in dict_words.items():
        output_list.append((v, k))

    output_list.sort()
    output_list = output_list[len(output_list) - n:]
    new_list = []
    output_list.sort(reverse=True)
    for (k, v) in output_list:
        new_list.append((v, k))

    return new_list

print (count_words('betty bought a bit of butter but the butter was bitter', 3))

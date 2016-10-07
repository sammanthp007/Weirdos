def count_words(s, n): 
    list_of_words = s.split()
    for i in range(len(list_of_words)):
        if list_of_words[i][-1] == '.' or list_of_words[i][-1] == ',' or list_of_words[i][-1] == '?':
            list_of_words[i] = list_of_words[i][:-1]

    output_list = []
    for word in list_of_words:
        if len(output_list) == 0:
            output_list.append((len(word), word))
        else:
            if len(output_list) <= n:
                output_list.append((len(word), word))
                output_list.sort()
            else:
                if len(word) >= output_list[0][0]:
                    output_list = output_list[1:]
                    output_list.append((len(word), word))
                    output_list.sort()
    return output_list

print(count_words('samman is a sexxy boy dont you think so betty', 2)) 

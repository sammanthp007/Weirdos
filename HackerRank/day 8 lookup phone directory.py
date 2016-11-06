num_test_cases = int(input().strip())

phone_directory = {}
for i in range(num_test_cases):
    entry = input().strip()
    entry_list = entry.split(' ')
    phone_directory[entry_list[0]] = entry_list[1]

while (True):
    try:
        lookup = input().strip()
        val = phone_directory.get(lookup, 0)

        if int(val) == 0:
            print ('Not found')
            continue
        else:
            print (lookup + '=' + val)
    except:
        break
        
    
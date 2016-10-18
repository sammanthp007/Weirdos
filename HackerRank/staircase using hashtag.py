def  StairCase(n):
    #i = {0,1,2,3,4,5}
    for i in range(n):
        # for each line
        each_line = (n - i - 1)* " "
        each_line = each_line + (i + 1)* "#"
        print (each_line)

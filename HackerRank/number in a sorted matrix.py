# Find if a number is in a matrix that is sorted ascendingly in both rows and columns
# Done by Samman Bikram Thapa of Howard University by 7:23 pm Oct 10 2016

"""

A matrix - M by N 

  2  6   9 
  3  8   10
  7  11  12
  
  def isPresent(target: Int): Boolean 

"""

# takes in a number and a two dimensional array and returns if the number exists in the array or not
def is_present(num, lis):
    
    if (len(lis) == 0) or not (isinstance(num, (int))):
        return False

    last_row = len(lis) - 1
    last_col = len(lis[0]) - 1

    if len(lis) == 1 and num < lis[0][0]:
        return False

    if num < lis[last_row][0]:
        return is_present(num, lis[:last_row])
                          
    if num < lis[0][last_col]:
        return is_present(num, removes_last_col(lis))
    
    # go thorugh all the items in the list's last row and colm
    for item in lis[last_row]:
        if item == num:
            return True
    
    last_col_itr = get_last_col(lis)
    for item in last_col_itr:
        if item == num:
            return True
        
    return False
        
# takes in a two dimensional list and returns a two dimensional with the last column removed
def removes_last_col(lis):
    new_lis = []
    for row in lis:
        new_row = []
        for col in row[:-1]:
            new_row.append(col)
        new_lis.append(new_row)
    return new_lis
   
# takes in a two dimensional list and returns a list of items that was in the last column
def get_last_col(lis):
    new_lis = []
    for i in range(len(lis)):
        new_lis.append(lis[i][-1])
    return new_lis


# Test Cases

# Running for the case given in the question: 
"""
  2  6   9 
  3  8   10
  7  11  12
"""
lis = [[2,6,9], [3,8,10], [7,11,12]]
num = 2

print(is_present(num, lis))

# Asserting other test cases:

# 1) Test for when number in list

"""
  2  6   9 
  3  8   10
  7  11  12
"""
lis = [[2,6,9], [3,8,10], [7,11,12]]
num = 2

assert is_present(num, lis) == True


# *************************************

# 2) Test for when number not in list
"""
  2  6   9 
  3  8   10
  7  11  12
"""
lis = [[2,6,9], [3,8,10], [7,11,12]]
num = 4

assert is_present(num, lis) == False

# *************************************

# 3) Test for when number is 0
"""
  2  6   9 
  3  8   10
  7  11  12
"""
lis = [[2,6,9], [3,8,10], [7,11,12]]
num = 0

assert is_present(num, lis) == False

# *************************************

# 4) Test for when number list is empty
"""
"""
lis = []
num = 4

assert is_present(num, lis) == False

# *************************************

# 5) Test for when number list is empty and number is 0
"""
"""
lis = []
num = 0

assert is_present(num, lis) == False

# *************************************

# 6) Test for when number is not of type int
"""
  2  6   9 
  3  8   10
  7  11  12
"""
lis = []
num = "sumo logic"

assert is_present(num, lis) == False

# *************************************

# 7) Test for when number is negative number but list does not have negative numbers
"""
  2  6   9 
  3  8   10
  7  11  12
"""
lis = [[2,6,9], [3,8,10], [7,11,12]]
num = -3

assert is_present(num, lis) == False

# *************************************

# 8) Test for when number is negative number and list has negative numbers and the num is in the list
"""
  -222  -26   -9 
  -23    -8   -1
   3     11   12
"""
lis = [[-222,-26,-9], [-23,-8,-1], [3,11,12]]
num = 3

assert is_present(num, lis) == True

# *************************************

# 9) Test for when number as the last item in the two dimensional list
"""
  -222  -26   -9 
  -23    -8   -1
   3     11   12
"""
lis = [[-222,-26,-9], [-23,-8,-1], [3,11,12]]
num = 12

assert is_present(num, lis) == True

# *************************************

# 10) Test for when number as the first item in the two dimensional list
"""
  -222  -26   -9 
  -23    -8   -1
   3     11   12
"""
lis = [[-222,-26,-9], [-23,-8,-1], [3,11,12]]
num = -222

assert is_present(num, lis) == True

# *************************************

# 11) Test for when list size increases
"""
  -222  -26   -9 
  -23    -8   -1
   3     11   12
"""
lis = [[-222,-26,-9, 1], [-23,-8,-1, 2], [3,11,12, 13]]
num = -26

assert is_present(num, lis) == True

# *************************************

# 12) Test for when list size is one with one item
"""
  1
"""
lis = [[1]]
num = -26

assert is_present(num, lis) == False

# *************************************

# 13) Test for when list is one row
"""
  1 4
"""
lis = [[1, 4]]
num = 4

assert is_present(num, lis) == True

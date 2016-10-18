def  calculateNumberOfDays(x, y, d):
    """Calculate the number of days for Kai to surpase the number of problems Aka completes

    x - The number of problems per day Aka will complete, will be >= 1
    y - The number of problems per day Kai will complete, will be between 0 and 100 inclusive
    d - The number of problems Aka is already ahead by
 
    returns the number of days it will take for Kai to complete more problems than Aka or -1 if never
    """
    if (x > y):
        return -1
    if (x == y and d > 0):
        return -1
    if (x == y and d == 0):
        return -1
    if d < 0:
        return 0
    num_of_days = (d * 1.0) / (y - x)
    count = 0
    while (count <= num_of_days):
        count += 1
    return count

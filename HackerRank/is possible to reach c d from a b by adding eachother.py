def isPossible(a, b, c d):
    if boolIsPossible(a, b, c, d):
        return "Yes"
    return "No"


def boolIsPossible(a, b, c, d):
    if areEqual(a, b, c, d):
        return True

    if a > c or b > d:
        print (a,b,c,d)
        return False

    # Depth 1:
    if boolIsPossible(a + b, b, c, d):
        return True

    # Depth 2:
    if boolIsPossible(a, a + b, c, d):
        return True

    return False

def areEqual(a,b,c,d):
    return a == c and b == d


a,b,c,d = 1,4,5,9
print(isPossible(a,b,c,d))

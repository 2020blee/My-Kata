import math

def NoTwoAdjacent(r, g):
    if r > g + 1:
        return 0
    else:
        numerator = math.factorial(g+1)
        denominator = math.factorial(r) * math.factorial(g+1-r)
        ans = numerator/denominator
        return ans

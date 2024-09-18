import math
def ucln(a, b):
    if(math.gcd(a, b)==1):
        return True
    return False
if(__name__=='__main__'):
    l, r = map(int, input().split())
    for i in range(l, r-1):
        for j in range(i+1, r):
            for k in range(j+1, r+1):
                if(ucln(i, j) and ucln(i, k) and ucln(j, k)):
                    print("(", i, ", ", j, ", ", k, ")", sep="")
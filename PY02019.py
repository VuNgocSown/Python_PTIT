import math
if(__name__=='__main__'):
    n = int(input())
    a = [int(i) for i in input().split()]
    a = sorted(a)
    for i in range(0, n-1):
        for j in range(i+1, n):
            if(math.gcd(a[i], a[j])==1):
                print(a[i], a[j])
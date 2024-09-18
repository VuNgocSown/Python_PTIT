import math
def ucln(a, b):
    if(b == 0):
        return a
    return ucln(b, a % b)
def nt(n):
    for i in range(2, int(math.sqrt(n)+1)):
        if(n%i==0):
            return 0
    return n > 1
def tongcs(n):
    sum = 0
    while(n>0):
        c = n % 10
        sum += c
        n //= 10
    return sum
if(__name__=='__main__'):
    t = int(input())
    while(t > 0):
        a , b= map(int, input().split())
        uc = ucln(a, b)
        if(nt(tongcs(uc))):
            print("YES")
        else:
            print("NO")
        t-=1
import math
def ucln(a, b):
    if(b==0):
        return a
    return ucln(b, a%b)
def nt(n):
    for i in range(2, int(math.sqrt(n))+1):
        if(n%i==0):
            return 0
    return n > 1
if(__name__=='__main__'):
    t = int(input())
    while(t > 0):
        n = int(input())
        cnt = 0
        for i in range(1, n):
            if(ucln(i, n)==1):
                cnt+=1
        if(nt(cnt)):
            print("YES")
        else:
            print("NO")
        t-=1
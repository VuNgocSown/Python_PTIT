import math
def nt(n):
    for i in range(2, int(math.sqrt(n)+1)):
        if(n%i==0):
            return 0
    return n > 1
def check(n):
    sum = 0
    for i in range(0, len(n)):
        if(i % 2 ==0):
            if(int(n[i])%2!=0):
                return 0
        else:
            if(int(n[i])%2==0):
                return 0
        sum += int(n[i])
    if(nt(sum)):
        return 1
    return 0
if(__name__=='__main__'):
    t = int(input())
    while(t>0):
        n = input()
        if(check(n)):
            print("YES")
        else:
            print("NO")
        t-=1
import math
def nt(n):
    for i in range(2, int(math.sqrt(n)+1)):
        if(n%i==0):
            return 0
    return n>1
def tongcs(n):
    sum = 0
    while(n > 0):
        sum += n%10
        n //=10
    if(nt(sum)):
        return True
    return False
if(__name__=='__main__'):
    t = int(input())
    while(t > 0):
        n = int(input())
        if(tongcs(n)):
            print("YES")
        else:
            print("NO")
        t-=1
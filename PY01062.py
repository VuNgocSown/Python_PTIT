import math
def nt(n):
    for i in range(2, int(math.sqrt(n)+1)):
        if(n%i==0):
            return 0
    return n > 1
def check(n):
    if(nt(len(n))==False):
        return 0
    snt = 0
    nnt = 0
    for i in range(0, len(n)):
        if(nt(int(n[i]))):
            snt+=1
        else:
            nnt+=1
    if(nnt > snt):
        return 0
    return 1
  
if(__name__=='__main__'):
    t = int(input())
    while(t>0):
        n = input()
        if(check(n)):
            print("YES")
        else:
            print("NO")
        t-=1
import math
def nt(n):
    for i in range(2, int(math.sqrt(n)+1)):
        if(n%i==0):
            return 0
    return n > 1
def check(n):
    be = int(n[:3])
    ed = int(n[len(n)-3:len(n)])
    if(nt(be) and nt(ed)):
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
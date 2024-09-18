import math
def nt(n):
    for i in range(2, int(math.sqrt(n)+1)):
        if(n%i==0):
            return 0
    return n > 1
def check(n):
    if(nt(len(n))==0):
        return False
    nto=0
    nnto=0
    for i in n:
        if(nt(int(i))):
            nto+=1
        else:
            nnto+=1
    if(nto > nnto):
        return True
    return False
            
if(__name__=='__main__'):
    t = int(input())
    while(t > 0):
        n = input()
        if(check(n)):
            print("YES")
        else:
            print("NO")
        t-=1
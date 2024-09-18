import math
def nt(n):
    for i in range(2, int(math.sqrt(n)+1)):
        if(n%i==0):
            return 0
    return n > 1
def check(n):
    for i in range(0, len(n)):
        if(n[i] == '2' or n[i]=='3' or n[i]=='5' or n[i]=='7'):
            if(nt(i)==0):
                return 0
        else:
            if(nt(i)):
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
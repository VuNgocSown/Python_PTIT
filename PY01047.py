import math
def nt(n):
    for i in range(2, int(math.sqrt(n)+1)):
        if(n%i==0):
            return 0
    return n > 1
if(__name__=='__main__'):
    t = int(input())
    while(t > 0):
        n = input()
        num = ""
        for i in range(-4, 0):
            num += n[i]
        if(nt(int(num))):
            print("YES")
        else:
            print("NO")
        t-=1
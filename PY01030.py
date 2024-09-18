import math
def ucln(a, b):
    if(b == 0):
        return a
    return ucln(b, a%b)
if(__name__=='__main__'):
    n, k=map(int, input().split())
    cnt = 0
    for i in range(int(math.pow(10, k-1)), int(math.pow(10, k))):
        if(ucln(i, n)==1):
            print(i, end=' ')
            cnt+=1
            if(cnt==10):
                print()
                cnt=0
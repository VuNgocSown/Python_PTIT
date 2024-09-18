def check(n):
    if(len(n)<3): return False
    if(n[1]<=n[0] or n[-2]<=n[-1]): return False
    p1=1
    p2=len(n)-2
    while(n[p1]>n[p1-1]): p1+=1
    while(n[p2]>n[p2+1]): p2-=1
    if(p2+2==p1): return True
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
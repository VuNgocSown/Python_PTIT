def check(n):
    for i in range(0, len(n)):
        if((n[i]!='4') & (n[i]!='7')):
            return 0
    return 1
if(__name__=='__main__'):
    t = int(input())
    while(t > 0):
        n = input()
        if(check(n)):
            print("YES")
        else:
            print("NO")
        t-=1
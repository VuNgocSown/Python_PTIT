def check(n):
    for i in range(0, len(n)):
        if(n[i]!='0' and n[i]!='1' and n[i]!='2'):
            return False
    return True
if(__name__=='__main__'):
    t = int(input())
    while(t > 0):
        n = input()
        if(check(n)):
            print("YES")
        else:
            print("NO")
        t-=1
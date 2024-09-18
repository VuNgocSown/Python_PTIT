def ucln(a, b):
    if(b == 0):
        return a
    return ucln(b, a%b)
if(__name__=='__main__'):
    t = int(input())
    while(t > 0):
        n = input()
        rn = n[::-1]
        if(ucln(int(n), int(rn))==1):
            print("YES")
        else:
            print("NO")
        t-=1
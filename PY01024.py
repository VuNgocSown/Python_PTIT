def check(n):
    sum = n % 10
    c = n % 10
    n //= 10
    while(n > 0):
        ed = n % 10
        sum += ed
        if(abs(ed-c)!=2):
            return 0
        c = ed
        n //= 10
    if(sum % 10 != 0):
        return 0
    return 1
if(__name__=='__main__'):
    t = int(input())
    while(t > 0):
        n = int(input())
        if(check(n)):
            print("YES")
        else:
            print("NO")
        t-=1
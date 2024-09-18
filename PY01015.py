def kg(n):
    c = n % 10
    n //=10
    while(n > 0):
        ed = n % 10
        if(ed > c):
            return 0
        c = ed
        n //= 10
    return 1
if(__name__=='__main__'):
    t = int(input())
    while(t > 0):
        n = int(input())
        if(kg(n)):
            print("YES")
        else:
            print("NO")
        t-=1
def tn(n):
    newNum = 0
    x = n
    while(n>0):
        c = n % 10
        if((c!=0) & (c!=2) & (c!=4) & (c!=6) & (c!=8)):
            return 0
        newNum = newNum * 10 + c
        n //= 10
    if(x != newNum):
        return 0
    return 1
if(__name__=='__main__'):
    t = int(input())
    while(t > 0):
        n = int(input())
        for i in range(10, n):
            if(tn(i)):
                print(i, end=' ')
        print()
        t-=1
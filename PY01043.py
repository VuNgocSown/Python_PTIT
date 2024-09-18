def check(n):
    revNum = 0
    cnt = 0
    x=n
    while(n > 0):
        c = n % 10
        revNum = revNum*10+c
        cnt+=1
        if(c % 2 != 0):
            return False
        n //= 10
    if((cnt % 2 != 0) or (revNum != x)):
        return False
    return True
if(__name__=='__main__'):
    t = int(input())
    arr = []
    for i in range(20, 1000000):
        if(check(i)):
            arr.append(i)
    while(t > 0):
        n = int(input())
        for x in arr:
            if(x < n):
                print(x, end=' ')
        print()
        t-=1
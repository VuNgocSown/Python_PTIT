def rev(n):
    revNum = 0
    while(n>0):
        c = n % 10
        revNum = revNum*10 + c
        n //=10
    return revNum
if(__name__=='__main__'):
    t = int(input())
    while(t > 0):
        n = int(input())
        sum = 0
        check = False
        if(n % 7 == 0):
            print(n)
        else:
            for i in range(0, 1000):
                sum = n + rev(n)
                n = sum
                if(sum % 7 == 0):
                    check = True
                    print(n)
                    break
            if(not check):
                print(-1)
        t-=1
            
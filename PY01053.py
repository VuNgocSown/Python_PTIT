def tongcs(n):
    sum = 0
    while(n > 0):
        sum += n%10
        n //=10
    return sum
if(__name__=='__main__'):
    t = int(input())
    while(t > 0):
        n = int(input())
        if(tongcs(n) % 3 == 0):
            print("YES")
        else:
            print("NO")
        t-=1
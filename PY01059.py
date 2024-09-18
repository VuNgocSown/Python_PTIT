import math
def cal(n):
    sum = 0
    mul = 1
    check=False
    for i in range(0, len(n)):
        if(i%2!=0):
            sum += int(n[i])
        else:
            if(int(n[i])):
                mul *= int(n[i])
                check=True
    if(not check):
        mul = 0
    return sum, mul

if(__name__=='__main__'):
    t = int(input())
    while(t>0):
        n = input()
        sum, mul = cal(n)
        print(mul,sum)
        t-=1
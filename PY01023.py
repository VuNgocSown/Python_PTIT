import math
if(__name__=='__main__'):
    t = int(input())
    while(t > 0):
        n = int(input())
        print("1 ", end="")
        x = n
        for i in range(2, int(math.sqrt(n)+1)):
            if(x % i==0):
                cnt = 0
                while(x%i==0):
                    x//=i
                    cnt += 1
                print("* ",i, "^", cnt, sep="", end=" ")
        if(x!=1):
            print("* ", x, "^1", sep="", end="")
        print()
        t-=1
                
if(__name__=='__main__'):
    t = int(input())
    while(t>0):
        n = input()
        mul = 1
        for i in range(0, len(n)):
            if(n[i]!='0'):
                mul *= int(n[i])
        print(mul)
        t-=1
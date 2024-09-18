if(__name__=='__main__'):
    t = int(input())
    while(t > 0):
        n = int(input())
        a = []
        b = []
        x = input().split()
        y = input().split()
        for i in range(0, n):
            a.append(int(x[i]))
        for i in range(0, n):
            b.append(int(y[i]))
        a.sort()
        b.sort()
        check = False
        for i in range(0, n):
            if(a[i] > b[i]):
                check = True
                print("NO")
                break
        if(check == False):
            print("YES")
        t-=1
        
if __name__ == '__main__':
    t = int(input())
    while(t > 0):
        n = int(input())
        a = [int(i) for i in input().split()]
        b = [int(i) for i in input().split()]
        a.sort()
        b.sort()
        check = False
        i = 0
        while(i < n):
            if(a[i] > b[i]):
                check = True
                break
            i+=1
        if(check):
            print("NO")
        else:
            print("YES")
        t-=1
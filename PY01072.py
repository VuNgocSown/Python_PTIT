if __name__ == '__main__':
    n, k = map(int, input().split())
    a = [int(i) for i in input().split()]
    b = [] 
    for i in range(n):
        if(a[i] not in b):
            b.append(a[i])
    b.sort()
    c = []
    c.append(0)
    for i in range(1, k+1):
        c.append(i)
    # print(c)
    n=len(b)
    while(True):
        for i in range(1, k+1):
            print(b[c[i]-1], end=' ')
        print()
        i = k
        while(c[i]==n-k+i):
            i-=1
        if(i==0):
            break
        else:
            c[i]+=1
            for j in range(i+1, k+1):
                c[j]=c[j-1]+1
        
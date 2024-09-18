a = []
def fibo():
    a.append(1)
    a.append(1)
    for i in range(2, 93):
        a.append(a[i-1]+a[i-2])
if(__name__=='__main__'):
    t=int(input())
    fibo()
    while(t > 0):
        m, b = map(int, input().split())
        for i in range(m, b + 1):
            print(a[i-1], end=' ')
        print()
        t-=1
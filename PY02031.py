nt = [1]*10000
def sang():
    nt[0] = 0
    nt[1] = 0
    for i in range(2, int(1000) + 1):
        if nt[i]:
            for j in range(i*i, 10000, i):
                nt[j] = 0
if __name__ == '__main__':
    sang()
    n, m = map(int, input().split())
    a = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        a[i]=list(map(int, input().split()))
    for i in range(n):
        for j in range(m):
            if(nt[a[i][j]]):
                a[i][j]=1
            else:
                a[i][j]=0
    for i in range(n):
        for j in range(m):
            print(a[i][j], end=' ')
        print()
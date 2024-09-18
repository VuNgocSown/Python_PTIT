import math
if __name__ == '__main__':
    n = int(input())
    a = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        a[i]=list(map(int, input().split()))
    k = int(input())
    nt = 0
    nd = 0
    for i in range(n):
        for j in range(i+1, n):
            nt += a[i][j]
    for i in range(n):
        for j in range(i):
            nd+=a[i][j]
    if(abs(nt-nd)<=k):
        print("YES")
    else:
        print("NO")
    print(abs(nt-nd))
    
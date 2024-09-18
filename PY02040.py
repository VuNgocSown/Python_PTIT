import math
if __name__ == '__main__':
    n = int(input())
    a = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        a[i]=list(map(int, input().split()))
    k = int(input())
    nt = 0
    nd = 0
    for i in range(0, n-1):
        for j in range(n-2-i, -1, -1):
            # print(a[i][j], end=' ')
            nt+=a[i][j]
        # print()
    for i in range(1, n):
        for j in range(n-i, n):
            nd+=a[i][j]
    if(abs(nt-nd)<=k):
        print("YES")
    else:
        print("NO")
    print(abs(nt-nd))
    
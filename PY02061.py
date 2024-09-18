if __name__ == '__main__':
    t = int(input())
    while(t > 0):
        n, m = map(int, input().split())
        a = [[0 for _ in range(m)] for _ in range(n)]
        b = [[0 for _ in range(3)] for _ in range(3)]
        for i in range(n):
            a[i] = list(map(int, input().split()))
        for i in range(3):
            b[i] = list(map(int, input().split()))
        s=0
        for i in range(n):
            if i==n-2: break
            for j in range(m):
                if j==m-2: break
                for x in range(3):
                    for y in range(3):
                        s+=b[x][y]*a[i+x][j+y]
        print(s)
        t-=1
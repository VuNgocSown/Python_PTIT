nt = [1]*1000000

def sang():
    nt[0] = 0
    nt[1] = 0
    for i in range(2, int(1000) + 1):
        if nt[i]:
            for j in range(i*i, 1000000, i):
                nt[j] = 0

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    
    sang()
    
    b = [0]*1000000
    for i in range(n):
        if 0 <= a[i] < 1000000 and nt[a[i]]:
            b[a[i]] += 1
    
    for i in range(n):
        if 0 <= a[i] < 1000000 and b[a[i]]:
            print(a[i], b[a[i]])
            b[a[i]] = 0

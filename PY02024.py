def tichcs(n):
    mul = 1
    while(n > 0):
        mul *= n % 10
        n //=10
    return mul
if __name__ == '__main__':
    t = int(input())
    while(t > 0):
        n = int(input())
        a = []
        [a.append(int(i)) for i in input().split()]
        a.sort()
        a.sort(key=tichcs)
        for i in range(0, n):
            print(a[i], end=' ')
        print()
        t-=1
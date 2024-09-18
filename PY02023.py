def tongcs(n):
    sum = 0
    while(n>0):
        sum += n % 10
        n //=10
    return sum
if __name__ == '__main__':
    t = int(input())
    while(t > 0):
        n = int(input())
        a = []
        [a.append(int(i)) for i in input().split()]
        a.sort()
        a.sort(key=tongcs)
        for i in range(0, n):
            print(a[i], end=' ')
        print()
        t-=1
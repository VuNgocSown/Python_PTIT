if(__name__=='__main__'):
    n = int(input())
    a = [float(i) for i in input().split()]
    max_val = max(a)
    min_val = min(a)
    b = []
    for i in range(0, len(a)):
        if(a[i]==max_val or a[i]==min_val):
            a[i]=-1
            b.append(i)
    sum = 0
    for i in a:
        if(i != -1):
            sum += i
    sum /= len(b)
    print('%.2f' % sum)
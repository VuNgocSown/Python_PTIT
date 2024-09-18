if(__name__=='__main__'):
    n = int(input())
    a = []
    s = input().split()
    cnt = 0
    for i in range(0, len(s)):
        a.append(int(s[i]))
    for i in range(1, n):
        if(a[i]!=a[i-1]):
            cnt+=1
    print(cnt)
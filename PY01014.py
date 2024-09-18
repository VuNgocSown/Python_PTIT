if(__name__=='__main__'):
    a, k, n = map(int, input().split())
    c = k - a % k
    b = c
    cnt = 0
    while(a + b <= n):
        print(b, end=' ')
        cnt+=1
        b+=k
    if(cnt==0):
        print(-1)
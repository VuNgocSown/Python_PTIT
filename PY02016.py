if(__name__=='__main__'):
    t = int(input())
    while(t>0):
        n = int(input())
        a = [int(i) for i in input().split()]
        cnt = [0]*1000000
        for i in a:
            cnt[i]+=1
        max_val = 0
        for i in a:
            max_val = max(max_val, cnt[i])
        if(max_val > n/2):
            for i in range(0, 1000000):
                if(max_val == cnt[i]):
                    print(i)
                    break
        else:
            print("NO")
        t-=1
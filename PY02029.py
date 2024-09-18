if __name__ == '__main__':
    n, m = map(int, input().split())
    a = [int(i) for i in input().split()]
    cnt = [0]*(m+1)
    for i in a:
        cnt[i]+=1
    max_val = max(cnt)
    for i in range(len(cnt)):
        if(cnt[i]==max_val):
            cnt[i]=0
    max_val = max(cnt)
    if(max_val==0):
        print("NONE")
    else:
        for i in range(len(cnt)):
            if(cnt[i]==max_val):
                print(i)
                break
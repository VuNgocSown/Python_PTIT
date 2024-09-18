if(__name__=='__main__'):
    a = []
    cnt = 0
    while(cnt < 10):
        x = [int(i) for i in input().split()]
        # print(x)
        cnt += len(x)
        for i in x:
            if((i % 42) not in a):
                a.append(i%42)
    print(len(a))
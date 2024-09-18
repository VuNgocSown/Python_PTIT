if(__name__=='__main__'):
    t = int(input())
    while(t > 0):
        n = int(input())
        a = []
        x = [0]*1001
        for i in range(0, n):
            m = int(input())
            a.append(m)
            x[m]+=1
        max_val = 0
        for i in range(0, 1001):
            max_val = max(max_val, x[i])
        for i in range(0, 1001):
            if(x[i]==max_val):
                print(i)
                break
        t-=1
        
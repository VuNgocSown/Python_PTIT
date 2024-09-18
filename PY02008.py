nt = [1]*1000000
def sang():
    nt[0]=0
    nt[1]=0
    for i in range(2, 1000):
        if(nt[i]):
            for j in range(i*i, 1000000, i):
                nt[j]=0
if(__name__=='__main__'):
    n, x = map(int, input().split())
    sang()
    listnt = []
    cnt = 0
    sum = x
    for i in range(2, 1000000):
        if(nt[i]):
            listnt.append(i)
            cnt+=1
            if(cnt == n):
                break
    print(sum, end = ' ')
    for i in listnt:
        sum += i
        print(sum, end = ' ')
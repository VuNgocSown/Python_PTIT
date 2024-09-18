if __name__ == '__main__':
    t = int(input())
    while(t > 0):
        n = int(input())
        arr = [int(i) for i in input().split()]
        ma = dict({})
        for i in arr:
            if i not in ma:
                ma[i]=1
            else:
                ma[i]+=1
        for val, fre in ma.items():
            if(fre % 2 == 1):
                print(val)
        t-=1
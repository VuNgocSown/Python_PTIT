def handle(n):
    if(len(n)==1):
        return n
    check = False
    tmp = False
    for i in range(len(n)-1, 0, -1):
        if(tmp):
            if(int(n[i])+1 < 5):
                tmp = False
        if(int(n[i])>=5):
            tmp = True
    if(tmp):
        check = True
    if(check):
        be = int(n[0])+1
        newNum = str(be) + (len(n)-1)*'0'
        return newNum
    else:
        newNum = n[0] + (len(n)-1)*'0'
        return newNum
    
    
if(__name__=='__main__'):
    t = int(input())
    while t > 0:
        n = input()
        print(handle(n))
        t-=1
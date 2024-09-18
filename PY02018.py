if(__name__=='__main__'):
    n = int(input())
    check = False
    listNum = [int(i) for i in input().split()]
    for i in range(1, n+1):
        if(i not in listNum):
            print(i)
            check = True
    if(not check):
        print(n+1)
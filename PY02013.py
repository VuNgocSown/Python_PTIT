def check(listNum):
    cnt = 0
    for i in listNum:
        if(i == 0):
            cnt += 1
    if(cnt == len(listNum)):
        return 0
    return 1
def equal(listNum):
    for i in range(1, len(listNum)):
        if(listNum[i]!=listNum[i-1]):
            return 0
    return 1
if(__name__=='__main__'):
    while(1):
        cnt = 0
        listNum = [int(i) for i in input().split()]
        if(not check(listNum)):
            break
        while(1):
            newList = [0]*len(listNum)
            for i in range(0, len(listNum)):
                if(i == len(listNum)-1):
                    newList[i] = abs(listNum[i]-listNum[0])
                else:
                    newList[i]=abs(listNum[i]-listNum[i+1])
            cnt += 1
            listNum = newList.copy()
            if(equal(newList)):
                break
        print(cnt)
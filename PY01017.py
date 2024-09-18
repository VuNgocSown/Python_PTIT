if(__name__=='__main__'):
    t = int(input())
    while(t > 0):
        n = input()
        newStr=""
        cnt = 1
        for i in range(len(n)-2, -1, -1):
            if(n[i+1]!=n[i]):
                newStr=str(cnt)+n[i+1]+newStr
                cnt = 1
            else:
                cnt+=1
        newStr = str(cnt)+n[0]+newStr
        print(newStr)
        t-=1
import math
if(__name__=='__main__'):
    t = int(input())
    while(t>0):
        s = input()
        n = input()
        cnt = 0
        while(s.find(n)!=-1):
            cnt += 1
            s = s[:s.find(n)] + s[s.find(n)+len(n):]
            # print(s)
        print(cnt)
        t-=1
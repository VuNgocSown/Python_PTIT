import math
def check(s, revS):
    for i in range(1, len(s)):
        if(abs(ord(s[i])-ord(s[i-1])) != abs(ord(revS[i])-ord(revS[i-1]))):
            return 0
    return 1
if(__name__=='__main__'):
    t = int(input())
    while(t>0):
        s = input()
        revS = s[::-1]
        if(check(s, revS)):
            print("YES")
        else:
            print("NO")
        t-=1
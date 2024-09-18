if(__name__=='__main__'):
    t = int(input())
    while(t > 0):
        s = input()
        subStr=s[len(s)-2:len(s)]
        if(subStr=='86'):
            print("YES")
        else:
            print("NO")
        t-=1
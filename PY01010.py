if(__name__=='__main__'):
    t = int(input())
    while(t > 0):
        n = input()
        be = n[:2]
        ed = n[len(n)-2:]
        if(be==ed):
            print("YES")
        else:
            print("NO")
        t-=1
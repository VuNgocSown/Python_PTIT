if(__name__=='__main__'):
    t = int(input())
    while(t > 0):
        n = input()
        check = True
        for i in range(2, len(n)-2):
            if(n[i]!=n[i-2] or n[i]!=n[i+2]):
                check=False
                break
        if(check):
            print("YES")
        else:
            print("NO")
        t-=1
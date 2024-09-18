if(__name__=='__main__'):
    n = input()
    cnt = 0
    for i in range(0, len(n)):
        if((n[i]=='4') | (n[i]=='7')):
            cnt+=1
    if((cnt % 4 == 0) | (cnt % 7 == 0)):
        print("YES")
    else:
        print("NO")
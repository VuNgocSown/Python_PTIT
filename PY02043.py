if __name__ == '__main__':
    t = int(input())
    while(t > 0):
        s1 = input()
        s2 = input()
        cnt = 0
        while(s1.find(s2)!=-1):
            s1 = s1[s1.find(s2)+len(s2):]
            cnt+=1
        print(cnt)
        t-=1
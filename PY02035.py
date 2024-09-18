if __name__ == '__main__':
    s = input()
    a = []
    if(len(s)%2==0):
        for i in range(0, len(s), 2):
            a.append(int(s[i:i+2]))
    else:
        for i in range(0, len(s)-1, 2):
            a.append(int(s[i:i+2]))
    k = int(input())
    cnt = [0]*100
    for i in a:
        cnt[i]+=1
    b = []
    for i in a:
        if(i not in b):
            b.append(i)
    b.sort()
    check = False
    for i in b:
        if(cnt[i] >= k):
            print(i, cnt[i])
            check = True
    if(not check):
        print("NOT FOUND")
            
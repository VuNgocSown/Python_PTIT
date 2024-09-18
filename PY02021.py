if __name__ == '__main__':
    t = int(input())
    while(t > 0):
        n, m, k = map(int, input().split())
        a = [int(i) for i in input().split()]
        b = [int(i) for i in input().split()]
        c = [int(i) for i in input().split()]
        i = 0
        j=0
        h=0
        check = False
        while(i < n and j < m and h < k):
            if(a[i] == b[j] == c[h]):
                print(a[i], end = ' ')
                i+=1
                j+=1
                h+=1
                check = True
            elif(a[i] < b[j] or a[i] < c[h]):
                i+=1
            elif(b[j] < a[i] or b[j] < c[h]):
                j+=1
            elif(c[h] < a[i] or c[h] < b[j]):
                h+=1
        if(not check):
            print("NO", end = "")
        print()
        t-=1
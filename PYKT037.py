def he_cs(n, k):
    s = ""
    while(n > 0):
        x = n % k
        if(x >= 10):
            s+= chr(x+55)
        else:
            s+= str(x)
        n//=k
    return s[::-1]
if __name__ == '__main__':
    t = int(input())
    while(t > 0):
        n, k = map(int, input().split())
        print(he_cs(n, k))
        t-=1
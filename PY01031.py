def he_cs(n, k):
    result = ""
    while(n > 0):
        x = n % k
        if(x >= 10):
            result += chr(55 + x)
        else:
            result += str(x)
        n //= k
    return result[::-1]
if __name__ == '__main__':
    t = int(input())
    while(t > 0):
        n, k = map(int, input().split())
        print(he_cs(n, k))
        t-=1
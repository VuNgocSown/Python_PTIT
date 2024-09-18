import math
def he_10(n):
    result = 0
    mu = 0
    for i in range(len(n)-1, -1, -1):
        result += int(n[i]) * int(math.pow(2, mu))
        mu += 1
    return result
def he_8(n):
    s = ""
    while (n > 0):
        s += str(n%8)
        n //= 8
    return s[::-1]
if __name__ == '__main__':
    n = input()
    print(he_8(he_10(n)))
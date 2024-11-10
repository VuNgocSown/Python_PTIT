import math
def nt(n):
    for i in range(2, int(math.sqrt(n)+1)):
        if(n%i==0):
            return 0
    return n > 1
if __name__ == '__main__':
    n = int(input())
    a = [int(i) for i in input().split()]
    b = []
    for x in a:
        if(x not in b):
            b.append(x)
    sum_val = sum(b)
    check = False
    l_val = 0
    for i in range(len(b)):
        l_val += b[i]
        sum_val -= b[i]
        if(nt(l_val) and nt(sum_val)):
            print(i)
            check = True
            break
    if(not check):
        print("NOT FOUND")
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
    for i in a:
        if(i not in b):
            b.append(i)
    sum_arr = sum(b)
    left_arr = 0
    check = False
    for i in range(0, len(b)):
        left_arr+=b[i]
        sum_arr-=b[i]
        if(nt(left_arr) and nt(sum_arr)):
            print(i)
            check = True
            break
    if(not check):
        print("NOT FOUND")
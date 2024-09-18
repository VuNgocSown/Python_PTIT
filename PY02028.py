import math
def nt(n):
    for i in range(2, int(math.sqrt(n)+1)):
        if(n%i==0):
            return 0
    return n > 1
if __name__ == '__main__':
    n = int(input())
    a = [int(i) for i in input().split()]
    primes = [i for i in a if nt(i)]
    primes.sort()
    index = 0
    for i in a:
        if(nt(i)):
            print(primes[index], end=" ")
            index+=1
        else:
            print(i, end = " ")
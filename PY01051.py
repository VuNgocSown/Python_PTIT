def tongcs(n):
    sum = 0
    while(n > 0):
        sum += n % 10
        n //=10
    return sum
def tn(n):
    x = str(tongcs(n))
    if(len(x)<2): return False
    revX=x[::-1]
    if(x!=revX): return False
    return True
if(__name__=='__main__'):
    t = int(input())
    while(t > 0):
        n = int(input())
        if(tn(n)):
            print("YES")
        else:
            print("NO")
        t-=1
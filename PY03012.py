
if __name__ == '__main__':
    n = int(input())
    a = {}
    for i in range(n):
        s = input()
        ac, sub = map(int, input().split())
        a[s] = (ac, sub)
    
    
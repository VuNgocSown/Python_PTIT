if __name__ == '__main__':
    n, m = map(int, input().split())
    a = list(set(sorted([int(i) for i in input().split()])))
    b = list(set(sorted([int(i) for i in input().split()])))
    if(a == b):
        print("YES")
    else:
        print("NO")
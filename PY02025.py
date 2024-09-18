if __name__ == '__main__':
    n, m = map(int, input().split())
    a = set(sorted([int(i) for i in input().split()]))
    b = set(sorted([int(i) for i in input().split()]))
    inter = a.intersection(b)
    asub = a.difference(b)
    bsuba = b.difference(a)
    
    for i in sorted(inter):
        print(i, end=' ')
    print()
    
    for i in sorted(asub):
        print(i, end=' ')
    print()
    
    for i in sorted(bsuba):
        print(i, end=' ')
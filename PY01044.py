if __name__ == '__main__':
    s1 = set([i.lower() for i in input().split()])
    s2 = set([i.lower() for i in input().split()])
    u = list(s1.union(s2))
    v = list(s1.intersection(s2))
    u.sort()
    v.sort()
    for i in u:
        print(i, end = " ")
    print()
    for i in v:
        print(i, end = " ")
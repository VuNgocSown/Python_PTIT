if __name__ == '__main__':
    s = input()
    a = []
    if(len(s)%2==0):
        for i in range(0, len(s), 2):
            a.append(s[i:i+2])
    else:
        for i in range(0, len(s)-1, 2):
            a.append(s[i:i+2])
    b = []
    for i in a:
        if(i not in b):
            b.append(i)
    b.sort()
    for i in b:
        print(i, end = ' ')
            
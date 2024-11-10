if __name__ == '__main__':
    s = input()
    while(len(s)>1):
        be = int(s[:len(s)//2])
        ed = int(s[len(s)//2:])
        s = str(be+ed)
        print(s)
    # print(s)
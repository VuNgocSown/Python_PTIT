def check(s):
    if(s.find('888')!=-1):
        return 0
    for i in s:
        if(i != '6' and i != '8'):
            return 0
    return 1
if __name__ == '__main__':
    s = input()
    if(check(s)):
        print("YES")
    else:
        print("NO")
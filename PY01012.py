if __name__ == '__main__':
    s = input()
    t = input()
    p = int(input())
    print(s[:p-1] + t + s[p-1:])
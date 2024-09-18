if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        print("Test ", i+1, ":", sep="", end = ' ')
        s1 = input()
        s2 = input()
        s1 = [i for i in s1]
        s2 = [i for i in s2]
        s1.sort()
        s2.sort()
        if(s1 == s2):
            print("YES")
        else:
            print("NO")
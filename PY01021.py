if __name__ == '__main__':
    t = int(input())
    while(t > 0):
        s = input()
        new_str = []
        num = 0
        for i in range(len(s)):
            if(s[i].isdigit()):
                num += int(s[i])
            else:
                new_str.append(s[i])
        new_str.sort()
        new_str = "".join(new_str)
        new_str += str(num)
        print(new_str)
        t-=1
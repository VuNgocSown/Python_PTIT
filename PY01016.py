if(__name__=='__main__'):
    t = int(input())
    while(t > 0):
        n = input()
        newStr = ""
        for i in range(0, len(n)):
            if(n[i].isdigit()):
                for j in range(0, int(n[i])):
                    newStr += n[i-1]
        print(newStr)
        t-=1
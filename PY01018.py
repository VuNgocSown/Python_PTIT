if(__name__=='__main__'):
    P ="ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
    while(True):
        x = input()
        if(x[0] == '0'):
            break
        # print(k, s)
        k, s = x.split()
        k = int(k)
        newStr = ""
        for i in range(0, len(s)):
            newStr+=P[(i+k)%28]
        print(newStr.)
        
        
    
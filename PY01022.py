if __name__ == '__main__':
    s = input()
    if(len(s) == 1):
        print(1)
    else:
        cnt = 0
        while(len(s) > 1):
            cnt+=1
            sum = 0
            for i in s : 
                sum += ord(i)-ord('0')
            s = str(sum)
        print(cnt)
import sys
if __name__ == '__main__':
    n = int(input())
    arr = []
    while len(arr)<n:
        arr.extend(list(map(int, input().split())))
    chan = []
    le = []
    for i in arr:
        if(i % 2 ==0):
            chan.append(i)
        else:
            le.append(i)
    chan.sort()
    le.sort(reverse=True)
    i = 0
    j = 0
    for ele in arr:
        if(ele%2==0):
            print(chan[i], end = ' ')
            i+=1
        else:
            print(le[j], end = ' ')
            j+=1
def check(current):
    cnt = 0
    if(current[0] == 0):
        return 0
    for ele in current:
        if(ele == 2):
            cnt += 1
    if(cnt > len(current)/2):
        return 1
    return 0
tp_arr = []
def qlui(n, current=[]):
    if(len(tp_arr) > 1000):
        return
    if(len(current) == n):
        if(check(current)):
            tp_arr.append("".join(map(str, current)))
            if(len(tp_arr) > 1000):
                return
        return
    for i in range(0, 3):
        current.append(i)
        qlui(n, current)
        current.pop()
        
    
if __name__ == '__main__':
    t = int(input())
    for i in range(1,10):
        qlui(i)
    while(t > 0):
        n = int(input())
        for i in range(n):
            print(tp_arr[i], end = " ")
        print()
        t-=1
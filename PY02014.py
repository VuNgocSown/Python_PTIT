nt = [1] * 10000
def sang():
    nt[0]=0
    nt[1]=0
    for i in range(2, 100):
        if(nt[i]):
            for j in range(i*i, 10000, i):
                nt[j]=0
if __name__ == '__main__':
    n = int(input())
    arr = [int(i) for i in input().split()]
    cnt = 0
    sang()
    for i in arr:
        if(nt[i]):
            continue
        fw_val = i
        bw_val = i
        cnt_fw = 0
        cnt_bw = 0
        while(nt[fw_val]==0):
            cnt_fw +=1
            fw_val +=1
        while(nt[bw_val]==0):
            cnt_bw +=1
            bw_val -=1
        cnt = max(cnt, min(cnt_bw, cnt_fw))
    print(cnt)
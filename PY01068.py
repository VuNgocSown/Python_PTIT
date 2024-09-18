direct_arr = []
def qlui(i, k, current =[]):
    if(len(current) == k):
        for j in current:
            print(direct_arr[j], end = ' ')
        print()
        # for j in current:
        #     print(j, end = ' ')
        # print()
        return
    for j in range(i, len(direct_arr)):
        current.append(j)
        qlui(j+1, k, current)
        current.pop()
if __name__ == '__main__':
    n, k = map(int, input().split())
    direct_arr = list(set(input().split()))
    direct_arr.sort()
    qlui(0, k)
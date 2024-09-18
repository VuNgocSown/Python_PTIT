if __name__ == '__main__':
    n = int(input())
    arr = [int(i) for i in input().split()]
    idx = 0
    min_val = 1e9
    for i in range(n):
        sum = 0
        for j in range(n):
            sum += abs(arr[j]-arr[i])
        if(sum < min_val):
            min_val = sum
            idx=arr[i]
    print(min_val, idx) 
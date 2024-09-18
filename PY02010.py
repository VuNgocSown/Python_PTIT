if __name__ == '__main__':
    while(True):
        n = int(input())
        if(n == 0):
            break
        arr = []
        for i in range(n):
            arr.append(int(input()))
        arr.sort()
        if(arr[0] == arr[-1]):
            print("BANG NHAU")
        else:
            print(arr[0], arr[-1])
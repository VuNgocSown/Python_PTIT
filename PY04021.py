class Net:
    def __init__(self, id, name, hour, minute):
        self.id = id
        self.name = name
        self.hour = hour
        self.minute= minute
    def __str__(self):
        return f"{self.id} {self.name} {self.hour} gio {self.minute} phut"

if __name__=='__main__':
    n = int(input())
    arr = []
    for i in range(n):
        id = input()
        name = input()
        h1, m1 = map(int, input().split(":"))
        h2, m2 = map(int, input().split(":"))
        if m2 < m1:
            m2+=60
            h2-=1
        minute = (h2-h1)*60+(m2-m1)
        p = Net(id, name, minute//60, minute%60)
        arr.append(p)
    arr.sort(key=lambda x: (-x.hour, -x.minute))
    for ele in arr:
        print(ele)
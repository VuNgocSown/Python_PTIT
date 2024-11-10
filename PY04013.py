class Rain:
    counter = 1
    def __init__(self, name, time, capacity):
        self.id = f"T{Rain.counter:02d}"
        Rain.counter += 1
        self.name = name
        self.time = time
        self.capacity = capacity
    def calculate(self):
        self.capacity = self.capacity/(self.time/60)
    def __str__(self):
        return f"{self.id} {self.name} {self.capacity:.2f}"
if __name__ == '__main__':
    n = int(input())
    arr = []
    for i in range(n):
        name = input()
        hour1, minute1 = map(int, input().split(":"))
        hour2, minute2 = map(int, input().split(":"))
        if(minute1 > minute2):
            hour2 -= 1
            minute2 += 60
        time = (hour2-hour1)*60+(minute2-minute1)
        capacity = float(input())
        check = False
        # print(time, capacity)
        for ele in arr:
            if(ele.name == name):
                ele.time += time
                ele.capacity+=capacity
                check = True
        if not check:
            kv = Rain(name, time, capacity)
            arr.append(kv)
    for ele in arr:
        ele.calculate()
        print(ele)

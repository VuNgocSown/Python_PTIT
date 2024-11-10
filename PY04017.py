class Race:
    def __init__(self, name, unit, speed, time):
        self.name = name
        self.unit = unit
        self.speed = round(speed)
        self.time = time
    def handle(self, name, unit):
        id = "".join([word[0] for word in unit.upper().split()])+"".join(word[0] for word in name.upper().split())
        return id
    def __str__(self):
        return f"{self.handle(self.name, self.unit)} {self.name} {self.unit} {self.speed} Km/h"
if __name__ == '__main__':
    n = int(input())
    arr = []
    for i in range(n):
        name = input()
        unit = input()
        hour, minute = map(int,input().split(":"))
        time = (hour-6)*60+minute
        speed = 120/time*60
        p = Race(name, unit, speed, time)
        arr.append(p)
    arr.sort(key = lambda x: (x.time))
    for ele in arr:
        print(ele)
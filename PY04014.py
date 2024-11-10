import math

def category(point):
    average = point
    if average >= 9:
        return "XUAT SAC"
    elif average >= 8:
        return "GIOI"
    elif average >= 7:
        return "KHA"
    elif average >= 5:
        return "TB"
    else:
        return "YEU"

class Point:
    counter = 1

    def __init__(self, name, m1, m2, m3, m4, m5, m6, m7, m8, m9, m10):
        self.id = f"HS{Point.counter:02d}"
        Point.counter += 1
        self.name = name
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        self.m4 = m4
        self.m5 = m5
        self.m6 = m6
        self.m7 = m7
        self.m8 = m8
        self.m9 = m9
        self.m10 = m10
        self.average = (self.m1 * 2 + self.m2 * 2 + self.m3 + self.m4 + self.m5 + self.m6 + self.m7 + self.m8 + self.m9 + self.m10)/10/1.2
        self.average = round(self.average, 2)
    def __str__(self):
        return f"{self.id} {self.name} {self.average:.1f} {category(self.average)}"

if __name__ == '__main__':
    n = int(input())
    arr = []
    for i in range(n):
        name = input()
        m1, m2, m3, m4, m5, m6, m7, m8, m9, m10 = map(float, input().split())
        p = Point(name, m1, m2, m3, m4, m5, m6, m7, m8, m9, m10)
        arr.append(p)
    arr.sort(key=lambda x: (-x.average))
    for ele in arr:
        print(ele)
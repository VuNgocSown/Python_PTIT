import math
class Triango:
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
    def chuVi(self):
        a = math.sqrt((self.x1-self.x2)**2 + (self.y1-self.y2)**2)
        b = math.sqrt((self.x1-self.x3)**2 + (self.y1-self.y3)**2)
        c = math.sqrt((self.x3-self.x2)**2 + (self.y3-self.y2)**2)
        return a, b, c
    
    def dienTich(self):
        self.a, self.b, self.c = self.chuVi
        

if __name__ == '__main__':
    t = int(input())
    result = []
    while(t > 0):
        x1, y1, x2, y2, x3, y3 = map(int, input().split())
        if(x1==x2==x3 or y1 == y2 == y3):
            result.append("INVALID")
        else:
            triang = Triango(x1, y1, x2, y2, x3, y3)
            result.append(triang)
        t-=1
    for x in result:
        print(x)
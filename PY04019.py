def state(score):
    if score > 9.5: return "XUAT SAC"
    elif score >= 8: return "DAT"
    elif score >= 5: return "CAN NHAC"
    else: return "TRUOT"
class NV:
    counter = 1
    def __init__(self, name, score):
        self.id = f"TS0{NV.counter:01d}"
        NV.counter += 1
        self.name = name
        self.score = score
    def __str__(self):
        return f"{self.id} {self.name} {self.score:.2f} {state(self.score)}"
if __name__ == '__main__':
    n = int(input())
    arr = []
    for i in range(n):
        name = input()
        lt = float(input())
        if(lt > 10):
            lt /= 10
        th = float(input())
        if(th > 10):
            th /= 10
        ts = NV(name, (lt+th)/2)
        arr.append(ts)
    arr.sort(key = lambda x: (-x.score))
    for ele in arr:
        print(ele)
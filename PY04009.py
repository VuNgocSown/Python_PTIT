class SV:
    def __init__(self, name, birth, m1, m2, m3):
        self.name = name
        self.birth = birth
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    def __str__(self):
        return f"{self.name} {self.birth} {(self.m1+self.m2+self.m3):.1f}"
if __name__ == '__main__':
    name = input()
    birth = input()
    m1 = float(input())
    m2 = float(input())
    m3 = float(input())
    sv = SV(name, birth, m1, m2, m3)
    print(sv)
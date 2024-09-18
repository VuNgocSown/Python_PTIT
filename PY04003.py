import math
class PhanSo:
    def __init__(self, tu, mau):
        self.tu = tu
        self.mau = mau
    def rg(self):
        ucln = math.gcd(self.tu, self.mau)
        self.tu //= ucln
        self.mau //=ucln
        return f'{self.tu}/{self.mau}'
if __name__ == '__main__':
    tu, mau = map(int, input().split())
    ps = PhanSo(tu, mau)
    print(ps.rg())
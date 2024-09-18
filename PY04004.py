import math
class PhanSo:
    def __init__(self, tu, mau):
        self.tu = tu
        self.mau = mau
    def rg(self):
        ucln = math.gcd(self.tu, self.mau)
        self.tu //= ucln
        self.mau //= ucln
    def cong(self, other):
        new_tu = self.tu * other.mau + other.tu*self.mau
        new_mau = self.mau * other.mau
        result = PhanSo(new_tu, new_mau)
        result.rg()
        return result
    def __str__(self):
        return f'{self.tu}/{self.mau}'
if __name__ == '__main__':
    x, y, z, t = map(int, input().split())
    p = PhanSo(x, y)
    q = PhanSo(z, t)
    result = p.cong(q)
    print(result)
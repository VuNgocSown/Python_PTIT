import math
class Matrix:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.data = [[0 for _ in range(n)] for _ in range(m)]
    def input_matrix(self):
        for i in range(n):
            self.data[i]=list(map(int, input().split()))
    def transpose(self):
        transposed_mtr = Matrix(self.m, self.n)
        for i in range(self.m):
            for j in range(self.n):
                transposed_mtr.data[i][j]=self.data[j][i]
        return transposed_mtr
    def mulmtr(self, other):
        result = Matrix(self.n, self.n)
        result.data = [[0 for _ in range(self.n)] for _ in range(self.n)]
        for i in range(self.n):
            for j in range(self.m):
                for k in range(self.n):
                    result.data[i][j]+= self.data[i][k]*other.data[k][j]
        return result
    def __str__(self):
        result = []
        for row in self.data:
            result.append(" ".join(map(str, row)))
        return "\n".join(result)
                
if __name__ == '__main__':
    t = int(input())
    while(t > 0):
        n, m = map(int, input().split())
        mtr1 = Matrix(n, m)
        mtr1.input_matrix()
        mtr2 = mtr1.transpose()
        mtr3 = Matrix(n, n)
        mtr3 = mtr1.mulmtr(mtr2)
        print(mtr3)
        t-=1
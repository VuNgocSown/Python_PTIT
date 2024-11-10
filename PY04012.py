class SV:
    def __init__(self, id, name, className):
        self.id = id
        self.name = name
        self.className = className
class HP:
    def __init__(self, id, attend):
        self.id = id
        self.attend = attend
    def calculate_score(self):
        score = 10
        for ele in self.attend:
            if ele == 'v':
                score -=2
            elif ele == 'm':
                score -=1
        return max(score, 0)
if __name__=='__main__':
    n = int(input())
    svs = []
    attendances = []
    for i in range(n):
        id = input()
        name = input()
        className = input()
        sv = SV(id, name, className)
        svs.append(sv)
    for i in range(n):
        data = input().split()
        id = data[0]
        attend = data[1]
        hp = HP(id, attend)
        attendances.append(hp)
    for sv in svs:
        for attend in attendances:
            if(sv.id == attend.id):
                score = attend.calculate_score()
                if(score == 0):
                    print(f"{sv.id} {sv.name} {sv.className} {score} KDDK")
                else:
                    print(f"{sv.id} {sv.name} {sv.className} {score}")

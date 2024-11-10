from datetime import datetime
class KH:
    counter = 1
    def __init__(self, name, room, day, price):
        self. id = f"KH{KH.counter:02d}"
        KH.counter+=1
        self.name = name
        self.room = room
        self.day = day
        self.price = price
    def __str__(self):
        return f"{self.id} {self.name} {self.room} {self.day} {self.price}"
def cal_price(room, day):
    price = 0
    if(room == '1'):
        price = 25 * day
    elif room == '2':
        price = 34 * day
    elif room == '3':
        price = 50 * day
    else:
        price = 80 * day
    return price
if __name__ == '__main__':
    n = int(input())
    arr = []
    for i in range(n):
        name = input().strip()
        room = input().strip()
        be = input().strip()
        ed = input().strip()
        fee = int(input())
        date_format = "%d/%m/%Y"
        be = datetime.strptime(be, date_format)
        ed = datetime.strptime(ed, date_format)
        delta = ed - be
        day = delta.days+1
        totalPrice = cal_price(room[0], day) + fee
        kh = KH(name, room, day, totalPrice)
        arr.append(kh)
    arr.sort(key = lambda x: (-x.price))
    for ele in arr:
        print(ele)
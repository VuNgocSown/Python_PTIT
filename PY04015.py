class HD:
    counter = 1
    def __init__(self, name, price):
        self.id = f"KH{HD.counter:02d}"
        HD.counter += 1
        self.name = name
        self.price = price
    def __str__(self):
        return f"{self.id} {self.name} {self.price}"
def totalPrice(num):
    price = 0
    if(num > 100):
        price = (num-100)*200+50*150+50*100
        price += price*0.05
    elif(num > 50):
        price = (num-50)*150 + 50*100
        price += price*0.03
    else:
        price = num*100 + num*100*0.02
    return round(price)
if __name__ == '__main__':
    n = int(input())
    arr = []
    for i in range(n):
        name = input()
        be = int(input())
        af = int(input())
        price = totalPrice(af-be)
        kh = HD(name, int(price))
        arr.append(kh)
    arr.sort(key = lambda x: (-x.price))
    for ele in arr:
        print(ele)
class Phone:
    def __init__(self,price,name):
        self.price=price
        self.name=name

    def __add__(self, other):
        return self.price+other.price

p1=Phone(500,'Apple')
p2=Phone(1000,'Nokia')
print(p1+p2)

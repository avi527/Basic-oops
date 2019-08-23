class Mobile:
    def __init__(self,brand,ram,price):
        self.brand=brand
        self.ram=ram
        self.price=price
    def applyDiscount(self,offer_prc):
        self.offer_prc=offer_prc
        off_price= (offer_prc/100) * self.price
        return self.price-off_price

m=Mobile('mi','4gb',63000)
print(m.applyDiscount(10))

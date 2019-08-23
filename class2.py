class Laptop:
    def __init__(self,brand,model_name,price):
        self.model_name=model_name
        self.brand=brand
        self.price=price
#create another instance variable
        self.laptop_name=model_name +' '+brand
obj1=Laptop('hp','hp009',63000)
print(obj1.model_name,obj1.brand,obj1.price)
print(obj1.laptop_name)

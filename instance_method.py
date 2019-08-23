class Person:
    def __init__(self,first_name,last_name,age):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
    def full_name(self):
        return self.first_name + ' '+self.last_name
    def check_age(self):

        if (self.age>18):
            return True

p1=Person('avinash','singh',19)
print(p1.first_name,p1.last_name,p1.age)
print('-------------print call full name method--------------------')
print(p1.full_name())
print('-------------print call check age method--------------------')
print(p1.check_age())

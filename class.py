class Person:
    def __init__(self,first_name,last_name,mobile):
        #instance variable
        print('instance method called')
        self.first_name=first_name
        self.last_name=last_name
        self.mobile=mobile
p_obj=Person('avinash','singh',8745016128)
p_obj2=Person('sudheer','singh',5986586578685)
print(p_obj.last_name)
print(p_obj2.first_name)

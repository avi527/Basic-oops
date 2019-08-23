class Person:
    instance_count=0
    def __init__(self,name):
        Person.instance_count+=1
        self.name=name
p=Person('avinash')
p1=Person('avinash')
print(Person.instance_count)


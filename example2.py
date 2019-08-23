#Write a program with class employee that keeps a track of the number of
#employees in an organization and also store thier name,designation,and
#salary details
class Employee:
    emp_count=0
    def __init__(self,name,designation,salary):
        self.name=name
        self.designation=designation
        self.salary=salary
        Employee.emp_count +=1
    def countEmp(self):
        print(f"total employee is {Employee.emp_count}")
    def detailEmp(self):
        print(f"name is : {self.name}")
        print(f"designation is : {self.designation}")
        print(f"salary is : {self.salary}")
e1=Employee("Avinash","Python Developer",250000)
e2=Employee("Avinash singh","Php",850000)
e1.countEmp()
e1.detailEmp()
e2.countEmp()
e2.detailEmp()


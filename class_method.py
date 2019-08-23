class Myclass():
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    @classmethod
    def mymethod(cls,string):
        f,l=string.split(',')
        return cls(f,l)

m=Myclass('aaa','sss')
m1=Myclass.mymethod('hh,pp')





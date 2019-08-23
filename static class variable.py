class Circle:
    pie=3.14
    def __init__(self,radius):
        self.radius=radius
    def circumfernce(self):
        return (2 * Circle.pie * self.radius)
c=Circle(5)
print(c.circumfernce())

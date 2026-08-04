
class circle:
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return (22/7)*self.radius**2
    def perimter(self):
        return 2*(22/7)*self.radius
c1=circle(4)
print(c1.area())
print(c1.perimter())

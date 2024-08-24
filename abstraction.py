from abc import ABC,abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass



class Circle(Shape):

    def __init__(self,radius):
        self.radius = radius


    def __str__(self):
        return "Circle"


    def area(self):
        print(3.14*self.radius*self.radius)



class Rectangle(Shape):
    def __init__(self,l,b):
        self.l = l
        self.b = b


    def __str__(self):
        return "Rectangle"


    def area(self):
        print(self.l*self.b)


sh1 = Circle(5)
sh2 = Rectangle(3,4)

print(sh1)
print(sh2)

sh1.area()
sh2.area()

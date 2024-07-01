class Shape:
    def __init__(self):
        self.color = (0, 0, 0)


class Rectangle(Shape):
    def __init__(self, h, w):
        Shape.__init__(self) #Need to call constructor function of superclass
        self.height = h
        self.width = w


    def area(self):
        return self.height * self.width 
    


rect1 = Rectangle(2, 4)
print(rect1.height, rect1.width, rect1.area(), rect1.color)
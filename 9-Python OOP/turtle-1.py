import turtle

               #Inheritance
class NewTurtle(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("turtle")

    def forward(self, x):
        # self.backward(2 * x)
        self.left(90)
        self.forward(x)

nonte = turtle.Turtle()
nonte.forward(100)

nonte = NewTurtle()
nonte.forward(100)

turtle.done()

#in python if we use '_' starting of a variable or method, it is known as private (though it is not private)
#ex: _num, _add() etc.
import turtle as t
import numpy as np
class Turtle:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.t = t.Turtle()
        self.t.penup()
        self.t.goto(x, y)
        self.t.pendown()
        self.t.color(color)
    def forward(self, distance):
        self.t.forward(distance)
    def backward(self, distance):
        self.t.backward(distance)
    def left(self, angle):
        self.t.left(angle)
    def right(self, angle):
        self.t.right(angle)
    def penup(self):
        self.t.penup()
    def pendown(self):
        self.t.pendown()
    def color(self, color):
        self.t.color(color)


    def ReadPosition(turtle):
        """Read the position of the turtle"""
        # get the position of the turtle and name of each turtle
        position = turtle.t.pos()
        name = turtle.t
        # print the position of the turtle
        print("Position of {}: {}".format(name, position))
        return 1
# create a drawing of rhombicosidodecahedron
    def rhombicosidodecahedron():
        t1 = Turtle(0, 0, "red")
        t2 = Turtle(0, 0, "green")
        t3 = Turtle(0, 0, "blue")
        turtles = np.array([t1, t2, t3])
        # create a loop that will draw the rhombicosidodecahedron
        for Item in turtles:
            Turtle.ReadPosition(Item)
            if (Item == t1):
                t1.left(90)
                t1.forward(60)
                t1.right(90)
                t1.forward(60)
            if (Item == t2):
                t2.left(-90)
                t2.forward(60)
                t2.right(-90)
                t2.forward(60)
            if (Item == t3):
                t3.forward(60)
                t3.forward(60)
                t3.left(90)
                t3.forward(60)
                t3.right(90)
                t3.forward(60)
        t.done()
        return 1
# run the turtle

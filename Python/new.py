import turtle as t
import random as r
class Turtle(object):
    def __init__(self, d1,id):
        self.id = id
        self.d1 = d1
    def test(d1,i):
        print("Running Test(s): %s" % i)
        for x in range(0,i):
            print(1+x,2+x,3+x)
        return 
for i in range(0, 20):
    c = Turtle(t,1).d1 = i
    a = Turtle(t,2).test = True
    Turtle.test(t.color('blue'),0)
    Turtle.test(t.bgcolor('black'),1)
    Turtle.test(t.forward(r.randint(0,90)),2)
    Turtle.test(t.right(r.randint(0,90)),3)
    Turtle.test(t.fd(45.50),4)
    Turtle.test(t.degrees(r.randint(0,360)),5)
    Turtle.test(t.fd(r.randint(0,180)),6)
    Turtle.test(t.home(),7)
    

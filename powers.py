from turtle import Turtle

class BigPaddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("green")
        self.speed = -3
        self.penup()
        self.goto(x=1000, y=1000)

    def fall(self):
        self.sety(self.ycor() + self.speed)

class MultiBalls(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("blue")
        self.speed = -3
        self.penup()
        self.goto(x=1000, y=1000)

    def fall(self):
        self.sety(self.ycor() + self.speed)





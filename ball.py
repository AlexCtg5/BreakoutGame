from turtle import Turtle

ball_color = "#F6F1EE"

class Ball(Turtle):
    def __init__(self, xcr, ycr):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("#FFCC70")
        self.goto(xcr, ycr)
        self.xball_speed = 3
        self.yball_speed = -3

    def bounce(self):
        self.ball_speed = self.ball_speed * (-1)

class PowerBallOne(Turtle):
    def __init__(self, xcr, ycr):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("#FFE6C7")
        self.goto(xcr, ycr)
        self.power_one_xball_speed = 3
        self.power_one_yball_speed = 3

    def bounce(self):
        self.power_one_ball_speed = self.power_one_ball_speed * (-1)

class PowerBallTwo(Turtle):
    def __init__(self, xcr, ycr):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("#FFE6C7")
        self.goto(xcr, ycr)
        self.power_two_xball_speed = -3
        self.power_two_yball_speed = 3

    def bounce(self):
        self.power_two_ball_speed = self.power_two_ball_speed * (-1)


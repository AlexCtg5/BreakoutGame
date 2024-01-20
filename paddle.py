from turtle import Turtle
class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("#FFCC70")
        self.penup()
        self.shapesize(stretch_wid=0.75, stretch_len=6, outline=None)
        self.goto(x=0, y=-260)
        self.player_speed = 0
        self.type = "small"
        self.big_paddle_hp = 3

    def move_left(self):
        self.player_speed = -6

    def move_right(self):
        self.player_speed = 6

    def stop(self):
        self.player_speed = 0

    def big_paddle(self):
        self.shapesize(stretch_wid=0.75, stretch_len=12, outline=None)
        i=0
        for i in range(10):
            if i >= 9:
                self.shapesize(stretch_wid=0.75, stretch_len=6, outline=None)



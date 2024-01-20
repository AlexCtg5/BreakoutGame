from turtle import Turtle

class Squares(Turtle):
    def __init__(self, position, color, hp):
        super().__init__()
        self.penup()
        self.goto(position)
        self.shape("square")
        self.color(color)
        self.hp = hp
        self.shapesize(stretch_wid=1.5, stretch_len=3, outline=None)



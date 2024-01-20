from turtle import Screen
from paddle import Paddle
from squares import Squares
from ball import Ball, PowerBallOne, PowerBallTwo
from powers import BigPaddle, MultiBalls
import random
import os
from tkmacosx import Button

#-------------------------Screen-Setup-------------------------
BG = "#22092C"
screen = Screen()
screen.title("Breakout")
screen.setup(width=800, height=600)
screen.bgcolor(BG)
screen.tracer(0)
screen.listen()

#------------------------Setup_Squares-------------------------
#Squares-colors:
three_hits = "#872341"
two_hits = "#BE3144"
one_hit = "#F05941"
#
square_list = []
x= -361
y = 270
for i in range(1,13):
    square = Squares((x, y), three_hits, 3)
    square_list.append(square)
    x += 65
x = -361
y = 235
for i in range(1,13):
    square = Squares((x, y), three_hits, 3)
    square_list.append(square)
    x += 65
x = -361
y = 200
for i in range(1,13):
    square = Squares((x, y), two_hits, 2)
    square_list.append(square)
    x += 65
x = -361
y = 165
for i in range(1,13):
    square = Squares((x, y), two_hits, 2)
    square_list.append(square)
    x += 65
x = -361
y = 130
for i in range(1,13):
    square = Squares((x, y), one_hit, 1)
    square_list.append(square)
    x += 65
x = -361
y = 95
for i in range(1,13):
    square = Squares((x, y), one_hit, 1)
    square_list.append(square)
    x += 65

#-----------Paddle_and_paddle_movement-----------
paddle = Paddle()
screen.onkeypress(fun=paddle.move_left, key="a")
screen.onkeypress(fun=paddle.move_right, key="d")
screen.onkeyrelease(fun=paddle.stop, key="a")
screen.onkeyrelease(fun=paddle.stop, key="d")
#----------------------Ball-––––––----------------
ball = Ball(xcr=-3,ycr=10)
#Power balls
power_ball_one = PowerBallOne(xcr=1000, ycr=1000)
power_ball_two = PowerBallTwo(xcr=1000, ycr=1000)
#----------------Power-----------
power = BigPaddle()
balls_power = MultiBalls()
#--------------------Game-Settings----------------
screen.update()
is_going = True
while is_going:
    #Remove widget
    # start_button.destroy()
    # exit_button.destroy()
    #Paddle, powers and balls speed
    paddle.setx(paddle.xcor() + paddle.player_speed)
    ball.setx(ball.xcor() + ball.xball_speed)
    ball.sety(ball.ycor() + ball.yball_speed)
    power_ball_one.setx(power_ball_one.xcor() + power_ball_one.power_one_xball_speed)
    power_ball_one.sety(power_ball_one.ycor() + power_ball_one.power_one_yball_speed)
    power_ball_two.setx(power_ball_two.xcor() + power_ball_two.power_two_xball_speed)
    power_ball_two.sety(power_ball_two.ycor() + power_ball_two.power_two_yball_speed)
    power.fall()
    balls_power.fall()
    # Paddle margins limit
    if paddle.xcor() > 325:
        paddle.setx(325)
    if paddle.xcor() < -330:
        paddle.setx(-330)
    # Collision ball with down margin and reset game
    if ball.ycor() < -290:
        ball.goto(0, 0)
    #Collision ball with paddle
    if ball.distance(paddle) <= 65 and ball.ycor() <= -250 and paddle.type == "small":
        ball.yball_speed *= -1
    if ball.distance(paddle) <= 125 and ball.ycor() <= -250 and paddle.type == "big":
        ball.yball_speed *= -1
    #Collision ball with margins
    if ball.xcor() > 380:
        ball.xball_speed *= -1
    if ball.xcor() < -380:
        ball.xball_speed *= -1
    if ball.ycor() > 290:
        ball.yball_speed *= -1
    #Collision ball with squares
    for n in square_list:
        if n.distance(ball) <= 30:
            ball.yball_speed *= -1
            if n.hp == 3:
                n.hp -= 1
                n.color(two_hits)
            elif n.hp == 2:
                n.hp -= 1
                n.color(one_hit)
            else:
                #power drop
                multi_balls_drop_chance = random.randint(1,3)
                big_paddle_drop_chance = random.randint(1,3)
                if multi_balls_drop_chance == 1:
                    balls_power.goto(n.xcor(), n.ycor())
                if big_paddle_drop_chance == 2:
                    power.goto(n.xcor(), n.ycor())
                if paddle.type == "big":
                    paddle.big_paddle_hp -= 1
                #square delete
                n.goto(1000, 1000)
    #Check big paddle hp and turns it small if 0
    if paddle.big_paddle_hp == 0:
        paddle.shapesize(stretch_wid=0.75, stretch_len=6, outline=None)
        paddle.big_paddle_hp = 3

    #Collision big paddle power with paddle
    if power.ycor() <= -250 and power.distance(paddle) <= 65 and paddle.type == "small":
        power.goto(x=1000, y=1000)
        paddle.shapesize(stretch_wid=0.75, stretch_len=12, outline=None)
        paddle.type = "big"
    if power.ycor() <= -250 and power.distance(paddle) <= 125 and paddle.type == "big":
        power.goto(x=1000, y=1000)
        paddle.shapesize(stretch_wid=0.75, stretch_len=12, outline=None)
        paddle.type = "big"
    #Collision multi balls power with paddle
    if balls_power.ycor() <= -250 and balls_power.distance(paddle) <= 65 and paddle.type == "small":
        balls_power.goto(x=1000, y=1000)
        power_ball_one.goto(x=0, y=0)
        power_ball_two.goto(x=0, y=0)
    if balls_power.ycor() <= -250 and balls_power.distance(paddle) <= 125 and paddle.type == "big":
        balls_power.goto(x=1000, y=1000)
        power_ball_one.goto(x=0, y=0)
        power_ball_two.goto(x=0, y=0)

    #Collision power balls with paddle
    #power ball one
    if power_ball_one.distance(paddle) <= 65 and power_ball_one.ycor() <= -250 and paddle.type == "small":
        power_ball_one.power_one_yball_speed *= -1
    if power_ball_one.distance(paddle) <= 125 and power_ball_one.ycor() <= -250 and paddle.type == "big":
        power_ball_one.power_one_yball_speed *= -1
    #power ball two
    if power_ball_two.distance(paddle) <= 65 and power_ball_two.ycor() <= -250 and paddle.type == "small":
        power_ball_two.power_two_yball_speed *= -1
    if power_ball_two.distance(paddle) <= 125 and power_ball_two.ycor() <= -250 and paddle.type == "big":
        power_ball_two.power_two_yball_speed *= -1

    #Collision power balls with margins
    #power ball one
    if power_ball_one.xcor() > 380:
        power_ball_one.power_one_xball_speed *= -1
    if power_ball_one.xcor() < -380:
        power_ball_one.power_one_xball_speed *= -1
    if power_ball_one.ycor() > 290:
        power_ball_one.power_one_yball_speed *= -1
    #power ball two
    if power_ball_two.xcor() > 380:
        power_ball_two.power_two_xball_speed *= -1
    if power_ball_two.xcor() < -380:
        power_ball_two.power_two_xball_speed *= -1
    if power_ball_two.ycor() > 290:
        power_ball_two.power_two_yball_speed *= -1

    #Collision power balls with squares
    #power ball one
    for n in square_list:
        if n.distance(power_ball_one) <= 30:
            power_ball_one.power_one_yball_speed *= -1
            if n.hp == 3:
                n.hp -= 1
                n.color(two_hits)
            elif n.hp == 2:
                n.hp -= 1
                n.color(one_hit)
            else:
                #square delete
                n.goto(1000, 1000)
    #power ball two
    for n in square_list:
        if n.distance(power_ball_two) <= 30:
            power_ball_two.power_two_yball_speed *= -1
            if n.hp == 3:
                n.hp -= 1
                n.color(two_hits)
            elif n.hp == 2:
                n.hp -= 1
                n.color(one_hit)
            else:
                #square delete
                n.goto(1000, 1000)

    screen.update()


screen.exitonclick()
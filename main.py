from turtle import Screen
from paddle import Paddle
from dotted_line import Lines
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()

screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)
line = Lines()
ball = Ball()
score = Scoreboard()

l_paddle = Paddle((-360, 0))
r_paddle = Paddle((360, 0))

screen.listen()
screen.onkey(l_paddle.l_move_up, "w")
screen.onkey(l_paddle.l_move_down, "x")

screen.onkey(r_paddle.r_move_up, "p")
screen.onkey(r_paddle.r_move_down, "m")


is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    ball.move_ball()

    # detect collision with the roof and bottom of the screen
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.change_y()

    # detect collision with ball and right paddle
    if r_paddle.distance(ball) < 50 and ball.xcor() > 340:
        ball.change_x()
    else:
        score.increase_l_score()


    #  detect collision with ball and left paddle
    if ball.distance(l_paddle) < 50 and ball.xcor() > -340:
        ball.change_x()
    else:
        score.increase_r_score()


screen.exitonclick()
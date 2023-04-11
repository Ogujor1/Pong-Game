from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.xmove = 10
        self.ymove= 10

    def move_ball(self):
        new_x = self.xcor() + self.xmove
        new_y = self.ycor() + self.ymove
        self.goto(new_x, new_y)

    def change_y(self):
        self.ymove *= -1

    def change_x(self):
        self.xmove *= -1

    def reset_game(self):
        self.goto(0, 0)
        self.change_x()
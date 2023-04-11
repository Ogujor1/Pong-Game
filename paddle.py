from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.color('white')
        self.shape('square')
        self.shapesize(stretch_wid=4, stretch_len=1)
        self.penup()
        self.goto(position)

    def l_move_up(self):
        newup_y = self.ycor() + 10
        self.goto(-360, newup_y)

    def l_move_down(self):
        newdown_y = self.ycor() - 10
        self.goto(-360, newdown_y)

    def r_move_up(self):
        newup_y = self.ycor() + 10
        self.goto(360, newup_y)

    def r_move_down(self):
        newdown_y = self.ycor() - 10
        self.goto(360, newdown_y)
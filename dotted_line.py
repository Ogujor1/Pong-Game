from turtle import Turtle


class Lines(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('square')
        self.setheading(90)
        self.color('white')
        self.penup()
        self.goto(0, -300)
        self.draw_line()

    def draw_line(self):
        for num in range(50):
            self.penup()
            self.forward(10)
            self.pendown()
            self.forward(10)
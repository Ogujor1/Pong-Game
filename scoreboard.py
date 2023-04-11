from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color('white')
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    def update_score(self):
        self.goto(-100, 240)
        self.write(f'{self.l_score}', align='center', font=('Arial', 12, 'normal'))
        self.goto(100, 240)
        self.write(f'{self.r_score}', align='center', font=('Arial', 12, 'normal'))

    def increase_l_score(self):
        self.clear()
        self.l_score += 1
        self.update_score()

    def increase_r_score(self):
        self.clear()
        self.r_score += 1
        self.update_score()
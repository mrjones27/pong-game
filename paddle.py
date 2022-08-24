from turtle import Turtle

PADDLE_LENGTH = 1
PADDLE_WIDTH = 5

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=PADDLE_WIDTH, stretch_len=PADDLE_LENGTH)
        self.goto(350, 0)

    def go_up(self):
        """Move paddle up"""
        new_y_pos = self.ycor() + 20
        self.sety(new_y_pos)

    def go_down(self):
        """Move paddle down"""
        new_y_pos = self.ycor() - 20
        self.sety(new_y_pos)

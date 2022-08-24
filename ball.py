from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10

    def move(self):
        """Move's the ball"""
        new_x_position = self.xcor() + self.x_move
        new_y_position = self.ycor() + self.y_move
        self.goto(new_x_position, new_y_position)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1


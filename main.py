from turtle import Screen
import time
from ball import Ball
from paddle import Paddle

game_is_on = True

# define screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# create paddles
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

# create ball
ball = Ball()

screen.listen()

# Right Player shortcuts
screen.onkey(fun=r_paddle.go_up, key="Up")
screen.onkey(fun=r_paddle.go_down, key="Down")

# Left Player shortcuts
screen.onkey(fun=l_paddle.go_up, key="w")
screen.onkey(fun=l_paddle.go_down, key="s")

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # detect wall collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect r_paddle collision
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() > -340):
        ball.bounce_x()
screen.exitonclick()

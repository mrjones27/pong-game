from turtle import Screen
from paddle import Paddle

game_is_on = True

# define screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
paddle = Paddle()

# key shortcuts
screen.listen()
screen.onkey(fun=paddle.go_up, key="Up")
screen.onkey(fun=paddle.go_down, key="Down")
while game_is_on:
    screen.update()


screen.exitonclick()


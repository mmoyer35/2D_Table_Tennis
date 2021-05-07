from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Set up screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

# Create paddle, ball, and scoreboard objects
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

# Paddle input
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

# reset both paddles, reset the ball and return it to the original speed.
def new_volley():
    r_paddle.reset_position()
    l_paddle.reset_position()
    ball.point_scored()
    screen.update()
    time.sleep(1)


# Game loop
game_is_on = True
while game_is_on:
    screen.update()
    ball.move()
    time.sleep(0.01)
    #Detect collision with wall
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()

    #Detect collision with paddles
    if ball.distance(r_paddle) <= 50 and ball.xcor() >= 330 or ball.distance(l_paddle) <= 50 and ball.xcor() <= -330:
        # movement speed increases by 7.5% each time a player successfully hits the ball
        ball.x_move = ball.x_move * 1.075
        ball.y_move = ball.y_move * 1.075
        ball.bounce_x()
        time.sleep(0.01)

    #Detect R paddle misses, add point to scoreboard and reset
    if ball.xcor() > 340:
        scoreboard.l_point()
        new_volley()

    #Detect L paddle misses, add point to scoreboard and reset
    if ball.xcor() < -340:
        scoreboard.r_point()
        new_volley()

screen.exitonclick()
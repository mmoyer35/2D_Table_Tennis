from turtle import Turtle
import random
import time


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 2
        self.y_move = 2

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    # bouncing off a top or bottom wall
    def bounce_y(self):
        self.y_move *= -1

    # bouncing off paddles
    def bounce_x(self):
        self.x_move *= -1
        self.move()

    # reset ball position, randomly choose one of four directions for the next game, start movement
    def point_scored(self):
        self.goto(0, 0)
        self.x_move = random.choice([-2,2])
        self.y_move = random.choice([-2,2])
        time.sleep(0.5)
        self.bounce_x()






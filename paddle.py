from turtle import Turtle

class Paddle(Turtle):
    
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    #Paddle movement, prevent it from going off screen.
    def go_up(self):
        if int(self.ycor()) <= 210:
            new_y = self.ycor() + 30
            self.goto(self.xcor(), new_y)

    def go_down(self):
        if int(self.ycor()) >= -210:
            new_y = self.ycor() - 30
            self.goto(self.xcor(), new_y)

    def reset_position(self):
        self.goto((self.xcor(), 0))

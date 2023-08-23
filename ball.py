from turtle import Turtle
import time

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move_ball(self):
        """ Moves the ball"""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """Bounces the ball anytime it hits the top"""
        self.y_move *= -1
        self.move_speed *= 0.7

    def bounce_x(self):
        """Bounces the ball anytime it hits the paddle"""
        self.x_move *= -1

    def reset_ball(self):
        """Restarts the ball whenever the ball goes out and restarts the ball speed"""
        time.sleep(0.4)
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()
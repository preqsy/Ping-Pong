from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)
        self.paddle_position = position

    def go_up(self):
        """controls the paddles upward movements"""
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        """controls the paddles downward movements"""
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)


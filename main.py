from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


ball = Ball()
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong')

speed = 0.1
screen.tracer(0)


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

score = Scoreboard()
screen.listen()
screen.onkeypress(r_paddle.go_up, 'Up')
screen.onkeypress(r_paddle.go_down, 'Down')
screen.onkeypress(l_paddle.go_up, 'w')
screen.onkeypress(l_paddle.go_down, 's')

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    # if r_paddle.ycor() > 250 or r_paddle.ycor() < -250 or l_paddle.ycor() > 250 or l_paddle.ycor() < -250:
    #     print("stop")
    #     game_on = False
    ball.move_ball()

    if ball.ycor() > 280 or ball.ycor() < -280:

        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        score.l_point()
        ball.reset_ball()

    if ball.xcor() < -380:
        score.r_point()
        ball.reset_ball()


screen.exitonclick()


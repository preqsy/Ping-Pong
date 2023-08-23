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
    # Detects when the ball hits the top 
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # Detects when the ball hits the paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    #Detects when the ball passes and when the right user loses
    if ball.xcor() > 400:
        score.l_point()
        ball.reset_ball()
        if score.l_score == 5:
            score.game_over()
            game_on = False
    #Detects when the ball passes and when the left user loses
    if ball.xcor() < -410:
        score.r_point()
        ball.reset_ball()
        if score.r_score == 5:
            score.game_over()
            game_on = False


screen.exitonclick()


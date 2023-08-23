from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    def update_score(self):
        """Update the scores"""
        self.goto(-100, 200)
        self.write(self.l_score, align='center', font=("Courier", 80, 'normal'))
        self.goto(100, 200)
        self.write(self.r_score, align='center', font=("Courier", 80, 'normal'))


    def l_point(self):
        """Increases the left users scores each time the right user miss the ball"""
        self.l_score += 1
        self.clear()
        self.update_score()

    def r_point(self):
        """Increases the right users scores each time the left user miss the ball"""
        self.r_score += 1
        self.clear()
        self.update_score()
        
        
    def game_over(self):
        self.goto(0, 0)
        if self.l_score == 5:
            self.write(f"       GAMEOVER!!!!!🥲😭 \n The left user wins {self.l_score} to {self.r_score}", align='center', font=("Courier", 40, 'normal'))
        elif self.r_score == 5:
            self.write(f"       GAMEOVER!!!!!🥲😭 \n The right user wins {self.r_score} to {self.l_score}", align='center', font=("Courier", 40, 'normal'))

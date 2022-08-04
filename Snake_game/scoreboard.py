from turtle import Turtle, Screen
ALIGNMENT = 'center'
FONT = ('Courier', 24, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(0, 250)
        self.score = 0
        self.color('white')
        self.update_score()


    def update_score(self):
        self.write(f"Score : {self.score}", True, align=ALIGNMENT, font= FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", True, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()






# scoreboard = Scoreboard()
# screen = Screen()
# screen.exitonclick()
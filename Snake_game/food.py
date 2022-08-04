from turtle import Turtle, Screen
import random


class Food(Turtle):

    def __init__(self):
        # self.food = Turtle()
        super().__init__()
        self.shape('circle') # generally its size is 20/20
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5) # Now the size becomes 10/10
        self.color('blue')
        self.speed('fastest')
        self.refresh()


    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)


# food = Food()
# screen = Screen()
# screen.exitonclick()
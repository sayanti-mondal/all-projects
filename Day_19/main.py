import turtle
from turtle import Turtle, Screen
import random
is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title='Make your bet', prompt="Which turtle will win the race? Enter a color: ")
colors = ['red', 'orange', 'yellow','green', 'blue','purple']
y_positions = [-78,-48,-18,12,42,72]
all_turtles = []

for turtle_index in range(6):
    new_turtle = Turtle('turtle')
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    new_turtle.color(colors[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"you've won! The {winning_color} is the winner.")
            else:
                print(f"you've lost! The {winning_color} is the winner.")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)



#
# def move_forward():
#     tim.forward(50)
#
# def move_backward():
#     tim.backward(50)
#
# def clear_screen():
#     tim.clear()
#     tim.pendown()
#     tim.home()
#     tim.penup()
#
# def move_left():
#     tim.setheading(tim.heading() + 10)
#
# def move_right():
#     tim.setheading(tim.heading() - 10)
#
#
#
#
#
#
#
# screen.listen()
# screen.onkey(key='w', fun=move_forward)
# screen.onkey(key='s', fun=move_backward)
# screen.onkey(key='c', fun=clear_screen)
# screen.onkey(key='a', fun=move_left)
# screen.onkey(key='d', fun=move_right)
screen.exitonclick()


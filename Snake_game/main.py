from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("My Snake Game")
screen.tracer(0)

starting_position = [(0, 0), (-20, 0), (-40, 0)]

# segments = []
#
# for position in starting_position:
#     new_segment = Turtle('square')
#     new_segment.color('white')
#     new_segment.penup()
#     new_segment.goto(position)
#     segments.append(new_segment)
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
        # for segment in segments:
        #     segment.forward(20)

    # for seg_num in range(len(segments)-1, 0, -1):
    #     new_x = segments[seg_num-1].xcor() # x coordinate of 2nd last segment
    #     new_y = segments[seg_num-1].ycor() # y coordinate of 2nd last segment
    #     segments[seg_num].goto(new_x, new_y) #moving the last segment to 2nd last's position
    #
    # segments[0].forward(10)
    # segments[0].left(90)



    #Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend_segment()
        scoreboard.increase_score()

    #Detect Collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        is_game_on = False
        scoreboard.game_over()

   # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            is_game_on = False
            scoreboard.game_over()



















screen.exitonclick()

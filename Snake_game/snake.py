from turtle import Turtle
new_segment = Turtle()
STARTING_POSITION = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 10
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
       self.segments = []
       self.create_snake()
       self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
            new_segment = Turtle('square')
            new_segment.color('white')
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def extend_segment(self):
        self.add_segment(self.segments[-1].position())



    def move(self) :
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()  # x coordinate of 2nd last segment
            new_y = self.segments[seg_num - 1].ycor()  # y coordinate of 2nd last segment
            self.segments[seg_num].goto(new_x, new_y)  # moving the last segment to 2nd last's position

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)





# snake = Snake()
# snake.move()
# screen = Screen()
# screen.exitonclick()


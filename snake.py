#1: Create a window
from turtle import Turtle, Screen 
import time

START_POS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
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
        for pos in START_POS:
            self.update(pos)

    def update(self, pos):
        new_seg = Turtle()
        new_seg.shape("square")
        new_seg.color("black")
        new_seg.penup()
        new_seg.goto(pos)
        self.segments.append(new_seg)

    def extend(self):
        self.update(self.segments[-1].position())

    def move_snake(self):
        for move in range(len(self.segments) - 1,  0, -1):
            newx = self.segments[move - 1].xcor()
            newy = self.segments[move - 1].ycor()
            self.segments[move].goto(newx, newy)  
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def bottom(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:    
            self.head.setheading(LEFT)
            

    
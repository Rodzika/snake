from turtle import Turtle
from tkinter import *


SNAKES_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
SNAKE_HEAD_DIRECTIONS = [90, 270, 90, 0]

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.all_snakes = [] 
        
        self.create_snake()
        
        self.snake.head = self.all_snakes[0]
        
        
    def create_snake(self):
        for Snake_position in SNAKES_POSITION:
            self.add_segment(Snake_position)
        self.all_snakes[0].color("red")
        
    def make_snakes_follow(self):
        for seg_num in range(len(self.all_snakes) - 1, 0, -1):
            new_x = self.all_snakes[seg_num - 1].xcor()
            new_y = self.all_snakes[seg_num - 1].ycor()
            self.all_snakes[seg_num].goto(new_x, new_y)
        self.snake_head.forward(MOVE_DISTANCE)
            
    def add_segment(self, position):
        new_snake = Turtle(shape="square")
        new_snake.color("white")
        new_snake.penup()
        new_snake.goto(position)
        self.all_snakes.append(new_snake)
        
    def reset(self):
        for seg in self.all_snakes:
            seg.goto(1000, 1000)
        self.all_snakes.clear()
        self.create_snake()
        self.snake_head = self.all_snakes[0]
        
    def extend(self):
        self.ad_segment(self.all_snaket[-1].position())
        
    def increase_speed(self, increasing_speed):
        self.snake_head.speed(increasing_speed)
        
    def up_arrow_key(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)
            
    def down_arrow_key(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)
            
    def left_arrow_key(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)
            
    def right_arrow_key(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)
            
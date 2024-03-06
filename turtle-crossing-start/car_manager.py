COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
from turtle import Turtle
import random


class CarManager:
    def __init__(self):
        super().init()
        self.shape("square")
        self.color(random.choice(COLORS))
        self.shapesize()
    
